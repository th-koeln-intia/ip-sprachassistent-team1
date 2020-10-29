---
title: Wecker
permalink: /docs/features/alarm
subtitle: Wer hat an der Uhr gedreht?
layout: page
show_sidebar: false
menubar: docs_menu
---

# Wecker ⏰

### Hinzufügen eigener Wecktöne

Neben den beiden mitgelieferten Wecktönen kann man selbstverständlich auch eigene Wecktöne installieren. Bei der Auswahl des Wecktons sollte man darauf achten, dass dieser nicht zu lang ist, da man den Wecker immer nur stoppen kann nachdem der Weckton komplett abgespielt wurde.

Damit man demnächst von seinem Lieblingssound geweckt wird, sind folgende Schritte nötig:

**1. Weckton hochladen**

Der gewünschte Weckton muss als .wav Datei vorliegen. Die Datei muss dann auf dem Raspberry im Projektordner unter src/api/assets/alarm_sounds abgelegt werden. Dabei empfehlen wir den Dateinamen in eine Zahl zwischen eins und 100 zu ändern.

```
📦ip-sprachassistent-team1
 ┣ 📂src
 ┃ ┣ 📂api
 ┃ ┃ ┣ 📂assets
 ┃ ┃ ┃ ┣ 📂alarm_sounds
 ┃ ┃ ┃ ┃ ┣ 🔊1.wav
 ┃ ┃ ┃ ┃ ┣ 🔊2.wav
 ┃ ┃ ┃ ┃ ┗ 🔊3.wav
```

**2. Intents bearbeiten**

Standardmäßig erkennt Deep Thought über die Spracherkennung nur die beiden Wecktöne "eins" und "zwei". Damit man nun auch den neu hinzugefügten Weckton einstellen kann, muss man den hinterlegten Dateinamen explizit in der [alarm.ini](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/rhasspy/profiles/de/intents/alarm.ini) angeben.

**Beispiel:** Wir haben die Datei 3.wav unter [src/api/assets/alarm_sounds](https://github.com/th-koeln-intia/ip-sprachassistent-team1/tree/master/src/api/assets/alarm_sounds) abgelegt. Dann sollte der ChangeAlarmSound Intent wie folgt abgeändert werden:

```ini
alarm_change_state = (setz | setze | änder | ändere | stell | stelle)
alarm_sound_alias = (Weckton | Alarmton | Weckerton)
<alarm_change_state> [den] <alarm_sound_alias> [auf] (1|2|3){alarm_sound!int}
```

Wenn man etwas experimentierfreudig ist, so kann man dem Weckton auch einen Namen geben, der dann auf die Zahl gemappt wird. Siehe [Rhasspy Doku](https://rhasspy.readthedocs.io/en/latest/training/#substitutions)

**Beispiel:** Die Datei heißt weiterhin `3.wav`, wir möchten diesen Weckton aber mit dem Befehl "Setze den Weckton auf Kindergeschrei" einstellen. Dann sieht der ChangeAlarmSound Intent so aus:

```ini
alarm_change_state = (setz | setze | änder | ändere | stell | stelle)
alarm_sound_alias = (Weckton | Alarmton | Weckerton)
<alarm_change_state> [den] <alarm_sound_alias> [auf] (1|2|Kindergeschrei:3){alarm_sound!int}
```