from api.app import app
from api import MQTT_HOST, MQTT_PORT
from flask import request, Response, jsonify
import json
import paho.mqtt.publish as publish


@app.route('/light/<string:friendly_name>/set', methods=['POST'])
def set_light_with_friendly_name(friendly_name):
    body = request.get_json()
    if body is None:
        return jsonify({"error": "BAD_REQUEST"}), 400
    else:
        publish.single('zigbee2mqtt/' + friendly_name + '/set', json.dumps(body), hostname=MQTT_HOST, port=MQTT_PORT)
        return jsonify(body), 200

@app.route('/light/set', methods=['POST'])
def set_light():
    body = request.get_json()
    if body is None or 'friendly_name' not in body or 'payload' not in body:
        return jsonify({"error": "BAD_REQUEST"}), 400
    else:
        publish.single('zigbee2mqtt/' + body['friendly_name'] + '/set', json.dumps(body['payload']), hostname=MQTT_HOST, port=MQTT_PORT)
        return jsonify(body), 200

