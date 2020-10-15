from api.app import app
from api import MQTT_HOST, MQTT_PORT
from flask import request, Response, jsonify
import json 
import paho.mqtt.publish as publish
from json import JSONDecoder, JSONEncoder

   
@app.route('/light/set', methods=['POST'])
def set_light():
    body = request.get_json()
    if body is None or 'friendly_name' not in body or 'payload' not in body:
        return jsonify({"error": "BAD_REQUEST"}), 400
    else:
        topic = 'zigbee2mqtt/' + body['friendly_name'] + '/set'
        publish.single(topic, json.dumps(body['payload']), hostname=MQTT_HOST, port=MQTT_PORT)
        return json.dumps(body), 200

