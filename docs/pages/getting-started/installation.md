---
title: Installation
permalink: /getting-started/installation/
subtitle: Wie verwende ich Deep Thought?
layout: page
show_sidebar: false
menubar: getting-started_menu
---

# Installationsanleitung

Wir setzen eine frische [Installation von Raspberry Pi OS](https://www.raspberrypi.org/downloads/raspberry-pi-os/) vorraus. Eine Grafische Oberfläche ist nicht erforderlich, es genügt also Raspberry Pi OS Lite.

## Repository clonen

Zunächst benötigen wir die erforderlichen Daten von Deep Thought. Am einfachsten ist es unser [GitHub-Repository](https://github.com/th-koeln-intia/ip-sprachassistent-team1) zu clonen.

```sh
sudo apt-get update
sudo apt-get install git
git clone https://github.com/th-koeln-intia/ip-sprachassistent-team1.git
cd ip-sprachassistent-team1
```

Die Daten befinden sich jetzt auf dem Raspberry Pi.

## Tooling installieren
Jetzt müssen wir einige Tools installieren und Konfigurationen setzen. Wir stellen dafür ein Script Namens [install.sh](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/install.sh) bereit, man kann sie allerdings auch manuell ausführen.

```sh
sudo chmod +x ./docker/install.sh
sudo ./docker/install.sh
```

Das Skript führt die folgenden Schritte durch:
* SPI auf dem Raspberry Pi aktiveren
* Docker installieren
* Nutzer `pi` zur docker-Gruppe hinzufügen
* docker-compose installieren
* Respeaker 4-Mic-Array Treiber installieren
* Vordefinierte `asound` Konfiguration setzen

Die Ausführung des Skripts kann relativ lange dauern. Nach der installation ist ein Neustart mittels `sudo reboot` notwendig, das Skript führt diesen nicht von alleine aus.

## Sprachassistenten installieren

### Docker

Wir empfehlen zur Benutzung von Deep Thought eine Docker-Umgebung zu verwenden. Zuerst muss man die Umgebungsvariablen für die docker-compose Datei seinen Bedürfnissen anpassen. Hierfür legt man auf Basis der [./docker/.env.example](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/.env.example) eine Datei ./docker/.env an und bearbeitet diese anschließend mit dem Editor seiner Wahl.

```sh
cp ./docker/.env.example ./docker/.env
```

Anschließend kann man mithilfe der [docker-compose.yml](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/docker-compose.yml) alle Services starten:

```sh
cd ./docker
docker-compose up -d 
```

Nachdem die Services gestartet sind, sind sie unter folgenden Adressen erreichbar:

| Service     |                         URL                          |
| ----------- | :--------------------------------------------------: |
| Rhasspy     | [http://raspberrypi:12101](http://raspberrypi:12101) |
| Node-Red    |  [http://raspberrypi:1880](http://raspberrypi:1880)  |
| MQTT-Broker |  [mqtt://raspberrypi:1883](mqtt://raspberrypi:1883)  |

## Download der erforderlichen Dateien für Rhasspy

Auch wenn der Sprachassistent offline arbeitet, ist es für die Einrichtung notwendig, den Raspberry Pi einmalig mit dem Internet zu verbinden, damit die erforderlichen Dateien heruntergeladen werden können. Am einfachsten ist es den LAN-Anschluss des Pis zu verwenden.

Sobald der Raspberry Pi eine Internetverbindung hat, wird im Web-Interface von Rhasspy unter [http://raspberrypi:12101](http://raspberrypi:12101) ein Download-Hinweis angezeigt. Die erforderlichen Dateien lassen sich dann mit einem Knopfdruck herunterladen. Sobald der Download abgeschlossen ist, kann die Internetverbindung wieder getrennt werden.

![Rhasspy Download](/assets/rhasspy_download.PNG)

## Wake-Word einrichten

Damit der Sprachassistent perfekt auf die eigene Stimme eingestellt ist, muss nach dem ersten Start das Wake-Word eingesprochen werden. Hierzu öffnet man die Rhasspy Oberfläche [http://raspberrypi:12101](http://raspberrypi:12101) und klickt auf das Ausrufezeichen, um den Wake-Word Manager zu öffnen.

![WakeWord1](/assets/wword_1.PNG)

Anschließend muss das Wake-Word eingesprochen werden. Hierzu klickt man auf den Record Knopf neben Example 1 und sagt "Hey, Trixie". Das ganze wiederholt man für Example 2 und Example 3.

![Wakeword2](/assets/wword_2.PNG)

Wenn man mit den Sprachaufnahmen zufrieden ist müssen diese noch gespeichert werden. Hierzu scrollt man fast bis ans Ende der Seite und klickt dort auf "Save Settings".

![Wakeword3](/assets/wword_3.PNG)


## Lampen einrichten

### Lampen mit Zigbee2MQTT Verbinden

Zuerst muss die Zigbee-fähige Lampe Zigbee2MQTT bekannt sein. Wir verwenden im Folgenden die aus dem [Tech-Stack](/docs/tech-stack/) bekannte Philips Hue white and color (929001573). Wenn andere Lampen verwendet werden sollen, müssen die Schritte entsprechend der [Dokumentation von Zigbee2MQTT](https://www.zigbee2mqtt.io/information/supported_devices.html) angepasst werden.

Die einfachste Methode für unsere Lampe ist ein [Touchlink reset](https://www.zigbee2mqtt.io/information/touchlink). Dazu genügt es eine Nachricht ohne Nutzdaten in das MQTT-Topic `zigbee2mqtt/bridge/config/touchlink/factory_reset` zu publishen. Die Lampe muss sich dafür nahe (laut Dokumentation in Entfernung von unter 10cm) an dem Zigbee-Stick befinden. Zusätzlich muss in der [configuration.yaml](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/zigbee2mqtt/data/configuration.yaml) von Zigbee2MQTT das Attribut `permit_join: true` gesetzt sein.

Sobald sich die Glühbirne gepaart hat, sollte diese kurz aufblinken und die Paarung ist abgeschlossen.

Es ist sinnvoll nach jeder Paarung einer Lampe einen `friendly_name` in der [devices.yaml](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/zigbee2mqtt/data/devices.yaml) zuzuweisen um den Überblick nicht zu verlieren und die Konfiguration später zu erleichtern. Zum Beispiel so.

```yml
'0x123456789abcdef0':
  friendly_name: 'lamp_living_room_1'
'0x123456789abcdef1':
  friendly_name: 'lamp_bathroom_1'  
'0x123456789abcdef2':
  friendly_name: 'lamp_bathroom_2'
'0x123456789abcdef3':
  friendly_name: 'lamp_balcony_1'
```

Nachdem alle gewünschten Lampen erfolgreich verbunden sind, sollte `permit_join: false` gesetzt werden.

Wir werden im Folgenden zwei Möglichkeiten beschreiben einen Touchlink reset durchzuführen:

#### Touchlink Reset über Node-Red

Im Web-Interface von [Node-Red](http://raspberrypi:1880/) ist ein Flow Namens `Touchlink Reset` verfügbar, der mit einem einfachen Klick eine entsprechende Nachricht in das MQTT-Topic published.

![Node-Red Touchlink Reset Flow](/assets/Node-Red_Tochlink_Reset.png)

#### Touchlink Reset über MQTT-Explorer

Im Folgenden verwenden wir den [MQTT Explorer](http://mqtt-explorer.com/) um den MQTT-Broker anzusteuern und beginnen damit uns auf dem bereitgestellten Mosquitto-Broker anzumelden:

![MQTT-Explorer Login](/assets/MQTT_Explorer_1.png)

Der Login sollte erfolgreich sein und wir können eine leere Nachricht auf das oben genannte Topic publishen:

![MQTT-Explorer Publish](/assets/MQTT_Explorer_2.png)

### Konfigurieren der Gruppen

In der [groups.yaml](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/zigbee2mqtt/data/groups.yaml) werden die Gruppen der Lampen genau spezifiziert. Derzeit unterstützt der Sprachassistent die Folgenden Gruppen:

* living_room
* bedroom
* dining_room
* kitchen
* hallway
* bathroom

Weitere Gruppen können hier zwar definiert und über MQTT verwendet werden, allerdings ist der Sprachassistent noch nicht für diese Trainiert. Wenn der Sprachassistent diese auch ansprechen soll, muss die Konfiguration entsprechend der [Dokumentation](/docs/features/light) angepasst werden.

Damit die Lampen gruppenweise angesteuert werden können, müssen diese den Gruppen über ihre ID zugeordnet werden, das sähe dann für das obige Beispiel weiterführend so aus:

```yml
'1':
    friendly_name: living_room
    devices:
        - '0x123456789abcdef0'
'2':
    friendly_name: bathroom
    devices:
        - '0x123456789abcdef1'
        - '0x123456789abcdef2'
'3':
    friendly_name: balcony
    devices:
        - '0x123456789abcdef3'
```

Wichtig ist hier, dass die numerische Gruppen-ID eindeutig ist.

## Rhasspy trainieren

Um den Sprachassitenten zu trainieren muss man das [Web-Interface von Rhasspy](http://raspberrypi:12101) aufrufen und den Button "Train" drücken. Es kann sein, dass je nach Konfiguration ein Warnhinweis erscheint, der angibt, dass es Wörter ohne bekannte Aussprache gibt. Dann muss die Datei [custom_words.txt](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/rhasspy/profiles/de/custom_words.txt) entsprechend der [Dokumentation](https://rhasspy.readthedocs.io/en/latest/training/#custom-words) angepasst werden. Das Web-Interface leitet einen in dem Fall allerdings durch den Prozess. Bei der Erstinstallation sollte das allerdings nicht nötig sein.

![Rhasspy Training](/assets/Rhasspy_Training.png)