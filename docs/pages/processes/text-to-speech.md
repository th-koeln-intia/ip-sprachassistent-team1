---
title: Text-To-Speech
permalink: /results/text-to-speech/
subtitle: Entwicklungsergebnisse zur Implementierung des Text-To-Speech Services
layout: page
show_sidebar: false
menubar: docs_menu
---


# 🗣 Text To Speech

## Konfiguration von Espeak

Die Standard-Implementierung von Rhasspy für die Espeak Text-To-Speech Engine bietet nicht viel Raum für Optionen, daher müssen wir uns einem kleinen Trick innerhalb der `profile.json` bedienen und die Standartwerte mit Parametern überschreiben.

Zunächst einmal spricht die Standardeinstellung von Espeak zu schnell und ist desweiteren auch eine männliche Stimme, die für unsere Personifizierung über das Wakeword Trixie ungeeignet ist. Espeak bietet allerdings für die Sprachen verschiedene Stimmarten, die mit einem Suffix bestimmt werden können. Nach durchprobieren hat sich `de+f4` als am natürlichsten ergeben. Die Anpassung der Parameter für Wortpausen sowie Sprechgeschwindigkeit und Pitch sind ebenfalls durch ausprobieren entstanden und im Hinblick auf die Ziele des Forschungsprojekts so gewählt, dass die Stimme gut verständlich ist. 

Die Konfiguration sieht insgesamt so aus:

```json
"text_to_speech": {
        "espeak": {
            "arguments": [
                "-v",
                "de+f4",
                "-s",
                "120",
                "-g",
                "1",
                "-p",
                "45"
            ]
        },
        "system": "espeak"
    }
```

Die Stimme ist leider nicht besonders natürlich, denn es handelt sich hierbei lediglich um einen Sprachsynthesizer, der auf der Verkettung von Diphonen basiert.