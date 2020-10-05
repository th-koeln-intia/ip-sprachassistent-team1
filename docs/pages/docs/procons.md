---
title: Vor- und Nachteile
permalink: /docs/pros-and-cons/
subtitle: Vor- und Nachteile
layout: page
show_sidebar: false
menubar: docs_menu
---

# Vorteile

## Schnelle Konfiguration
Die einzelnen Services ließen sich ohne große Probleme konfigurieren und einwandfrei miteinander verwenden.

# Nachteile

## Langsame Erkennung Wake-Word
Die Spracherkennung ist auf dem Raspberry 3 sehr langsam, weshalb es sich dort empfiehlt die Erkennung auf einen [Server auszulagern]("https://rhasspy.readthedocs.io/en/latest/speech-to-text/#remote-http-server"). Auf dem Raspberry 4 ist die Spracherkennung schneller, weshalb man dort auf den extra Server verzichten könnte.

## Wake-Word muss für jede Person eingesprochen werden (kann auch Vorteil sein)
Da das Wake-Word über die Signatur des Audiosignals erkannt wird und nicht über speech-to-text, muss das Wake-Word von jeder Person eingesprochen werden, die Zugriff auf den Assistenten haben soll.
