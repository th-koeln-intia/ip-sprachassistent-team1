import json
from api.light import Zigbee2MqttSet, Zigbee2MqttSetEncoder, Payload, zigbee2MqttSetDecoder, PayloadEncoder
from api.app import app
import paho.mqtt.publish

# Test wheter the mapping classes can be successfully instantiated 
def test_new_Zigbee2MqttSet():
    zigbee2MqttSet = Zigbee2MqttSet(friendly_name='living_room', payload=Payload(state='ON', brightness=255, color='#ffffff'))
    assert zigbee2MqttSet.friendly_name == 'living_room'
    assert zigbee2MqttSet.topic == 'zigbee2mqtt/living_room/set'
    assert zigbee2MqttSet.payload.state == 'ON'
    assert zigbee2MqttSet.payload.brightness == 255
    assert zigbee2MqttSet.payload.color == '#ffffff'

# Test the JSON encoding and decoding
def test_json_encoding_decoding_Zigbee2MqttSet():
    zigbee2MqttSet = Zigbee2MqttSet(friendly_name='living_room', payload=Payload(state='ON', brightness=255, color='#ffffff'))
    zigbee2MqttSet_string = json.dumps(zigbee2MqttSet, cls=Zigbee2MqttSetEncoder)
    zigbee2MqttSet_dict = json.loads(zigbee2MqttSet_string)
    zigbee2MqttSet_decoded = zigbee2MqttSetDecoder(zigbee2MqttSet_dict)
    assert zigbee2MqttSet == zigbee2MqttSet_decoded 

# A valid request should return HTTP status OK
def test_light_endpoint_status_ok(mocker):
    mocker.patch('paho.mqtt.publish.single') #Prevent from publishing a real message

    response = app.test_client().post('/light/set', json={
        'friendly_name': 'living_room',
        'payload': {
            'state': 'ON',
            'brightness': 255,
            'color': '#0000ff'
        }
    })
    assert response.status_code == 200

# An invalid request should return HTTP status BAD REQUEST
def test_light_endpoint_status_bad_request():
    response = app.test_client().post('/light/set')
    assert response.status_code == 400

# A valid request should return ???? TODO 
def test_light_endpoint_response_data(mocker):
    mocker.patch('paho.mqtt.publish.single') # Prevent from publishing a real message


    response = app.test_client().post('/light/set', json={
        'friendly_name': 'living_room',
        'payload': {
            'state': 'ON',
            'brightness': 255,
            'color': '#0000ff'
        }
    })
    assert json.loads(response.data) == json.loads("""{
        "friendly_name": "living_room",
        "topic": "zigbee2mqtt/living_room/set",
        "payload": {
            "state": "ON",
            "brightness": 255,
            "color": "#0000ff"
        }
    }""")

# A valid request should publish a MQTT message
def test_light_endpoint_mqtt_params(mocker):
    mocker.patch('paho.mqtt.publish.single') 

    app.test_client().post('/light/set', json={
        'friendly_name': 'living_room',
        'payload': {
            'state': 'ON',
            'brightness': 255,
            'color': '#0000ff'
        }
    })

    expected_payload = Payload(state='ON', brightness=255, color='#0000ff')

    paho.mqtt.publish.single.assert_called_once_with('zigbee2mqtt/living_room/set', json.dumps(expected_payload, cls=PayloadEncoder), hostname=mocker.ANY, port=mocker.ANY) # pylint: disable=no-member
