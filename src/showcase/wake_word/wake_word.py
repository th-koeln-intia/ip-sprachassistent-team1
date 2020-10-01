import json


def on_wakeword_detection(client, userdata, msg):
    payload = json.loads(msg.payload)
    print("Detected Wake Word:")
    print("\tMatches Recording: " + payload['modelId'])
    print("\tDetected On: " + msg.topic)


def on_wakeword_activation(client, userdata, msg):
    print("Wake Word Activation")


def on_wakeword_deactivation(client, userdata, msg):
    print("Wake Word Deactivation")