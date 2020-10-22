---
title: Speech-To-Text
permalink: /results/speech-to-text/
subtitle: Entwicklungsergebnisse zur Implementierung des Speech-To-Text Services
layout: page
show_sidebar: false
menubar: results_menu
---

# 📝 Speech To Text

Wir verwenden [Pocketsphinx](https://rhasspy.readthedocs.io/en/latest/speech-to-text/#pocketsphinx) als Speech-To-Text Dienst.

## Einrichtung

Beim ersten Start wird ein Download eines von vortrainierten akustischen Modells sowie Wörterbuch benötigt.
Es handelt sich dabei um die [CMU Sphinx](https://sourceforge.net/projects/cmusphinx/) Datenbank.
Ein eigenes Training ist hier erstmal nicht sinnvoll was aus der 
[Dokumentation](https://cmusphinx.github.io/wiki/tutorialam/) auch hervorgeht, denn wir haben weder genügend Zeit noch 
genug Daten dafür.

## Technische Schwierigkeiten

Das Speech-To-Text-System ist hierbei auf dem Raspberry Pi ziemlich langsam - es ist allerdings möglich die Aufgabe auf
ein leistungsstärkeres System zu übertragen. Besonders beim Language Model Mixing (siehe nächsten Abschnitt) ist die Hardware des Rhaspberry zu schwach und es wird ausdrücklich empfohlen die Berechnung über einen Server laufen zu lassen.

Es geht nicht aus der Dokumentation hervor, allerdings müssen für Pocketsphinx die Intents (`sentences.ini`) gepflegt 
sein, weil aus dieser ein Sprachmodell erstellt wird. Das bedeutet es können noch so viele Wörter im Wörterbuch stehen, 
Pocketsphinx erkennt standardmäßig nur die Satzbestandteile, die auch in der `sentences.ini` stehen, selbst wenn auf der 
remote-Instanz bloß der Speech-To-Text Dienst läuft. Dieses Verhalten kann man abändern, indem man den Wert `mix_weight` bei PocketSphinx erhöht.
Je höher dieser Wert ist, desto mehr wird die `sentences.ini` mit dem language Model von PocketSphinx vermischt und es werden auch Wörter erkannt, die nicht in der `sentences.ini` eingetragen wurden. Aufgrund der Größe des mitgelieferten Language Models nimmt die Spracherkennung mit einem mix_weight > 0 sehr viel mehr Rechenkapazität in Anspruch.