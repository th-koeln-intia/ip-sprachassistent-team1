from api.app import app
from api import MQTT_HOST, MQTT_PORT
from flask import request, Response, jsonify
import json 
import paho.mqtt.publish as publish
from json import JSONDecoder, JSONEncoder

class Payload(object):
    def __init__(self, state=None, brightness=None, color=None):
        self.state = state
        self.brightness = brightness
        self.color = color
    def __eq__(self, other):
        return self.state == other.state and self.brightness == other.brightness and self.color == other.color

class PayloadEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Zigbee2MqttSet(object):
    def __init__(self, friendly_name, topic=None, payload=None):
        self.friendly_name = friendly_name
        self.topic = 'zigbee2mqtt/' + friendly_name + '/set' if topic is None else topic
        self.payload = payload
    def __eq__(self, other):
        return self.friendly_name == other.friendly_name and self.topic == other.topic and self.payload == other.payload

class Zigbee2MqttSetEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

def zigbee2MqttSetDecoder(dct):
    friendly_name = dct.get("friendly_name")
    topic = dct.get("topic", None)
    payload = dct.get("payload", None)
    state = payload.get("state", None) if payload is not None else None
    brightness = payload.get("brightness", None) if payload is not None else None
    color = payload.get("color", None) if payload is not None else None
    payload = Payload(state=state, brightness=brightness, color=color) if payload is not None else None
    return Zigbee2MqttSet(friendly_name=friendly_name, topic=topic, payload=payload)
    
@app.route('/light/set', methods=['POST'])
def set_light():
    body = request.get_json()
    if body is None or 'friendly_name' not in body:
        return jsonify({"error": "BAD_REQUEST"}), 400
    else:
        zigbeeSet = zigbee2MqttSetDecoder(body)
        publish.single(zigbeeSet.topic, json.dumps(zigbeeSet.payload, cls=PayloadEncoder), hostname=MQTT_HOST, port=MQTT_PORT)
        return json.dumps(zigbeeSet, cls=Zigbee2MqttSetEncoder), 200

