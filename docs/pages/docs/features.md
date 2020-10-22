---
title: Features
permalink: /docs/features/
subtitle: Features
layout: page
show_sidebar: false
menubar: docs_menu
---

# 🎙 Wake Word

Wir haben uns für das Wake Word "Hey Trixie entschieden".
//TODO

# 🔊 Hintergrungeräuschreduzierung

Wir haben eine Hintergrundgeräuschreduzierung implementiert.
//TODO

# 💡 Lichtsteuerung

### Erweiterung der Gruppen

Sollten weitere Gruppen über den Sprachassistenten angesteuert werden sollen und diese bereits nach [Konfigurieren der Gruppen](#konfigurieren-der-gruppen) definiert worden sein, dann muss für Rhasspy die Datei `profiles/de/slots/light_rooms` angepasst werden. Das Format hier richtet sich nach der [Dokumentation von Rhasspy](https://rhasspy.readthedocs.io/en/latest/training/#sentencesini).

Wichtig ist hier, dass eine Substitution für das Attribut `room` auf den `friendly_name` der `groups.yml` von Zigbee2MQTT durchgeführt wird um die entsprechende Gruppe anzusteuern.

Als Beispiel weiterführend für das obige Beispiel um den Sprachassistenten für die Steuerung der Gruppe `balcony` zu erweitern:

```
(Balkon | Terasse | Draussen){room:balcony}
```

Jetzt muss der Sprachassistent neu trainiert werden. Das geschiet entsprechend der [Anleitung](/getting-started/installation/#rhasspy-trainieren).

Die Gruppen sind jetzt einsatzbereit und können verwendet werden.


## Node-Red Flows

In der Bibliothek von Node-Red sind unterschiedliche Flows vorhanden, die eingesetzt werden können.

### `LightAPIFlow.json`

Dieser Flow implementiert die Lichtsteuerung über die API [/lights/set](#lightsset). Der Request Body wird über JavaScript-Funktionsblöcke erstellt und an die API übergeben.

### `LightsAPIFlow_Raw.json`

Dieser Flow implementiert die Lichtsteuerung über die API [/lights/set/raw](#lightssetraw). Der Request Body aus Rhasspy wird direkt an die API übergeben, die Logik liegt komplett innerhalb der API.

### `ChangeLightBrightness.json` / `ChangeLightColor.json` / `SwitchLight.json`

Diese drei Flows sollten nur dann aktiv sein, wenn die API nicht verwendet werden soll. Hier liegt die gesamte Logik in Node-Red, die über JavaScript-Funktionsblöcke implementiert wird.


# 🗣 Text To Speech

Wir haben Text-To-Speech.
//TODO

# 📝 Speech To Text

Wir verwenden [Pocketsphinx](https://rhasspy.readthedocs.io/en/latest/speech-to-text/#pocketsphinx) als Speech-To-Text Dienst.

//TODO

# 🕹 Intent Recognition

Wir haben eine Intent Recognition.
//TODO


# 💻 API

## Lichtsteuerung

Es gibt eine eigens entwickelte API für die Lichtsteuerung.

### Unit-Tests

Die API besitzt eigene Unit-Tests zur Gewährleistung der Funktionalität. Zum ausführen der Tests einfach Das Kommando `pytest` unterhalb des Verzeichnisses `/src/api` ausführen. 

### Endpunkte

#### `/lights/set`

Der Endpunkt erwartet einen POST-Request mit einem JSON Objekt, welcher eine vordefinierte Form haben muss. 

```json
{
    "friendly_name": "living_room",
    "payload": {
        "state": "ON",
        "brightness": 255,
        "color": "#55ffaa"
    },
    "feedback": {
        "text": "Okay ich ändere das Licht im Wohnzimmer"
    }
}
```

`friendly_name` und `payload` sind hierbei die erforderlichen Attribute. Die Attribute unter `payload` sind hierbei frei wählbar. 

Aus dem Request wird ein MQTT-Publish auf das Topic `zigbee2mqtt/<friendly_name>/set` mit der jeweiligen Nachricht, die im `payload` Objekt definiert ist.
Nachdem der Publish ausgeführt wurde, wird ein entsprechender Feedback-Text über Text-To-Speech ausgegeben.

Die Schnittstelle ist sehr flexibel einsetzbar, denn sie ist nicht restriktiv.

#### `/lights/set/raw`

Der Endpunkt erwartet einen POST-Request mit einem JSON Objekt, der entsprechend von Rhasspy erzeugt wurde. Wichtig ist hierbei hauptsächlich, dass `entities` entsprechend den Erwartungen der Schnittstelle entspricht.

```json
"entities": [
        {
            "entity": "room",
            "value": "living_room",
            //[..]
        },
        {
            "entity": "state",
            "value": "on",
            //[..]
        },
        {
            "entity": "brightness",
            "value": 255,
            //[..]
        },
        {
            "entity": "color",
            "value": "#ffffff",
            //[..]
        }
    ]
//[..]
```

Die Schnittstelle erstellt aus dem Request eine kompatible MQTT-Nachricht, die dann im jeweiligen Topic gepublished wird.
Danach wird ein entsprechender Feedback-Text über Text-To-Speech ausgegeben, der den eingesprochenen Text wiederholt.