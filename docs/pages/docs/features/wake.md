---
title: Wake Word
permalink: /docs/features/wake
subtitle: Hey, Trixie!
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