import paho.mqtt.client as mqtt
import os
import logging
import time

mqtt_host = os.getenv('MQTT_HOST', 'raspberrypi')
mqtt_port = os.getenv('MQTT_PORT', 1883)
mqtt_username = os.getenv('MQTT_USERNAME', None)
mqtt_password = os.getenv('MQTT_PASSWORD', None)

client = mqtt.Client()

logger = logging.getLogger('mqtt')



def on_connect(client, userdata, flags, rc):
    logger.info("Connected to MQTT Broker (result_code=%s)", str(rc))


def connect():
    if mqtt_host and mqtt_port:
        if mqtt_username is not None:
            client.username_pw_set(mqtt_username, mqtt_password)
        client.connect(mqtt_host, mqtt_port)
    client.on_connect = on_connect

    return client