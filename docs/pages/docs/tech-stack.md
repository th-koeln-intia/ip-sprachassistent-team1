---
title: Tech-Stack
permalink: /docs/tech-stack/
subtitle: Welche Technik steckt hinter Deep Thoguht?
layout: page
show_sidebar: false
menubar: docs_menu
---

# Hardware

Zur Entwicklung wurde folgende Hardware benutzt, die hier als Referenz dient:

| Typ                 | Modell                                  |
| ------------------- | --------------------------------------- |
| Einplatinencomputer | Raspberry Pi 3 B+                       |
| Mikrofon            | ReSpeaker 4-Mic Array                   |
| ZigBee USB-Stick    | CC2531                                  |
| ZigBee Lampe        | Philips Hue white and color (929001573) |
| Lautsprecher        | Logitech Z120                           |


# Tooling

## Rhasspy

[Rhasspy](https://rhasspy.readthedocs.io/) ist ein Open Source Dienst, welcher es ermöglicht einen eigenen 
Sprachassistenten zu entwickeln. Der Service liefert einige Dienste von Haus aus mit. 
Die verwendeten Dienste sind hier im Folgenden aufgelistet und erläutert

### Rhasspy Raven

[Rhasspy Raven](https://github.com/rhasspy/rhasspy-wake-raven-hermes/) ist ein Dienst zur Erkennung des Wake-Words. 
Ein Wake-Word ist das Wort, welches den Sprachassistenten "weckt" und signalisiert, dass die folgenden gesprochenen 
Wörter interpretiert werden sollen.
Raven benötigt ein Training um das Wake-Word zu erkennen - hierzu werden drei Audiodateien händisch aufgenommen und
gespeichert. 
Raven bietet auch die Möglichkeit einige Parameter wie Sensitivität und die Anzahl der übereinstimmenden 
Trainingsdateien zu definieren. 

Es lassen sich auch unterschiedliche Wake-Words erstellen.

### Pocketsphinx

[Pocketsphinx](https://github.com/rhasspy/rhasspy-asr-pocketsphinx-hermes) ist der Dienst, der unsere gesprochene 
Sprache transkribiert. Die Umwandlung erfolgt dabei komplett offline. Pocketsphinx bietet auch einige Parameter zur 
Feinabstimmung - insbesondere den Start- und Stopp-Zeitpunkt des Transkribierens.
Das Wörterbuch sowie die entsprechende Aussprache lässt sich hier über Textdateien definieren und ergänzen.

Die Entwicklungsdokumentation dazu findet sich [hier](/results/speech-to-text).

### Fsticuffs

[Fsticuffs](https://github.com/rhasspy/rhasspy-nlu-hermes) wird verwendet um Sätze bzw. Befehle zu erkennen, die 
gesprochen werden. Alle möglichen Befehle müssen definiert werden. Nach eigener Aussage ist Fsticuffs dafür extrem 
performant.

Die Entwicklungsdokumentation dazu findet sich [hier](/results/intent-recognition).

### Espeak

[Espeak](http://espeak.sourceforge.net/) ([Rhasspy GitHub](https://github.com/rhasspy/rhasspy-tts-cli-hermes)) ist ein 
Text-To-Speech Dienst. Er bietet Stimmunterstützung für verschiedene Sprachen.

Die Entwicklungsdokumentation dazu findet sich [hier](/results/text-to-speech).

### Rhasspy (Dialogue Management)

Der hauseigene [Rhasspy Dialogue Manager](https://github.com/rhasspy/rhasspy-dialogue-hermes) kümmert sich um die 
Sitzungsverwaltung. Dieser Service stellt einen Vermittler dar, der die anderen Services benachrichtigt, sobald diese 
mit ihrer Arbeit beginnen sollen. 

## MQTT
Bei dem Message Queuing Telemetry Transport (MQTT) handelt es sich um ein Client-Server-Netzwerkprotokoll. Es eignet 
sich besonders gut für Machine-To-Machine Kommunikation und ist deshalb im IoT-Bereich weit vertreten.

Dabei gibt es einen sogenannten MQTT-Broker, der hier den Server darstellt. Clients senden Nachrichten an den Broker in 
ein bestimmtes Topic. Topics stellen hier eine hierarchische Ordnung dar und sind nicht fest definiert. Ein Mögliches 
Topic wäre zum Beispiel `/Wohnzimmer/Rauchmelder/Rauchsensor` - hier würde beispielsweise der Rauchsensor des 
Rauchmelders die aktuellen Sensordaten schreiben (`PUBLISH`).
Wenn man jetzt einen möglichen Rauchmelder im Schlafzimmer koppeln möchte, kann dieser das Topic 
abbonieren (`SUBSCRIBE`). Der Broker wird dann die aktuellen Sensordaten weiterleiten.

MQTT definiert drei unterschiedliche Qualitiy of Service (QoS) - **most once** (Einmaliges Senden), 
**at least once** (Mehrfaches Senden bis Empfang bestätigt wird) und 
**exactly once** (Mehrfaches Senden, exakt einmaliger Empfang).

Zusätzlich kann eine Retain-Flag gesetzt werden, die dem Broker mitteilt die Nachrichten zwischenzuspeichern auch wenn 
es keinen Subscriber des Topics gibt.

Das Protokoll wird von der OASIS verwaltet und weiterentwickelt. 

Weitere Informationen: [https://mqtt.org/](https://mqtt.org/)

### Mosquitto

[Mosquitto](https://mosquitto.org/) ist eine Open Source implementierung des MQTT Brokers, der von der 
[Eclipse Foundation](https://www.eclipse.org/) entwickelt wird.

### MQTT Explorer

Der [MQTT Explorer](http://mqtt-explorer.com/) eignet sich hervorragend dafür seinen MQTT-Broker zu debuggen. Er bietet 
eine Übersicht über die MQTT Topics und ermöglicht es, eigene Nachrichten zu versenden.

## Zigbee2MQTT

[Zigbee2MQTT](https://www.zigbee2mqtt.io/) ist ein Service, der es ermöglicht smarte Geräte, die auf der [Zigbee Spezifikation](https://zigbeealliance.org/) basieren über MQTT Nachrichten zu verwenden. 

Wir verwenden den Service um eine (oder mehrere) Lampe über den Sprachassistenten anzusteuern. Der Entwicklungsprozess ist [hier](/docs/features/light) beschrieben.

## Node-Red

[Node-Red](https://nodered.org/) ist eine visuelle Programmierumgebung, die es ermöglicht Abläufe zu definieren. 

## Docker

Um die implementierten Anwendungen isoliert laufen zu lassen, verwenden wir [Docker](https://www.docker.com/).
Wie man Deep Thought mit Docker startet ist [hier](/getting-started/installation) beschrieben.

### Docker Image `hermes-led`

Das Docker Image `hermes-led` stellt eine Schnittstelle zwischen ReSpeaker Treiber zu MQTT dar. Es ist für ARM-Geräte 
auf [Docker Hub](https://hub.docker.com/r/thund/hermes-led) zu finden.

Damit das Image verwendet werden kann, müssen dem Container einige Geräte übergeben werden, das ganze geschiet über die 
entsprechenden Dateideskriptoren `/dev/gpiomem`, `/dev/mem`, `/dev/spidevv0.0` und `/dev/spidev0.1`. 

Der Container startet `HermesLedControl` und kann über die Umgebungsvariable `HLC_ARGUMENTS` parametisiert werden. Die 
zur Verfügung stehenden Parameter finden sich 
[hier](https://github.com/project-alice-assistant/HermesLedControl/wiki/Arguments-customization).
Eine Beispielkonfiguration, wie sie in Deep Thought verwendet wird sieht folgendermaßen aus. Wir verwenden hier das 
ReSpeaker 4-Mic-Array, übergeben unsere Rhasspy-Konfiguration und unseren den MQTT-Broker.

```yml
hermes-led:
    container_name: hermes-led
    image: thund/hermes-led:0.0.1
    volumes:
        - ./rhasspy/profiles/de:/tmp/rhasspy
    environment:
        - TZ=Europe/Berlin
        - HLC_ARGUMENTS=--hardware=respeaker4 --pathToConfig=/tmp/rhasspy/profile.json --engine=rhasspy --mqttServer=mosquitto
    devices:
        - /dev/gpiomem:/dev/gpiomem
        - /dev/mem:/dev/mem
        - /dev/spidev0.0:/dev/spidev0.0
        - /dev/spidev0.1:/dev/spidev0.1
    restart: unless-stopped
    privileged: true
```

## Jekyll

Die Dokumentation wird mit Jekyll generiert. Hierzu kann man ebenfalls einen Docker-Container verwenden, anstatt Jekyll 
lokal zu installieren.

Lokale Testversion hosten:

```sh
export JEKYLL_VERSION=3.8
cd ./docs
docker run --rm -p 4000:4000 --volume="/$(PWD):/srv/jekyll" -it jekyll/jekyll:$JEKYLL_VERSION  jekyll serve --force-polling
```

Die Dokumentation ist anschließend unter [http://localhost:4000](http://localhost:4000) aufrufbar.

## Flask

Die API welche die Logik der Intents steuert wird mit dem Python-Framework [Flask](https://flask.palletsprojects.com/en/1.1.x/) umgesetzt. Wir haben bei der Implementierung der API drauf geachtet die einzelnen Features (Lichtsteuerung, Wecker, etc.) in einzelne Module zu schreiben.


# Entwicklungswerkzeuge

## Visual Studio Code

Die einfachste Möglichkeit um direkt auf dem Raspberry Pi zu entwickeln gibt es mit [Visual Studio Code](https://code.visualstudio.com/) in Kombination mit den Folgenden Addons um Medienbrüche zu vermeiden:

### Remote - SSH
[Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) bietet eine einfache Möglichkeit über Visual Studio Code direkt auf den Raspberry Pi zuzugreifen. So kann man auf das Dateisystem und auf die Kommandozeile zugreifen.

### Remote - Containers mit Docker
Mit [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) und [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) ist es möglich die Docker-Umgebung, die sich auf dem Raspberry Pi befindet direkt in Visual Studio zu verwalten.

### Python
Sollte man am Python-Code arbeiten wollen, ist das [Python Addon](https://marketplace.visualstudio.com/items?itemName=ms-python.python) ein nützlicher Helfer.

