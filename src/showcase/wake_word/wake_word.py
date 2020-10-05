import json
import logging

logger = logging.getLogger('__name__')


def on_wakeword_detection(client, userdata, msg):
    payload = json.loads(msg.payload)
    logger.info("Detected Wake Word: (recording=%s)", payload['modelId'])
    logger.debug("Payload (%s): %s", msg.topic, payload)


def on_wakeword_activation(client, userdata, msg):
    logger.info("Wake Word service activated")


def on_wakeword_deactivation(client, userdata, msg):
    logger.info("Wake Word service deactivated")

