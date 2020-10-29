---
title: API
permalink: /results/api/
subtitle: Entwicklungsergebnisse zur API
layout: page
show_sidebar: false
menubar: results_menu
---

Wir haben uns dazu entschlossen die Features mittels einer API umzusetzen und die einzelnen Features in seperate Python-Module auszulagern. 

Zuerst hatten wir die Überlegung einzelne Python-Funktionen über das Node-Red Addon [pynodered](https://github.com/ghislainp/pynodered) verfügbar zu machen, nach einem kurzen Test hat sich aber herausgestellt, dass diese Bibliothek nichts anderes macht als eine Python-Funktion über eine Web-API freizugeben. Weil die Dokumentation hierzu nicht wirklich umfangreich ist und sich eine Einbindung in einen Docker-Container als nicht trivial erwiesen hat, haben wir uns dazu entschlossen eine eigene Web-API zu entwickeln. Die Entscheidung für eine Web-API fiel insofern leicht, als dass wir bereits Erfahrung mit Web-APIs gesammelt haben und eine einfache Integration in Node-Red gegeben ist.

Als Basis für unsere API haben wir uns für das Web-Framework [Flask](https://flask.palletsprojects.com/) entschieden. Die Wahl auf Flask fiel deshalb, weil es sich hierbei um ein langerprobtes Webframework handelt und anders als bspw. [Django](https://www.djangoproject.com/) für unseren Use-Case einen geringen Overhead besitzt.

Für die Kommunikation über MQTT haben wir die Bibliothek [paho-mqtt](hhttps://www.eclipse.org/paho/index.php?page=clients/python/index.php) gewählt, denn diese wird direkt von der eclipse Foundation entwickelt, welche auch unseren [MQTT-Broker Mosquitto](/docs/tech-stack/#mosquitto) entwickelt. Wir gehen somit von einer hohen Kompatibilität aus. Desweiteren ist die Dokumentation dieser Bibliothek sehr umfangreich und es exisitieren zahlreiche weiterführende Beispiele im Netz.

Die Entwicklung der Lichtsteuerung hat nach einer kurzen Einarbeitungszeit ohne nenneswerte Probleme geklappt. Wir haben uns dazu entschlossen hier zwei Endpunkte anzulegen (Siehe [hier](/docs/features/api/#lichtsteuerung)), um eine gewisse Flexibilität zu bieten. Während ein Endpunkt eine externe Verarbeitung des Intents benötigt (z.B. durch Node-Red) gibt es einen weiteren Endpunkt, der die Verarbeitung übernimmt.

Während der Entwicklung des Weckers haben wir uns die Frage gestellt, wie der Wecker persistiert werden soll. Sollte der Benutzer sich einen Wecker für den nächsten Tag stellen um pünktlich aufzustehen und die Stromverbindung des Raspberry Pis trennen, so sollte der Wecker trotzdem am nächsten Tag gehen (Sofern der Raspberry Pi wieder an mit Strom versorgt wird).
Dazu haben wir uns für eine relationale Datenbank, die auf den SQL-Syntax verwendet entschieden, da wir hier am meisten Erfahrung haben. Wir haben uns aufgrund der [Systemvoraussetzungen](https://www.sqlite.org/about.html) für [SQLite](https://www.sqlite.org/index.html) entschieden, denn hier sind die Anforderungen am geringsten (Im Vergleich zu MySQL/MariaDB und PostgresSQL).

Zu guter letzt haben wir ein [Dockerfile](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/flask/Dockerfile) geschrieben um unsere API genau wie alle anderen Module über eine Docker-Umgebung bereitzustellen.
Problematisch hierbei war, dass unser Python-Code in einem [anderen Verzeichnis](https://github.com/th-koeln-intia/ip-sprachassistent-team1/tree/master/src/api) liegt und somit der Build-Context angepasst werden muss. Das haben wir in der [docker-compose.yml](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/docker-compose.yml) umgesetzt. Eine weitere kleine Besonderheit ist es hier, dass wir zusätzlich zwei Volumes mounten um die Zeitzoneneinstellung des Raspberry Pis innerhalb des Containers zu verwenden.