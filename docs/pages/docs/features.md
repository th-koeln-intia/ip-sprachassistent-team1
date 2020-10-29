---
title: Features
permalink: /docs/features/
subtitle: Was kann Deep Thought im Detail und wie lässt sich Deep Thought erweitern?
layout: page
show_sidebar: false
menubar: docs_menu
---

In den folgenden Abschnitten beschreiben wir was Deep Thought kann und wie die einzelnen Komponenten angepasst bzw. erweitert werden können.

# 📖 Inhaltsverzeichnis

| Thema                                                       | Beschreibung                                                 |
| ----------------------------------------------------------- | ------------------------------------------------------------ |
| [Wake Word](/docs/features/wake-word/)                      | Das Aktivierungswort des Sprachassistenten                   |
| [Lichtsteuerung](/docs/features/light/)                     | Lichtsteuerung, die mit Deep Thought vorgenommen werden kann |
| [Wecker](/docs/features/alarm/)                             | Wecker stellen mit Deep Thought                              |
| [Hintergrungeräuschreduzierung](/docs/features/noise-cancelling/) | Filtern von Hintergrundgeräuschen                            |
| [API](/docs/features/api/)                                        | Die entwickelte API                                          |
































//TODO Ist das Kunst oder kann das weg?
## Node-Red Flows

In der Bibliothek von Node-Red sind unterschiedliche Flows vorhanden, die eingesetzt werden können.
Die Flows stellen eine exklusive Auswahl da, das bedeutet, dass nur entweder `LightAPIFlow` **oder** `LightAPIFlow_Raw` **oder** `ChangeLightBrightness.json`, `ChangeLightColor.json` und `SwitchLight.json` verwendet werden sollen.

### `LightAPIFlow.json`

Dieser Flow implementiert die Lichtsteuerung über die API [/lights/set](#lightsset). Der Request Body wird über JavaScript-Funktionsblöcke erstellt und an die API übergeben.

### `LightsAPIFlow_Raw.json`

Dieser Flow implementiert die Lichtsteuerung über die API [/lights/set/raw](#lightssetraw). Der Request Body aus Rhasspy wird direkt an die API übergeben, die Logik liegt komplett innerhalb der API. 

### `ChangeLightBrightness.json` / `ChangeLightColor.json` / `SwitchLight.json`

Diese drei Flows sollten nur dann aktiv sein, wenn die API nicht verwendet werden soll. Hier liegt die gesamte Logik in Node-Red, die über JavaScript-Funktionsblöcke implementiert wird.


# 🗣 Text To Speech

Wir haben Text-To-Speech.
//TODO

# 📝 Speech To Text

Wir verwenden [Pocketsphinx](https://rhasspy.readthedocs.io/en/latest/speech-to-text/#pocketsphinx) als Speech-To-Text Dienst.

//TODO

# 🕹 Intent Recognition

Wir haben eine Intent Recognition.
//TODO


