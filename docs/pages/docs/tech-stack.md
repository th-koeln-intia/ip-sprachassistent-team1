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

[Rhasspy](https://rhasspy.readthedocs.io/) ist ein Open Source Dienst, welcher es ermöglicht einen eigenen Sprachassistenten zu entwickeln. Der Service liefert einige Dienste von Haus aus mit. Die verwendeten sind hier im Folgenden aufgelistet und erläutert

### Rhasspy Raven

[Rhasspy Raven](https://github.com/rhasspy/rhasspy-wake-raven-hermes/) ist ein Dienst zur Erkennung des Wake-Words. Ein Wake-Word ist das Wort, welches den Sprachassistenten "weckt" und signalisiert, dass das folgende gesprochene interpretiert werden soll.
Raven benötigt ein Training um das Wake-Word zu erkennen - hierzu werden drei Audiodateien händisch aufgenommen und gespeichert. Raven bietet auch die Möglichkeit einige Parameter wie Sensitivität und die Anzahl der übereinstimmenden Trainingsdateien zu definieren.
Es lassen sich auch unterschiedliche Wake-Words erstellen.

### Pocketsphinx

[Pocketsphinx](https://github.com/rhasspy/rhasspy-asr-pocketsphinx-hermes) ist der Dienst, der unsere gesprochene Sprache transkribiert. Die Umwandlung erfolgt dabei komplett offline. Pocketsphinx bietet auch einige Parameter zur Feinabstimmung - insbesondere den Start- und Stopp-Zeitpunkt des Transkribierens.
Das Wörterbuch sowie die entsprechende Aussprache lässt sich hier über Textdateien definieren und ergänzen.

Beim ersten Start ist ein Download notwendig. 

### Fsticuffs

[Fsticuffs](https://github.com/rhasspy/rhasspy-nlu-hermes) wird verwendet um Sätze bzw. Befehle zu erkennen, die gesprochen werden. Alle möglichen Befehle müssen definiert werden. Nach eigener Aussage ist Fsticuffs dafür extrem performant.

### Espeak

[Espeak](http://espeak.sourceforge.net/) ([Rhasspy GitHub](https://github.com/rhasspy/rhasspy-tts-cli-hermes)) ist ein Text-To-Speech Dienst. Er bietet Stimmunterstützung für verschiedene Sprachen.

### Rhasspy (Dialogue Management)

Der hauseigene [Rhasspy Dialogue Manager](https://github.com/rhasspy/rhasspy-dialogue-hermes) kümmert sich um die Sitzungsverwaltung. Dieser Service stellt einen Vermittler dar, der die anderen Services benachrichtigt, sobald diese mit ihrer Arbeit beginnen sollen. 

//TODO bisschen ausführlicher, evtl. mit Beispiel

## MQTT
Bei dem Message Queuing Telemetry Transport (MQTT) handelt es sich um ein Client-Server-Netzwerkprotokoll. Es eignet sich besonders gut für Machine-To-Machine Kommunikation und ist deshalb im IoT-Bereich weit vertreten.

Dabei gibt es einen sogenannten MQTT-Broker, der hier den Server darstellt. Clients senden Nachrichten an den Broker in ein bestimmtes Topic. Topics stellen hier eine hierarchische Ordnung dar und sind nicht fest definiert. Ein Mögliches Topic wäre zum Beispiel `/Wohnzimmer/Rauchmelder/Rauchsensor` - hier würde beispielsweise der Rauchsensor des Rauchmelders die aktuellen Sensordaten schreiben (`PUBLISH`).
Wenn man jetzt einen möglichen Rauchmelder im Schlafzimmer koppeln möchte, kann dieser das Topic abbonieren (`SUBSCRIBE`). Der Broker wird dann die aktuellen Sensordaten weiterleiten.

MQTT definiert drei unterschiedliche Qualitiy of Service (QoS) - **most once** (Einmaliges Senden), **at least once** (Mehrfaches Senden bis Empfang bestätigt wird) und **exactly once** (Mehrfaches Senden, exakt einmaliger Empfang).

Zusätzlich kann eine Retain-Flag gesetzt werden, die dem Broker mitteilt die Nachrichten zwischenzuspeichern auch wenn es keinen Subscriber des Topics gibt.

Das Protokoll wird von der OASIS verwaltet und weiterentwickelt. 

Weitere Informationen: [https://mqtt.org/](https://mqtt.org/)

### Mosquitto

[Mosquitto](https://mosquitto.org/) ist eine Open Source implementierung des MQTT Brokers, der von der [Eclipse Foundation](https://www.eclipse.org/) entwickelt wird.

## Docker

Um die implementierten Anwendungen isoliert laufen zu lassen, verwenden wir [Docker](https://www.docker.com/).
Wie man das Projekt (//TODO Projektname) mit Docker startet ist [hier](/getting-started/installation) (//TODO Anchor) beschrieben.