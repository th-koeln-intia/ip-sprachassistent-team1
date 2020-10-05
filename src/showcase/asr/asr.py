import json
import logging

logger = logging.getLogger('pocketsphinx_asr')


def on_asr_activation(client, userdata, msg):
    logger.info("ASR service activated")


def on_asr_deactivation(client, userdata, msg):
    logger.info("ASR service deactivated")


def on_asr_start_listen(client, userdata, msg):
    payload = json.loads(msg.payload)
    logger.info("ASR service starts listening (session=%s)", payload['sessionId'])
    logger.debug("Payload (%s): %s", msg.topic, payload)


def on_asr_stop_listen(client, userdata, msg):
    payload = json.loads(msg.payload)
    logger.info("ASR service stops listening (session=%s)", payload['sessionId'])
    logger.debug("Payload (%s): %s", msg.topic, payload)


def on_asr_text_captured(client, userdata, msg):
    payload = json.loads(msg.payload)
    logger.info("ASR service starts listening (session=%s, text=%s)", payload['sessionId'], payload['text'])
    logger.debug("Payload (%s): %s", msg.topic, payload)