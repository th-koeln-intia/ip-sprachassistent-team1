from flask import jsonify, request
from app import app, get_db, query_db
import time
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import datetime

@app.route('/alarm', methods=['POST', 'DELETE', 'GET'])
def alarm():
    if request.method == 'POST':
        get_db().execute('REPLACE INTO alarms (id, hours, minutes, active) VALUES (?,?,?,?)', 
        [request.form['id'], request.form['hours'], request.form['minutes'], request.form['active']])
        get_db().commit()
    
    elif request.method == 'DELETE':
        get_db().execute('DELETE FROM alarms WHERE id=?', [request.form['id']])

    results = []
    alarms = query_db('SELECT * FROM alarms')

    return jsonify(alarms)

def alarm_play(alarm):
    in_file = open("./assets/alarm_sounds/"+ alarm['sound'] +".wav", "rb")
    data = in_file.read()
    in_file.close()
    
    publish.single("hermes/audioServer/alert/playBytes/fff", data, hostname="mosquitto")

def on_play_finished():
    now = datetime.datetime.now()
    return str(now.hour)
    alarm = query_db('SELECT * FROM alarms WHERE id=0', (), True)
    return str(alarm['hours'])

@app.cli.command()
def check_alarm():
    now = datetime.datetime.now()

    alarm = query_db('SELECT * FROM alarms WHERE hours=? AND minutes=?', (now.hour, now.minute), True)

    if alarm is None:
        return
    else:
        subscribe.callback(on_play_finished, "hermes/audioServer/default/playFinished", hostname="mosquitto")
        alarm_play(alarm)
