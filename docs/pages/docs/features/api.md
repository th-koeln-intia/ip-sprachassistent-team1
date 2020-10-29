---
title: API
permalink: /docs/features/api
subtitle: GET /docs/features/api
layout: page
show_sidebar: false
menubar: docs_menu
---

# 💻 API

## Lichtsteuerung

Es gibt eine eigens entwickelte API für die Lichtsteuerung.

### Unit-Tests

Die API besitzt eigene Unit-Tests zur Gewährleistung der Funktionalität. Zum ausführen der Tests einfach Das Kommando `pytest` unterhalb des Verzeichnisses [/src/api](https://github.com/th-koeln-intia/ip-sprachassistent-team1/tree/master/src/api) ausführen. 

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