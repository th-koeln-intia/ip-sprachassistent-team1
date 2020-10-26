---
title: Features
permalink: /docs/features/
subtitle: Was kann Deep Thought im Detail und wie lässt sich Deep Thought erweitern?
layout: page
show_sidebar: false
menubar: docs_menu
---

# 🎙 Wake Word

Deep Thought besitzt ein Aktivierungswort (Wake-Word, Hotword) welches verwendet wird um den Sprachassistenten aufzuwecken. Wir empfehlen hier das Wake-Word "Hey, Trixie", was sich während der Entwicklung als geeignet herausgestellt hat.
Es ist trotzdem möglich eigene Aktivierungswörter und auch unterschiedliche zu verwenden.

Die Wörter können sehr einfach und über eine [Audioaufnahme in Rhasspy definiert](/getting-started/installation/#wake-word-einrichten) werden. Wenn man mehrere Aktivierungswörter verwenden möchte, ist es allerdings wichtig darauf zu achten, die ID dort eindeutig zu setzen (beispielsweise: `heytrixie_marcel`).
Rhasspy übernimmt dann das Speichern im korrekten Ordner und trimmt die Audiospur.

Alternativ können auch aufgenomme Audio-Dateien direkt in den entsprechenden Ordner `docker/rhasspy/profiles/de/raven/<wake-word-id>` gelegt werden. 
Wichtig ist allerdings darauf zu achten, dass die Dateien zum ersten im WAVE-Format (1 Channel, 16000 Hz, 16 Bit LE) mit einem fortlaufend nummerierten festgelegten Dateinamen abgelegt werden und zum anderen, dass die Audiospur auf das Wake-Word zugeschnitten ist. Auch wenn es möglich ist, die Aufnahmen mit einem anderen Endgerät/Mikrofon zu erstellen und entsprechend abzulegen empfehlen wir die Aufnahmen für die besten Ergebnisse direkt auf dem Endgerät zu machen.

Der Dateiname muss mit `example-` beginnen. Es können beliebig viele Aufnahmen gespeichert werden.
Eine Mögliche Struktur des Verzeichnisses sähe also folgendermaßen aus:

```
📦ip-sprachassistent-team1
 ┣ 📂docker
 ┃ ┣ 📂rhasspy
 ┃ ┃ ┣ 📂profiles
 ┃ ┃ ┃ ┣ 📂de
 ┃ ┃ ┃ ┃ ┣ 📂raven
 ┃ ┃ ┃ ┃ ┃ ┣ 📂heytrixie_marcel
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜example-0.wav
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜example-1.wav
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜example-2.wav
 ┃ ┃ ┃ ┃ ┃ ┣ 📂heytrixie_karl
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜example-0.wav
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜example-1.wav
 ┃ ┃ ┃ ┃ ┃ ┣ 📂alexa_susi
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜example-0.wav
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜example-1.wav
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜example-2.wav
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜example-3.wav
```

Wenn man diesen Weg wählt, muss Rhasspy allerdings noch entsprechend konfiguriert werden - das passiert in der [`profile.json` Datei](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/rhasspy/profiles/de/profile.json). Da müssen die aktiven Aktivierungswörter mit der jeweiligen ID und optional spezifischen Einstellungen definiert werden. Für das obige Beispiel sähe eine mögliche Konfiguration so aus:

```json
{
  "wake": {
    "raven": {
      "keywords": {
        "heytrixie_marcel": {},
        "heytrixie_karl": {
          "average_templates": true,
          "probability_threshold": "0.8"
        },
        "alexa_susi": {
          "minimum_matches": 2
        }
      },
      "minimum_matches": "1",
      "probability_threshold": "0.58",
      "vad_sensitivity": "1"
    },
    "system": "raven"
  }
}
```

Weitere Informationen hierzu finden sich in unseren [Entwicklungsergebnissen](/results/wake-word/) und in der [Rhasspy Dokumentation](https://rhasspy.readthedocs.io/en/latest/wake-word/#raven).

# 🔊 Hintergrungeräuschreduzierung

Wir haben zum einen eine Hintergrundgeräuschreduzierung als Referenz implementiert und zum anderen weitere Möglichkeiten evaluiert (Siehe hierzu: [Ergebnisse Hintergrundgeräuschreduzierung](/results/noise-cancelling/)). Die derzeitige Lösung basiert auf Frequenzmodulation mit [SoX](http://sox.sourceforge.net/sox.html), wobei zum einen das Grundrauschen der Hardware entfernt wird und zum anderen ein Noise-Gate für etwaige Hintergrundgeräusche verwendet wird.

Eine Erweiterung sollte unter Berücksichtigung der Ergebnisse geschehen.

Unter Umständen ist es notwendig das Grundrauschen erneut aufzunehmen bzw. nicht das mitgelieferte Profil zu verwenden, wenn sich der Pi in einer anderen Umgebung befindet oder die Hardware erweitert/geändert wird. Dafür sind die folgenden Schritte notwendig:

Wir nehmen 10 Sekunden Grundrauschen auf - dabei sollte absolute Ruhe abseits des Grundrauschens sein und erstellen daraus ein Rauschprofil.
```sh
arecord -Dsysdefault:CARD=seeed4micvoicec -f S32_LE -r 16000 -c 4 -d 10 noise.wav
sox noise.wav -n noiseprof noise_sox.prof
```

Das daraus resultierende Rauschprofil legen wir jetzt in dem rhasspy-Ordner ab und ersetzen die bereits vorhandene Datei.

```
📦ip-sprachassistent-team1
 ┣ 📂docker
 ┃ ┣ 📂rhasspy
 ┃ ┃ ┗ 📜noise_sox.prof
```

Möglicherweise ist es jetzt noch notwendig den `amount` Parameter für den SoX Effekt `noisered` anzupassen, das ganze muss in der [profile.json](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/rhasspy/profiles/de/profile.json) unter `microphone.command.record_arguments` passieren.

# 💡 Lichtsteuerung

### Erweiterung der Gruppen

Sollten weitere Gruppen über den Sprachassistenten angesteuert werden sollen und diese bereits nach [Konfigurieren der Gruppen](#konfigurieren-der-gruppen) definiert worden sein, dann muss für Rhasspy die Datei [profiles/de/slots/light_rooms](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/rhasspy/profiles/de/slots/light_rooms) angepasst werden. Das Format hier richtet sich nach der [Dokumentation von Rhasspy](https://rhasspy.readthedocs.io/en/latest/training/#sentencesini).

Wichtig ist hier, dass eine Substitution für das Attribut `room` auf den `friendly_name` der [groups.yml](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/zigbee2mqtt/data/groups.yaml) von Zigbee2MQTT durchgeführt wird um die entsprechende Gruppe anzusteuern.

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