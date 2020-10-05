---
title: FAQ
permalink: /docs/faq/
subtitle: FAQ
layout: page
show_sidebar: false
menubar: docs_menu
---

# Allgemein

# Entscheidungen im Entwicklungsprozess

* **Warum habt ihr euch dazu entschieden, das GitHub Pages Theme zu wechseln und warum ausgerechnet bulma-clean-theme?**

Hauptargument für die Entscheidung das Theme zu wechseln ist den Dokumentationsaufwand zu verringern und gleichzeitig eine Struktur zu schaffen. Unser Ziel war es die Dokumentation auf mehrere Seiten aufzuteilen und eine Navigation zu ermöglichen. Es ist zwar Möglich das Ziel mit hauseigenen Mitteln von Jekyll umzusetzen, erforder allerdings eine Menge Aufwand.

Eine kurze Recherche hat gezeigt, dass sich eine Navigation über mehrere Seiten hinweg über Themes realisieren lässt.

Die Wahl auf [bulma-clean-theme](http://www.csrhymes.com/bulma-clean-theme/) fiel deshalb, weil das Theme zum einen die MIT-Lizenz verfolgt und zum Anderen sehr leicht ermöglicht die Dokumentation auf verschieden Dateien aufzuteilen. Anders als bei anderen Themes ist es hier nicht notwendig auf HTML-Dateien zu wechseln, es kann weiterhin mit Markdown-Dateien gearbeitet werden. Auch die Konfiguration der Menüs ist nicht so aufwendig wie bei anderen Themes.

* **Warum habt ihr ein Dockerfile `hermes-led` und warum ist dieses auf Docker Hub?**

Das Dockerfile `hermes-led` ist für die LED-Steuerung des ReSpeaker Mic-Array aus Docker heraus gedacht. Es schafft letzendlich eine Schnittstelle zwischen dem Treiber und MQTT. Das Image wurde auf Basis des folgenden [Issue](https://github.com/project-alice-assistant/HermesLedControl/issues/81) von [HermesLedControl](https://github.com/project-alice-assistant/HermesLedControl) erstellt und ein wenig optimiert um die Größe des Image zu verringern. 

Leider dauert es sehr lange das Image zu bauen, insbesondere auf dem Raspberry Pi, weshalb wir uns dazu entschlossen haben das fertige Image online zur Verfügung zu stellen. Als erstes dachten wir, dass man dafür [GitHub Packages](https://github.com/features/packages) nutzen könnte um das Image direkt auf unserem Repository zur Verfügung zu stellen. Leider ist es mit GitHub Packages derzeit noch nicht möglich das Image ohne sich in GitHub einzuloggen mit Docker zu verwenden. Weil wir das als nicht praktikabel erachtet haben, haben wir uns kurzerhand dazu entschlossen das Image auf [Docker Hub](https://hub.docker.com/r/thund/hermes-led) zur Verfügung zu stellen.

* **Warum habt ihr euch für dieses Wake-Word entschieden?**

Nach einer ausführlichen Recherche über Wake-Words (Siehe Kommentare im [Jira-Ticket](https://sprachassistenten.atlassian.net/browse/IP1-3), kamen für uns drei verschiedene Wake-Words in Frage. Diese waren "Asterix", "Obelix" und "Pixie". Leider wurde unser Favorit "Obelix" von der Spracherkennung sehr schlecht erkannt. Man musste das Wort sehr laut und deutlich sagen, damit es überhaupt erkannt wurde. Mit "Pixie" hatten wir das Gegenteilige Problem, da das gesprochene "P" keine starken Signaturen in der Sprachaufnahme erzeugt und das "i" dadurch so dominant wurde, dass jedes Wort mit der Endung "i" als Wake-Word erkannt wurde. Diesen Fehler konnten wir leicht beheben, indem wir den Anfang des Wortes markanter gestalteten. So entstand das Wort Trixie. Dieses war jedoch weiterhin sehr anfällig für false positives. Deshalb entschieden wir uns dazu noch ein "Hey, " vor das Wake-Word zu packen. Mit dieser Kombination ging die Anzahl der falschen Aktivierungen stark zurück und wir erhielten ein zufriedenstellendes Ergebnis.