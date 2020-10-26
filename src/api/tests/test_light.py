import json
import os
from api.app import app
from api.light import create_payload_from_rhasspy_intent, get_friendly_name_from_rhasspy_intent, publish_set
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
        },
        'feedback': {
            'text': 'Okay, ich schalte Licht im Wohnzimmer an'
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


# A valid request should return the provided request body as confirmation
def test_light_endpoint_response_data(mocker):
    mocker.patch('paho.mqtt.publish.single') # Prevent from publishing a real message


    response = app.test_client().post('/light/set', json={
        'friendly_name': 'living_room',
        'payload': {
            'state': 'ON',
            'brightness': 255,
            'color': '#0000ff'
        },
        'feedback': {
            'text': 'Okay, ich schalte Licht im Wohnzimmer an'
        }
    })
    assert ordered(json.loads(response.data)) == ordered(json.loads("""{
        "friendly_name": "living_room",
        "payload": {
            "state": "ON",
            "brightness": 255,
            "color": "#0000ff"
        },
        "feedback": {
            "text": "Okay, ich schalte Licht im Wohnzimmer an"
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
        },
        'feedback': {
            'text': 'Okay, ich schalte Licht im Wohnzimmer an'
        }
    })

    expected_payload = {
            'brightness': 255,
            'color': '#0000ff',
            'state': 'ON'
        }

    expected_feedback_payload = {
        'text': 'Okay, ich schalte Licht im Wohnzimmer an'
    }

    paho.mqtt.publish.single.assert_has_calls([mocker.call('zigbee2mqtt/living_room/set', json.dumps(expected_payload), hostname=mocker.ANY, port=mocker.ANY), mocker.call('hermes/tts/say', json.dumps(expected_feedback_payload), hostname=mocker.ANY, port=mocker.ANY)]) # pylint: disable=no-member



def load_rhasspy_intent_json():
    script_dir = os.path.dirname(__file__)
    rel = 'resources/rhasspy_intent.json'
    abs_path = os.path.join(script_dir, rel)
    return open(abs_path, 'r').read()


# Test whether a rhasspy intent JSON would create a valid MQTT Payload
def test_create_payload_from_rhasspy_intent():
    given_json = load_rhasspy_intent_json()
    given_dict = json.loads(given_json)
    payload = create_payload_from_rhasspy_intent(given_dict)
    
    expected_json = """{
        "state": "on",
        "color": "#ffffff",
        "brightness": 255
    }"""
    expected_payload = json.loads(expected_json)

    assert ordered(payload) == ordered(expected_payload)


# Test whether the friendly_name can be correctly parsed from a rhasspy intent JSON
def test_get_friendly_name_from_rhasspy_intent():
    given_json = load_rhasspy_intent_json()
    given_dict = json.loads(given_json)

    friendly_name = get_friendly_name_from_rhasspy_intent(given_dict)

    assert friendly_name == 'living_room'


def test_raw_endpoint_status_ok(mocker):
    mocker.patch('paho.mqtt.publish.single') #Prevent from publishing a real message

    given_json = load_rhasspy_intent_json()

    response = app.test_client().post('/light/set/raw', json=json.loads(given_json))
    assert response.status_code == 200


def test_raw_endpoint_status_bad_request(mocker):
    response = app.test_client().post('/light/set/raw')
    assert response.status_code == 400


def test_raw_endpoint_mqtt_params(mocker):
    mocker.patch('paho.mqtt.publish.single') 

    given_json = load_rhasspy_intent_json()
    given_dict = json.loads(given_json)

    app.test_client().post('/light/set/raw', json=given_dict)

    expected_payload = {
            'state': 'on',
            'brightness': 255,
            'color': '#ffffff'
        }

    expected_feedback_payload = {
        'text': 'Okay, schalte licht im wohnzimmer an'
    }

    paho.mqtt.publish.single.assert_has_calls([mocker.call('zigbee2mqtt/living_room/set', json.dumps(expected_payload), hostname=mocker.ANY, port=mocker.ANY), mocker.call('hermes/tts/say', json.dumps(expected_feedback_payload), hostname=mocker.ANY, port=mocker.ANY)]) # pylint: disable=no-member
