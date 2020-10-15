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
        publish_set(body['friendly_name'], json.dumps(body['payload']))
        return json.dumps(body), 200


@app.route('/light/set/raw', methods=['POST'])
def set_light_raw():
    body = request.get_json()
    if body is None:
        return jsonify({"error": "BAD_REQUEST"}), 400
    friendly_name = get_friendly_name_from_rhasspy_intent(body)
    payload = create_payload_from_rhasspy_intent(body)
    publish_set(friendly_name, json.dumps(payload))
    return json.dumps(body), 200


def create_payload_from_rhasspy_intent(dict):
    entities = dict.get('entities', None)
    if entities is None:
        return None
    state = next((x for x in entities if x['entity'] == 'state'), None)
    brightness = next((x for x in entities if x['entity'] == 'brightness'), None)
    color = next((x for x in entities if x['entity'] == 'color'), None)
    payload = {}
    if state is not None and 'value' in state:
        payload['state'] = state['value']
    if brightness is not None and 'value' in brightness:
        payload['brightness'] = brightness['value']
    if color is not None and 'value' in color:
        payload['color'] = color['value']
    return payload


def get_friendly_name_from_rhasspy_intent(dict):
    entities = dict.get('entities', None)
    if entities is None:
        return None
    room = next((e for e in entities if e['entity'] == 'room'), None)
    return room.get('value', None)


def publish_set(friendly_name, payload):
    topic = 'zigbee2mqtt/' + friendly_name + '/set'
    publish.single(topic, payload, hostname=MQTT_HOST, port=MQTT_PORT)