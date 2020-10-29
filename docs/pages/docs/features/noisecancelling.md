---
title: Hintergrundgeräuschreduzierung
permalink: /docs/features/noisecancelling
subtitle: Psss...ssst
layout: page
show_sidebar: false
menubar: docs_menu
---

# 🔊 Hintergrungeräuschreduzierung

Wir haben zum einen eine Hintergrundgeräuschreduzierung als Referenz implementiert und zum anderen weitere Möglichkeiten evaluiert (Siehe hierzu: [Ergebnisse Hintergrundgeräuschreduzierung](/results/noise-cancelling/)). Die derzeitige Lösung basiert auf Frequenzmodulation mit [SoX](http://sox.sourceforge.net/sox.html), wobei zum einen das Grundrauschen der Hardware entfernt wird und zum anderen ein Noise-Gate für etwaige Hintergrundgeräusche verwendet wird.

Eine Erweiterung sollte unter Berücksichtigung der Ergebnisse geschehen.

Unter Umständen ist es notwendig das Grundrauschen erneut aufzunehmen bzw. nicht das mitgelieferte Profil zu verwenden, wenn sich der Pi in einer anderen Umgebung befindet oder die Hardware erweitert/geändert wird. Dafür sind die folgenden Schritte notwendig:

Wir nehmen 10 Sekunden Grundrauschen auf - dabei sollte absolute Ruhe abseits des Grundrauschens sein und erstellen daraus ein Rauschprofil.
```sh
arecord -Dsysdefault:CARD=seeed4micvoicec -f S32_LE -r 16000 -c 4 -d 10 noise.wav
sox noise.wav -n noiseprof noise_sox.prof
```

Das daraus resultierende Rauschprofil legen wir jetzt in dem rhasspy-Ordner ab und ersetzen die bereits vorhandene Datei.

```
📦ip-sprachassistent-team1
 ┣ 📂docker
 ┃ ┣ 📂rhasspy
 ┃ ┃ ┗ 📜noise_sox.prof
```

Möglicherweise ist es jetzt noch notwendig den `amount` Parameter für den SoX Effekt `noisered` anzupassen, das ganze muss in der [profile.json](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/rhasspy/profiles/de/profile.json) unter `microphone.command.record_arguments` passieren.