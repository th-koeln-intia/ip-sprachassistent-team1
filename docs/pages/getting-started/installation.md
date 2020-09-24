---
title: Installation
permalink: /getting-started/installation/
subtitle: Installation
layout: page
show_sidebar: false
menubar: getting-started_menu
---

# Installation

## Installation mit Docker

Für die gegebene Hardware existiert eine Docker-Umgebung, die zum Schnelleinstieg verwendet werden kann.
Im Repository unter `/docker` finden sich die benötigten Daten.

Um mit einem frisch aufgesetzten Raspbian Image zu starten sind folgende Schritte notwendig:

```sh
git clone https://github.com/th-koeln-intia/ip-sprachassistent-team1
cd ip/sprachassistent-team1/docker
sudo chmod +x install.sh
sudo ./install.sh
``` 

Über das install script werden die nativen Abhängigkeiten für das Projekt installiert sowie die notwendigen Konfigurationsschritte des Betriebssystems durchgeführt.
Das ganze kann sehr lange (20min) dauern. Der Kernel wird mit einem Treiber ergänzt, es ist daher ratsam nicht nochmal nach der installation den Befehl `apt-get upgrade` auszuführen.

Das Skript führt die folgenden Schritte durch:
* SPI auf dem Raspberry Pi aktiveren
* docker installieren
* Nutzer `pi` zur docker-Gruppe hinzufügen
* docker-compose installieren
* Respeaker 4-Mic-Array Treiber installieren
* Vordefinierte `asound` Konfiguration setzen

Nach der installation ist ein Neustart mittels `sudo reboot` notwendig, das Skript führt diesen nicht von alleine aus.

Um die Umgebungsvariablen für Docker zu setzen, ist es sinnvoll eine `.env` Datei anzulegen, beispielsweise:

```env
ZIGBEE_DEVICE_PATH=/dev/ttyACM0
```

Jetzt kann die Docker-Umgebung gestartet werden. Auch dieser Schritt kann sehr lange dauern, denn es wird ein Docker Image gebaut.

```sh
docker-compose --env-file ./.env up -d
```

| Service     |                         URL                          |
| ----------- | :--------------------------------------------------: |
| Rhasspy     | [http://raspberrypi:12101](http://raspberrypi:12101) |
| Node-Red    |  [http://raspberrypi:1880](http://raspberrypi:1880)  |
| MQTT-Broker |  [mqtt://raspberrypi:1883](mqtt://raspberrypi:1883)  |
