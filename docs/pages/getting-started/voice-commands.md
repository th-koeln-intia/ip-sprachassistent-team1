---
title: Verfügbare Sprachbefehle
permalink: /getting-started/voice-commands/
subtitle: Was kann ich mit Deep Thought überhaupt machen?
layout: page
show_sidebar: false
menubar: getting-started_menu
---

# Sprachbefehle

Die Befehle (bis auf das Wake-Word) sind in unterschiedlichen Variationen verfügbar.

| Sprachbefehl                                                                                  | Aktion                                                                                          |
| --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| ["Hey, Trixie"](#hey-trixie)                                                                  | Weckt den Sprachassistenten auf                                                                 |
| ["Schalte das Licht im Wohnzimmer an"](#schalte-das-licht-im-wohnzimmer-an)                   | Schaltet die Lampen die der Gruppe `living_room` zugeordnet sind an                             |
| ["Schalte das Licht im Wohnzimmer auf Stufe 3"](#schalte-das-licht-im-wohnzimmer-auf-stufe-3) | Setzt die Helligkeit der Lampen, die der Gruppe `living_room` zugeordnet sind auf Stufe 3 (30%) |
| ["Schalte das Licht im Wohnzimmer auf grün"](#schalte-das-licht-im-wohnzimmer-auf-grün)       | Setzt die Farbe der Lampen, die der Gruppe `living_room` zugeordnet sind auf die Farbe Grün     |
| ["Setze den Wecker auf 12 Uhr 10"](#setze-den-wecker-auf-12-uhr-10) | Setzt den Wecker auf 12:10
| ["Lösche den Wecker"](#loesche-den-wecker) | Löscht den Wecker
| ["Stoppe den Wecker"](#stoppe-den-wecker) | Stoppt den aktuell klingelnden Wecker
| ["Setze den Weckton auf eins"](#setze-den-weckton-auf-eins) | Ändert den Weckton für den aktuell eingestellten Wecker

## Wake-Word

Das Wake-Word muss bei der ersten Verwendung eingerichtet werden, siehe dafür: [Wake-Word einrichten](/getting-started/installation/#wake-word-einrichten).

### "Hey, Trixie"

Wir empfehlen dieses Wake-Word, auch wenn es nicht zwingend verwendet werden muss, denn es hat sich als außerordentlich zuverlässlich erwiesen.
Siehe hierzu auch: [Prozess zur Suche eines geeigneten Wake-Words](/docs/features/#-wake-word)

## Lichtsteuerung

### "Schalte das Licht im Wohnzimmer an"

Der Sprachassistent ist in der Lage das Licht in den konfigurierten Räumen aus- und anzuschalten.

### "Schalte das Licht im Wohnzimmer auf Stufe 3"

Der Sprachassistent ist in der Lage die Helligkeit des Lichts in den konfigurierten Räumen zu steuern.
Die Helligkeit wird Stufenweise in den Stufen von 0-10 gesetzt, wobei 0 0% Helligkeit entspricht und 10 100%.

### "Schalte das Licht im Wohnzimmer auf grün"

Der Sprachassistent ist in der Lage die Farbe des Lichts in den konfigurierten Räumen zu steuern.
Es sind folgende Farben verfügbar (//TODO Weitere Farben und insbesondere auch Weiß/Warmweiß):

* Blau
* Gelb
* Orange
* Grün
* Rot
* Lila

## Wecker

### "Setze den Wecker auf 12 Uhr 10"

Der Wecker kann auf jede beliebige Uhrzeit gesetzt werden. Dabei gibt man die Uhrzeit im 24 Stunden Format an. Besteht bereits ein Wecker, so wird dieser überschrieben.

### "Lösche den Wecker"

Hiermit löscht man den vorhandenen Wecker. Mit dem Wecker wird auch der eingestellte Ton gelöscht, wodurch der nächste Wecker wieder den Weckton Nr. 1 erhält.

### "Stoppe den Wecker"

Wenn der Wecker klingelt, kann man den Wecker mit diesem Befehl ausschalten. Dabei ist zu beachten, dass das Wake-Word nur in den Pausen zwischen den einzelnen Wecktönen erkannt wird.

### "Setze den Weckton auf eins"

Standardmäßig kann zwischen zwei Wecktönen ausgewählt werden. 

| Weckton 1 | [Sound](/assets/1.wav)
| Weckton 2 | [Sound](/assets/2.wav)