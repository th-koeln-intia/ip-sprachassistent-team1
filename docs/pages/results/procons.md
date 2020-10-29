---
title: Vor- und Nachteile
permalink: /results/pros-and-cons/
subtitle: Warum sollte ich Deep Thought verwenden? Wann ist Deep Thought ungeeignet?
layout: page
show_sidebar: false
menubar: results_menu
---

# Vorteile

## Hintergrundgeräuschunterdrückung evaluiert und als PoC implementiert
Wir haben uns intensiv mit dem Thema Hintergrundgeräuschunterdrückung auseinandergesetzt, was alleine durch die Filterung des Grundrauschens in ein um einiges klareres Klangbild resultiert. Das unterstüzt unseren Speech-To-Text Service Pocketsphinx dabei die Sprachbefehle besser zu verstehen und zuverlässigere Ergebnisse zu liefern.
Wir haben unterschiedliche Möglichkeiten hierzu untersucht und zusammengefasst, was eine gute Grundlage zur Weiterentwicklung des Themas bietet. In unserer Referenzimplementierung ist es möglich den Sprachassistenten trotz etwaiger störender Geräusche im Hintergrund zuverlässig zu nutzen, wenn sich dieser in unmittelbarer Nähe des Nutzers befindet. Siehe hierzu: [Hintergrundgeräuschunterdrückung](/results/noise-cancelling/).

## Kann nicht von fremden Personen gesteuert werden
Da das Wake-Word über die Signatur des Audiosignals erkannt wird und nicht über speech-to-text, können fremde Personen den Sprachassistenten nicht steuern. Sollte ein weiterer Nutzer den Assistenten bedienen können, ist es leicht ein weiteres Wake-Word hinzuzufügen.

## Schnelle Konfiguration
Die einzelnen Services lassen sich ohne schnell konfigurieren und sind bereits nach einer kurzer Einarbeitungszeit erweiterbar.

# Nachteile

## Bedienung aus der Ferne nicht möglich
In unserer Referenzimplementierung der Hintergrundgeräuschunterdrückung ist es nicht möglich den Sprachassistenten aus einer großen Distanz zu bedienen, denn die Sprache wird unter Umständen als Hintergrundgeräusch wahrgenommen und herausgefiltert. Wir haben jedoch weitere Möglichkeiten aufgelistet, die als Grundlage zur Weiterentwicklung dienen können. Siehe hierzu: [Hintergrundgeräuschunterdrückung](/results/noise-cancelling/).

## Langsame Erkennung Speech-to-text
Die Spracherkennung ist auf dem Raspberry 3 relativ langsam, weshalb es sich dort empfiehlt die Erkennung auf einen [Server auszulagern](https://rhasspy.readthedocs.io/en/latest/speech-to-text/#remote-http-server). Auf dem Raspberry 4 ist die Spracherkennung schneller, weshalb man dort auf den extra Server verzichten könnte.

## Wake-Word muss für jede Person eingesprochen werden
Damit das Wake-Word erkannt wird, muss dieses von jeder Person, die den Sprachassistenten verwenden will, eingesprochen werden. Je nach Einsatzgebiet kann das ein Nachteil sein, denn das verursacht Aufwand bei der Installation.

## Text-To-Speech stimme ist künstlich
Die Stimme der verwendeten Text-To-Speech Implementierung ist sehr künstlich, denn sie wird auf Basis der Eingabephoneme synthetisiert. Teilweise ist es schwierig zu die Ausgabe zu verstehen, wenn man nicht weiß was genau gesprochen wird.
