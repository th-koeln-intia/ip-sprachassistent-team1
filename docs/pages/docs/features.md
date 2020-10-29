---
title: Features
permalink: /docs/features/
subtitle: Was kann Deep Thought im Detail und wie lässt sich Deep Thought erweitern?
layout: page
show_sidebar: false
menubar: docs_menu
---

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


