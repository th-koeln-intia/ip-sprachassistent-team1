from api.app import app
from api import MQTT_HOST, MQTT_PORT
from flask import request, Response, jsonify
import json 
import paho.mqtt.publish as publish
import jsonpickle
from types import SimpleNamespace as Namespace
from json import JSONDecoder, JSONEncoder

class Payload(object):
    def __init__(self, state=None, brightness=None, color=None, **kwargs):
        self.state = state
        self.brightness = brightness
        self.color = color

class PayloadEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Zigbee2MqttSet(object):
    def __init__(self, friendly_name, topic=None, payload=None, **kwargs):
        self.friendly_name = friendly_name
        self.topic = 'zigbee2mqtt/' + friendly_name + '/set' if topic is None else topic
        self.payload = payload

class Zigbee2MqttSetEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


@app.route('/light/set', methods=['POST'])
def set_light():
    body = request.get_json()
    if body is None or 'friendly_name' not in body:
        return jsonify({"error": "BAD_REQUEST"}), 400
    else:
        zigbeeSet = Zigbee2MqttSet(**body)
        publish.single(zigbeeSet.topic, json.dumps(zigbeeSet.payload, cls=PayloadEncoder), hostname=MQTT_HOST, port=MQTT_PORT)
        return json.dumps(zigbeeSet, cls=Zigbee2MqttSetEncoder), 200

