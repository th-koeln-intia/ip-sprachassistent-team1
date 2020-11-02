---
title: API
permalink: /docs/features/api
subtitle: GET /docs/features/api
layout: page
show_sidebar: false
menubar: docs_menu
---

# 💻 API

## Lichtsteuerung & Wecker

Es gibt eine eigens entwickelte API für die Lichtsteuerung und den Wecker.

### Unit-Tests

Die API besitzt eigene Unit-Tests zur Gewährleistung der Funktionalität. Zum ausführen der Tests einfach Das Kommando `pytest` unterhalb des Verzeichnisses [/src/api](https://github.com/th-koeln-intia/ip-sprachassistent-team1/tree/master/src/api) ausführen. 

### Endpunkte

#### `GET: /alarm`

Liefert ein Array aller gespeicherten Wecker.

```json
[
    {
        "id": 0,
        "hours": 11,
        "minutes": 11,
        "active": 1,
        "sound": 1
    }
]
```

#### `POST: /alarm`

Speichert einen Wecker in der Datenbank. Sollte bereits ein Wecker mit der ID existieren, wird dieser ersetzt. Als Rückgabewert erhält man alle Wecker, die nach dem Speichern in der Datenbank stehen. Folgende Eingabeparameter werden erwartet:

**Request Parameter**

| Key                   | Datentyp  | Beispiel  |
| --------------------- | ----------------------|
| id (required)         | Integer   | 0         |
| hours (required)      | Integer   | 11        |
| minutes (required)    | Integer   | 11        |
| active (required)     | 0 oder 1  | 1         |
| sound (required)      | Integer   | 1         |

**Response**

```json
[
    {
        "id": 0,
        "hours": 11,
        "minutes": 11,
        "active": 1,
        "sound": 1
    }
]
```

#### `DELETE: /alarm`

Löscht einen Wecker aus der Datenbank. Als Rückgabewert erhält man alle Wecker, die nach dem Löschen in der Datenbank stehen. Folgende Eingabeparameter werden erwartet:

**Request Parameter**

| Key                   | Datentyp  | Beispiel  |
| --------------------- | ----------------------|
| id (required)         | Integer   | 0         |

**Response**

```json
[
    {
        "id": 0,
        "hours": 11,
        "minutes": 11,
        "active": 1,
        "sound": 1
    }
]
```

#### `POST: /alarm/stop`

Stoppt den Alarm anhand der mitgelieferten ID. Folgende Eingabeparameter werden erwartet:

**Request Parameter**

| Key                   | Datentyp  | Beispiel  |
| --------------------- | ----------------------|
| id (required)         | Integer   | 0         |

**Response**

```json
"success"
```

#### `POST: /alarm/sound`

Setzt den Weckton für einen bestimmten Wecker. **Achtung** Der Weckton gilt nur für diesen Wecker. Sollte der Wecker gelöscht werden und ein neuer erstellt werden, erhält dieser wieder den Weckton mit dem Wert 1. Folgende Eingabeparameter werden erwartet:

**Request Parameter**

| Key                   | Datentyp  | Beispiel  |
| --------------------- | ----------------------|
| id (required)         | Integer   | 0         |
| sound (required)      | Integer   | 2         |

**Response**

```json
"success"
```



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