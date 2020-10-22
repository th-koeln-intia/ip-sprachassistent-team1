---
title: FAQ
permalink: /results/faq/
subtitle: Warum? Wieso? Weshalb?
layout: page
show_sidebar: false
menubar: results_menu
---

# Allgemein

# Entscheidungen im Entwicklungsprozess

* **Warum heißt der Sprachassistent Deep Thought?**

Dabei handelt es sich um den Computer aus dem Roman "Per Anhalter durch die Galaxis", der die Antwort "42" auf die Frage nach dem Sinn des Lebens berechnet ([Ausführliche Information](https://de.wikipedia.org/wiki/42_(Antwort))).
Einem Computer Fragen zu stellen respektive Anweisungen zu geben und daraufhin eine Antwort von diesem zu bekommen ist im Grunde das, was ein Sprachassistent tun soll. Zusätzlich bedeutet "Deep Thought" wörtlich übersetzt "tieferer Gedanke" - auch das fanden wir sehr passend, schließlich soll die Anweisung an den Sprachassistenten eine Intention des Benutzers umsetzen und daher haben wir uns für diesen Namen entschieden.

* **Warum habt ihr euch dazu entschieden, das GitHub Pages Theme zu wechseln und warum ausgerechnet bulma-clean-theme?**

Hauptargument für die Entscheidung das Theme zu wechseln ist den Dokumentationsaufwand zu verringern und gleichzeitig eine Struktur zu schaffen. Unser Ziel war es die Dokumentation auf mehrere Seiten aufzuteilen und eine Navigation zu ermöglichen. Es ist zwar Möglich das Ziel mit hauseigenen Mitteln von Jekyll umzusetzen, erforder allerdings eine Menge Aufwand.

Eine kurze Recherche hat gezeigt, dass sich eine Navigation über mehrere Seiten hinweg über Themes realisieren lässt.

Die Wahl auf [bulma-clean-theme](http://www.csrhymes.com/bulma-clean-theme/) fiel deshalb, weil das Theme zum einen die MIT-Lizenz verfolgt und zum Anderen sehr leicht ermöglicht die Dokumentation auf verschieden Dateien aufzuteilen. Anders als bei anderen Themes ist es hier nicht notwendig auf HTML-Dateien zu wechseln, es kann weiterhin mit Markdown-Dateien gearbeitet werden. Auch die Konfiguration der Menüs ist nicht so aufwendig wie bei anderen Themes.

* **Warum habt ihr ein Dockerfile `hermes-led` und warum ist dieses auf Docker Hub?**

Das Dockerfile `hermes-led` ist für die LED-Steuerung des ReSpeaker Mic-Array aus Docker heraus gedacht. Es schafft letzendlich eine Schnittstelle zwischen dem Treiber und MQTT. Das Image wurde auf Basis des folgenden [Issue](https://github.com/project-alice-assistant/HermesLedControl/issues/81) von [HermesLedControl](https://github.com/project-alice-assistant/HermesLedControl) erstellt und ein wenig optimiert um die Größe des Image zu verringern. 

Leider dauert es sehr lange das Image zu bauen, insbesondere auf dem Raspberry Pi, weshalb wir uns dazu entschlossen haben das fertige Image online zur Verfügung zu stellen. Als erstes dachten wir, dass man dafür [GitHub Packages](https://github.com/features/packages) nutzen könnte um das Image direkt auf unserem Repository zur Verfügung zu stellen. Leider ist es mit GitHub Packages derzeit noch nicht möglich das Image ohne sich in GitHub einzuloggen mit Docker zu verwenden. Weil wir das als nicht praktikabel erachtet haben, haben wir uns kurzerhand dazu entschlossen das Image auf [Docker Hub](https://hub.docker.com/r/thund/hermes-led) zur Verfügung zu stellen.