from .mqtt import mqtt
from .wake_word import wake_word
from .asr import asr
import logging
import coloredlogs


def setup_logger():
    logger = logging.getLogger('showcase')
    coloredlogs.install(level='DEBUG')


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
