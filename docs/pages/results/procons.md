---
title: Vor- und Nachteile
permalink: /results/pros-and-cons/
subtitle: Warum sollte ich Deep Thought verwenden? Wann ist Deep Thought ungeeignet?
layout: page
show_sidebar: false
menubar: results_menu
---

<h1 style="color:green">Vorteile</h1>

## Hintergrundgeräuschunterdrückung evaluiert und als PoC implementiert
Wir haben uns intensiv mit dem Thema Hintergrundgeräuschunterdrückung auseinandergesetzt, was alleine durch die Filterung des Grundrauschens in ein um einiges klareres Klangbild resultiert. Das unterstüzt unseren Speech-To-Text Service Pocketsphinx dabei die Sprachbefehle besser zu verstehen und zuverlässigere Ergebnisse zu liefern.
Wir haben unterschiedliche Möglichkeiten hierzu untersucht und zusammengefasst, was eine gute Grundlage zur Weiterentwicklung des Themas bietet. In unserer Referenzimplementierung ist es möglich den Sprachassistenten trotz etwaiger störender Geräusche im Hintergrund zuverlässig zu nutzen, wenn sich dieser in unmittelbarer Nähe des Nutzers befindet. Siehe hierzu: [Hintergrundgeräuschunterdrückung](/results/noise-cancelling/).

## Kann nicht von fremden Personen gesteuert werden
Da das Wake-Word über die Signatur des Audiosignals erkannt wird und nicht über speech-to-text, können fremde Personen den Sprachassistenten nicht steuern. Sollte ein weiterer Nutzer den Assistenten bedienen können, ist es leicht ein weiteres Wake-Word hinzuzufügen.

## Schnelle Konfiguration
Die einzelnen Services lassen sich ohne schnell konfigurieren und sind bereits nach einer kurzer Einarbeitungszeit erweiterbar.

## Zuverlässiges Wake-Word
Wir haben ein sehr zuverlässiges Wake-Word gefunden, was nach unserer Erfahrung im Alltag extrem selten Falsch-Positive und -Negative Erkennungen hat. 

## Flexible API mit Erweiterungsmöglichkeiten
Unsere API ist leicht auf weitere Use-Cases erweiterbar.

## Zuverlässige Spracherkennung
Unsere Implementation bietet eine sehr zuverlässige Erkennung der jeweiligen Intents bzw. der Sprache im allgemeinen.

## Docker-Umgebung und nahezu automatisierte Installation
Deep Thought wurde für eine Docker-Umgebung entwickelt, wodurch wir eine einfache Isolation des Sprachassistenten und leichte Bereitstellung auf mehreren Endgeräten bieten. Die Installation der nativen Abhängigkeiten erfolgt über ein Skript nahezu komplett automatisiert.

## Offline-Betrieb
Deep Thought kann komplett offline betrieben werden, es ist für den Betrieb keine Internetverbindung erforderlich. Lediglich während der Installation ist aus Komfortgründen notwendig kurzfrisitig eine Internetverbindung aufzubauen. 

## Datenschutz
Die Daten sind sicher, jegliche Kommunikation (Mit Ausnahme der Wake-Word Aufnahmen) wird nicht persistiert und auch nicht für ein eigenes Sprachmustertraining verwendet. 

<h1 style="color:red">Nachteile</h1>

## Bedienung aus der Ferne nicht möglich
In unserer Referenzimplementierung der Hintergrundgeräuschunterdrückung ist es nicht möglich den Sprachassistenten aus einer großen Distanz zu bedienen, denn die Sprache wird unter Umständen als Hintergrundgeräusch wahrgenommen und herausgefiltert. Wir haben jedoch weitere Möglichkeiten aufgelistet, die als Grundlage zur Weiterentwicklung dienen können. Siehe hierzu: [Hintergrundgeräuschunterdrückung](/results/noise-cancelling/).

## Langsame Erkennung Speech-to-text
Die Spracherkennung ist auf dem Raspberry 3 relativ langsam, weshalb es sich dort empfiehlt die Erkennung auf einen [Server auszulagern](https://rhasspy.readthedocs.io/en/latest/speech-to-text/#remote-http-server). Auf dem Raspberry 4 ist die Spracherkennung schneller, weshalb man dort auf den extra Server verzichten könnte.

## Wake-Word muss für jede Person eingesprochen werden
Damit das Wake-Word erkannt wird, muss dieses von jeder Person, die den Sprachassistenten verwenden will, eingesprochen werden. Je nach Einsatzgebiet kann das ein Nachteil sein, denn das verursacht Aufwand bei der Installation.

## Text-To-Speech stimme ist künstlich
Die Stimme der verwendeten Text-To-Speech Implementierung ist sehr künstlich, denn sie wird auf Basis der Eingabephoneme synthetisiert. Teilweise ist es schwierig zu die Ausgabe zu verstehen, wenn man nicht weiß was genau gesprochen wird.
