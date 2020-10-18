from flask import jsonify, request
from app import app, get_db, query_db
import time
import paho.mqtt.publish as publish

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

@app.route('/alarm/test')
def alarm_test():
    return publish.single("hermes/tts/say", {'text': 'Okay, ich Schalte das'}, hostname="mosquitto")

@app.cli.command()
def check_alarm():
    """Check alarms."""
    print('Importing feeds...')
    time.sleep(5)
    print('Done!')