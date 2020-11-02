---
title: Weiterentwicklung der API
permalink: /docs/api/
subtitle: Wie kann ich die API weiterentwickeln?
layout: page
show_sidebar: false
menubar: docs_menu
---

# Virtual Enivronemnt einrichten

Zur Weiterentwicklung der API ist es sinnvoll eine Virtual-Environment einzurichten. Zuerst sollte Python3 inklusive pip installiert sein.
Unter dem Stammverzeichnis des Sprachassistenten, kann man jetzt leicht eine Virtual Enviroment mit folgendem Kommando erstellen:

```sh
python3 -m venv venv
```

Der Befehl erstellt unter `./venv` eine virtuelle Python-Umgebung die wir jetzt noch aktivieren müssen. Je nachdem ob wir uns unter Windows oder UNIX/Linux befinden ist der Befehl dafür unterschiedlich:

```sh
venv\Scripts\activate.bat # Windows
source venv/bin/activate #UNIX/Linux
```

Für die Entwicklung ist es noch notwendig, die Abhängigkeiten in der Virtual Environment zu installieren. Das erreicht man über den Befehl:
```sh
pip install -r ./src/api/requirements.txt
```

# Neue API-Anlegen

Sollte man eine neue API anlegen wollen, so ist es sinnvoll unter `./src/api/` eine neue Python-Datei anzulegen um eine Modularisierung der Features zu haben. Jetzt ist es nur noch notwendig in der Datei `./src/api/app.py` das Modul zu importieren, indem man in der Letzen Zeile folgende Zeile hinzufügt wobei `feature` der jeweilige Dateiname ohne Dateiendung ist.

```py
from api import feature
```

Jetzt kann man mit der Implementierung des jeweiligen Features beginnen.