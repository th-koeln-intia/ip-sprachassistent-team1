from .mqtt import mqtt
from .wake_word import wake_word
from .asr import asr
import logging


def setup_logger():
    logger = logging.getLogger('__name__')
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter(fmt='[%(levelname)s]\t %(asctime)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    ch.setFormatter(formatter)

    logger.addHandler(ch)


def setup():
    client = mqtt.connect()

    mqtt.subscribe_and_add_callback("hermes/hotword/toggleOn", wake_word.on_wakeword_activation)
    mqtt.subscribe_and_add_callback("hermes/hotword/toggleOff", wake_word.on_wakeword_deactivation)
    mqtt.subscribe_and_add_callback("hermes/hotword/+/detected", wake_word.on_wakeword_detection)
    mqtt.subscribe_and_add_callback("hermes/asr/toggleOn", asr.on_asr_activation)
    mqtt.subscribe_and_add_callback("hermes/asr/toggleOff", asr.on_asr_deactivation)
    mqtt.subscribe_and_add_callback("hermes/asr/startListening", asr.on_asr_start_listen)
    mqtt.subscribe_and_add_callback("hermes/asr/stopListening", asr.on_asr_stop_listen)
    mqtt.subscribe_and_add_callback("hermes/asr/textCaptured", asr.on_asr_text_captured)

    client.loop_forever()


setup_logger()
setup()
