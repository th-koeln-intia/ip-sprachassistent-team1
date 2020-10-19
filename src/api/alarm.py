from flask import jsonify, request
from api.app import app, get_db, query_db
import time
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import datetime
import random
import json

@app.route('/alarm', methods=['POST', 'DELETE', 'GET'])
def alarm():
    if request.method == 'POST':
        get_db().execute('REPLACE INTO alarms (id, hours, minutes, active) VALUES (?,?,?,?)', 
        [request.form['id'], request.form['hours'], request.form['minutes'], request.form['active']])
        get_db().commit()
    
    elif request.method == 'DELETE':
        get_db().execute('DELETE FROM alarms WHERE id=?', [request.form['id']])
        get_db().commit()

    results = []
    alarms = query_db('SELECT * FROM alarms')

    return jsonify(alarms)

@app.route('/alarm/stop', methods=['POST'])
def alarm_stop():
    get_db().execute('UPDATE alarms SET active=0 WHERE id=?', [request.form['id']])
    get_db().commit()

    return True

def alarm_play(alarm):
    in_file = open("./assets/alarm_sounds/"+ str(alarm['sound']) +".wav", "rb")
    data = in_file.read()
    in_file.close()
    
    publish.single("hermes/audioServer/default/playBytes/alarm-" + str(alarm['id']), data, hostname="mosquitto")

def on_play_finished(client, userdata, message):
    active = random.randint(0,1)
    payloadObj = json.loads(message.payload)
    id = payloadObj['id']
    if 'alarm-' in id:
        alarmId = id.split("-")[1]
        alarm = query_db("SELECT * FROM alarms WHERE id=?", [alarmId], True)
        if alarm['active'] == 1:
            alarm_play(alarm)
        else:
            client.unsubscribe("hermes/audioServer/default/playFinished")
    
    return True


@app.cli.command()
def check_alarm():
    now = datetime.datetime.now()

    alarm = query_db('SELECT * FROM alarms WHERE hours=? AND minutes=?', [now.hour, now.minute], True)

    if alarm is None:
        return
    else:
        get_db().execute("UPDATE alarms SET active=1 WHERE id=?", [alarm['id']])
        get_db().commit()
        alarm_play(alarm)
        
        subscribe.callback(on_play_finished, "hermes/audioServer/default/playFinished", hostname="mosquitto")
