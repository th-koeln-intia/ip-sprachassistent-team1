import paho.mqtt.client as mqtt
import os
import logging
import time

MQTT_HOST = os.getenv('MQTT_HOST', 'raspberrypi')
MQTT_PORT = os.getenv('MQTT_PORT', 1883)
MQTT_USERNAME = os.getenv('MQTT_USERNAME', None)
MQTT_PASSWORD = os.getenv('MQTT_PASSWORD', None) 