import json
from api.app import app
import paho.mqtt.publish

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

# Sort a dictionary
def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj

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
    assert ordered(json.loads(response.data)) == ordered(json.loads("""{
        "friendly_name": "living_room",
        "payload": {
            "state": "ON",
            "brightness": 255,
            "color": "#0000ff"
        }
    }"""))

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

    expected_payload = {
            'brightness': 255,
            'color': '#0000ff',
            'state': 'ON'
        }

    paho.mqtt.publish.single.assert_called_once_with('zigbee2mqtt/living_room/set', json.dumps(expected_payload), hostname=mocker.ANY, port=mocker.ANY) # pylint: disable=no-member
