---
title: Showcase
permalink: /docs/showcase/
subtitle: Showcase
layout: page
show_sidebar: false
menubar: docs_menu
---

Für das erste Sprint Review wurde ein kleiner Showcase in Python entwickelt um unseren Entwicklungsstand präsentieren 
zu können. 

Es handelt sich hierbei um einen simplen Logger, der auf einige MQTT-Topcis subscribed und die entsprchenden Nachrichten
als Log ausgibt.
Hierbei liegt der Schwerpunkt auf der Wakeword-Erkennung sowie dem Speech-To-Text Service.

Die Daten der Services werden nach dem [Hermes Protokoll](https://docs.snips.ai/reference/hermes) als Nachrichten im 
MQTT-Broker bereitgestellt.

Der Showcase befindet sich im Ordner `/src/showcase` und kann wahlweise über die Datei `/src/main.py` oder
`/src/showcase/showcase.py` ausgeführt werden. Dazu muss der Sprachassistent Deep Thought laufen (Siehe hierzu 
[Installation](/getting-started/installation)) und der MQTT Broker über das Netzwerk erreichbar sein. 

Zum Ausführen sind dann die folgenden Schritte notwendig:

1. Python 3 installieren
2. Requirements mit `pip install -r requirements.txt` installieren
3. Ausführen des Showcase mit `python ./src/main.py`

