import json


def on_asr_activation(client, userdata, msg):
    print("Activate ASR component")


def on_asr_deactivation(client, userdata, msg):
    print("Deactivate ASR component")


def on_asr_start_listen(client, userdata, msg):
    payload = json.loads(msg.payload)
    print("Start ASR listening:")
    print("\tSession: " + payload['sessionId'])


def on_asr_stop_listen(client, userdata, msg):
    payload = json.loads(msg.payload)
    print("Stop ASR listening:")
    print("\tSession: " + payload['sessionId'])


def on_asr_text_captured(client, userdata, msg):
    payload = json.loads(msg.payload)
    print("Captured Text: " + payload['text'])
    print("\tSession: " + payload['sessionId'])