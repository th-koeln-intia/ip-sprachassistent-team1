---
title: Lichtsteuerung
permalink: /docs/features/light
subtitle: ...und es werde Licht
layout: page
show_sidebar: false
menubar: docs_menu
---

# 💡 Lichtsteuerung

### Erweiterung der Gruppen (Räume)

Sollten weitere Gruppen(Räume) über den Sprachassistenten angesteuert werden sollen und diese bereits nach [Konfigurieren der Gruppen](/getting-started/installation#konfigurieren-der-gruppen) definiert worden sein, dann muss für Rhasspy die Datei [profiles/de/slots/light_rooms](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/rhasspy/profiles/de/slots/light_rooms) angepasst werden. Das Format hier richtet sich nach der [Dokumentation von Rhasspy](https://rhasspy.readthedocs.io/en/latest/training/#sentencesini).

Wichtig ist hier, dass eine Substitution für das Attribut `room` auf den `friendly_name` der [groups.yml](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/zigbee2mqtt/data/groups.yaml) von Zigbee2MQTT durchgeführt wird um die entsprechende Gruppe anzusteuern.

Als Beispiel um den Sprachassistenten für die Steuerung der Gruppe `balcony` zu erweitern:

```
(Balkon | Terasse | Draussen){room:balcony}
```

Jetzt muss der Sprachassistent neu trainiert werden. Das geschiet entsprechend der [Anleitung](/getting-started/installation/#rhasspy-trainieren).

Die Gruppen sind jetzt einsatzbereit und können verwendet werden.