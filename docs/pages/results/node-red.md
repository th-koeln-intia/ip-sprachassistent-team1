---
title: Node-Red
permalink: /results/node-red
subtitle: Entwicklungsergebnisse zu den Node-Red Flows
layout: page
show_sidebar: false
menubar: results_menu
---

# Node-Red Flows

Wir haben unterschiedliche Flows in Node-Red entwickelt. Maßgeblich für die Verwendung von Node-Red war die Zugänglichkeit der Entwicklungsumgebung auch für Personen, die möglicherweise nicht ganz so vertraut mit der Programmierung sind, sodass man relativ leicht nachvollziehen kann wie die Logik implementiert ist.

Es wäre natürlich auch möglich gewesen diesen Teil der Logik an einen anderen Ort auszulagern, denn Rhasspy bietet da [unterschiedliche Schnittstellen](https://rhasspy.readthedocs.io/en/latest/reference/) auf die man zugreifen kann.

## Methodik

Unsere Flows sind in der Bibliothek von Node-Red verfügbar, das hat für die Entwicklung den entscheidenenden Vorteil, dass wir an unterschiedlichen Dateien arbeiten, denn standardmäßig verwendet Node-Red eine einzige Datei zur Verwaltung aller Flows. Wir haben uns dazu entschlossen die Entsprechende Datei `flows.json` aus unserer Versionsverwaltung zu entfernen, damit wir dort nicht in Konflikte geraten.

Alle implementierten Flows finden sich in einem [separaten Ordner](https://github.com/th-koeln-intia/ip-sprachassistent-team1/tree/master/docker/node-red/data/lib/flows) in einer dedizierten Datei auf die aus Node-Red heraus zugegriffen werden kann.

## Flows im Detail

Im Folgenden werden wir die einzelnen implementieren Flows betrachten und deren Sinn erörtern.

### SwitchLight

![Flow_SwitchLight](/assets/Flow_SetLight.png)

Dieser Flow stellt eine Implementierung auf Basis von den Node-Red Bausteinen dar um eine ZigBee-Fähige Lampe ein- und auszuschalten. Die gesamte Logik um das Ziel zu erreichen liegt hier in Node-Red durch JavaScript-Bausteine, die die nötige Transformation der Daten vornehmen.
Es wird ein entsprechender Befehl zum einschalten der Lampe über MQTT gesendet und ein passendes Feedback mittels Text-To-Speech ausgegeben.
In erster Linie wurde dieser Flow genau wie [ChangeLightBrightness](#changelightbrightness) und [ChangeLightColor](#changelightcolor) zum Testen verwendet. Nichtsdestotrotz haben wir uns dazu entschieden den Flow als Referenz mit zu versionieren.

Sollte dieser Flow verwendet werden, sollte man darauf achten, diesen in Kombination mit [ChangeLightBrightness](#changelightbrightness) und [ChangeLightColor](#changelightcolor) zu verwenden und [LightAPIFlow](#lightapiflow) sowie [LightAPIFLow_Raw](#lightapiflow_raw) zu deaktivieren.

### ChangeLightBrightness

![Flow_ChangeLightBrightness](/assets/Flow_ChangeLightBrightness.png)

Siehe [SwitchLight](#switchlight), nur handelt es sich hierbei um die Steuerung der Helligkeit der Lampe.

### ChangeLightColor

![Flow_ChangeLightColor](/assets/Flow_ChangeLightColor.png)

Siehe [SwitchLight](#switchlight), nur handelt es sich hierbei um die Steuerung der Farbe der Lampe.

### Touchlink Reset

![Flow_Touchlink](/assets/Flow_Touchlink.png)

Führt einen [Touchlink Reset](https://www.zigbee2mqtt.io/information/touchlink) durch um eine entsprechende Zigbee-fähige Lampe zu koppeln. Der Touchlink Reset kann über einen einfachen Mausklick auf der Schaltfläche des "Injizieren"-Bausteins durchgeführt werden.

### LightAPIFlow

![Flow_LightAPI](/assets/Flow_LightAPI.png)

Wir haben die Lichtsteuerung in einer [eigens entwickelten API](/docs/features/#api) integriert, die in diesem Flow verwendet wird. Dabei reagiert dieser Flow auf alle drei Intents `SwitchLight`, `ChangeLightColor` sowie `ChangeLightBrightness` und verarbeitet diese über JavaScript-Bausteine zu einem validen API-Call.

Sollte dieser Flow verwendet werden, sollte man darauf achten, die Flows [ChangeLightBrightness](#changelightbrightness) und [ChangeLightColor](#changelightcolor) sowie [LightAPIFLow_Raw](#lightapiflow_raw) zu deaktivieren.

### LightAPIFlow_Raw

![Flow_LightAPI_Raw](/assets/Flow_LightAPI_Raw.png)

Siehe [LightApiFlow](#lightapiflow), nur dass die gesamte Logik innerhalb der API liegt. Es wird direkt das erzeugte Intent aus Rhasspy an diese übergeben und in der API verarbeitet.

Sollte dieser Flow verwendet werden, sollte man darauf achten, die Flows [ChangeLightBrightness](#changelightbrightness) und [ChangeLightColor](#changelightcolor) sowie [LightAPIFLow](#lightapiflow) zu deaktivieren.

### Wecker

![Flow_Wecker](/assets/Flow_Wecker.png)

Der Flow dient zur Steuerung des Weckers. Sobald ein hierzu passendes Intent aus Node-Red erkannt wird, wird die API des Weckers aufgerufen.