---
title: Vor- und Nachteile
permalink: /docs/pros-and-cons/
subtitle: Warum sollte ich Deep Thought verwenden? Wann ist Deep Thought ungeeignet?
layout: page
show_sidebar: false
menubar: docs_menu
---

# Vorteile

## Kann nicht von fremden Personen gesteuert werden
Da das Wake-Word über die Signatur des Audiosignals erkannt wird und nicht über speech-to-text, können fremde Personen den Sprachassistenten nicht steuern.

## Schnelle Konfiguration
Die einzelnen Services ließen sich ohne große Probleme konfigurieren und einwandfrei miteinander verwenden.

# Nachteile

## Langsame Erkennung Speech-to-text
Die Spracherkennung ist auf dem Raspberry 3 sehr langsam, weshalb es sich dort empfiehlt die Erkennung auf einen [Server auszulagern](https://rhasspy.readthedocs.io/en/latest/speech-to-text/#remote-http-server). Auf dem Raspberry 4 ist die Spracherkennung schneller, weshalb man dort auf den extra Server verzichten könnte.

## Wake-Word muss für jede Person eingesprochen werden
Damit das Wake-Word erkannt wird, muss dieses von jeder Person, die den Sprachassistenten verwenden will, eingesprochen werden.
