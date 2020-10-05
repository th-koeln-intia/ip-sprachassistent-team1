---
title: Tech-Stack
permalink: /docs/tech-stack/
subtitle: Tech-Stack
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

Beim ersten Start wird ein Download eines von vortrainierten akustischen Modells sowie Wörterbuch benötigt.
Es handelt sich dabei um die [CMU Sphinx](https://sourceforge.net/projects/cmusphinx/) Datenbank.
Ein eigenes Training ist hier erstmal nicht sinnvoll was aus der 
[Dokumentation](https://cmusphinx.github.io/wiki/tutorialam/) auch hervorgeht, denn wir haben weder genügend Zeit noch 
genug Daten dafür.

Das Speech-To-Text-System ist hierbei auf dem Raspberry Pi ziemlich langsam - es ist allerdings möglich die Aufgabe auf
ein leistungsstärkeres System zu übertragen. Besonders beim Language Model Mixing (siehe nächsten Abschnitt) ist die Hardware des Rhaspberry zu schwach und es wird ausdrücklich empfohlen die Berechnung über einen Server laufen zu lassen.

Es geht nicht aus der Dokumentation hervor, allerdings müssen für Pocketsphinx die Intents (`sentences.ini`) gepflegt 
sein, weil aus dieser ein Sprachmodell erstellt wird. Das bedeutet es können noch so viele Wörter im Wörterbuch stehen, 
Pocketsphinx erkennt standardmäßig nur die Satzbestandteile, die auch in der `sentences.ini` stehen, selbst wenn auf der 
remote-Instanz bloß der Speech-To-Text Dienst läuft. Dieses Verhalten kann man abändern, indem man den Wert `mix_weight` bei PocketSphinx erhöht.
Je höher dieser Wert ist, desto mehr wird die `sentences.ini` mit dem language Model von PocketSphinx vermischt und es werden auch Wörter erkannt, die nicht in der `sentences.ini` eingetragen wurden. Aufgrund der Größe des mitgelieferten Language Models nimmt die Spracherkennung mit einem mix_weight > 0 sehr viel mehr Rechenkapazität in Anspruch.

Wir sehen folgende Konfigurationsbasis vor:

```json
//TODO Konfiguration hinzufügen, das hier ist nur ein Beispiel
"command": {
    "webrtcvad": {
      "skip_sec": 0,
      "min_sec": 1,
      "speech_sec": 0.3,
      "silence_sec": 0.5,
      "before_sec": 0.5,
      "vad_mode": 3
    }
  }
```  

### Fsticuffs

[Fsticuffs](https://github.com/rhasspy/rhasspy-nlu-hermes) wird verwendet um Sätze bzw. Befehle zu erkennen, die 
gesprochen werden. Alle möglichen Befehle müssen definiert werden. Nach eigener Aussage ist Fsticuffs dafür extrem 
performant.

### Espeak

[Espeak](http://espeak.sourceforge.net/) ([Rhasspy GitHub](https://github.com/rhasspy/rhasspy-tts-cli-hermes)) ist ein 
Text-To-Speech Dienst. Er bietet Stimmunterstützung für verschiedene Sprachen.

### Rhasspy (Dialogue Management)

Der hauseigene [Rhasspy Dialogue Manager](https://github.com/rhasspy/rhasspy-dialogue-hermes) kümmert sich um die 
Sitzungsverwaltung. Dieser Service stellt einen Vermittler dar, der die anderen Services benachrichtigt, sobald diese 
mit ihrer Arbeit beginnen sollen. 

//TODO bisschen ausführlicher, evtl. mit Beispiel

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

```export JEKYLL_VERSION=3.8```

```cd ./docs```

```docker run --rm -p 4000:4000 --volume="/$(PWD):/srv/jekyll" -it jekyll/jekyll:$JEKYLL_VERSION  jekyll serve```

Die Dokumentation ist anschließend unter [http://localhost:4000](http://localhost:4000) aufrufbar.


