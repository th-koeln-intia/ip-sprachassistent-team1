---
title: Troubleshooting
permalink: /docs/troubleshooting/
subtitle: Troubleshooting
layout: page
show_sidebar: false
menubar: docs_menu
---

## Bekannte Probleme und Lösungen

* **Meine Dokumentationsseite ist Lokal erreichbar, allerdings nicht wenn sie von GitHub deployt wird**

Der genaue Grund für dieses Verhalten ist unklar, es scheint mit relativen Links zusammenzuhängen. Gelöst werden kann das Problem auf jeden Fall, indem man für jede Dokumentationsseite einen Permalink anlegt. Das macht man folgendermaßen im Jekyll-Header:
```markdown
---
permalink: /link-to-site/
---
```
Jetzt kann die Seite problemlos über `https://ip-team1.intia.de/link-to-site` erreicht werden.

* **Ich bekomme trotz Touchlink Factory Reset die Lampe nicht mit zigbee2mqtt gekoppelt**

Abstand der Lampe zum ZigBee-Stick reduzieren (<10cm), Lampe einschalten und warten, bis sich diese "von selbst" meldet

* **Die Philips Hue Lampe hält sich nicht an das definierte Power-On-Verhalten**  

Laut einem [Reddit-Post](https://www.reddit.com/r/Hue/comments/aa3am0/so_the_power_on_behavior_is_not_working_like_i/) muss die Lampe jedes Mal für mindestens. 20 Sekunden eingeschaltet sein

* **Ich kann meine Node-Red Flows nicht importieren, es wird immer nur ein Node hinzugefügt**

Das liegt daran, dass fälschlicherweise nicht der gesamte Node-Red Flow exportiert wurde, sondern nur der einzelne Node. Sobald man einen Node auswählt und dann den Flow exportieren möchte wird standardmäßig nur der einzelne Node exportiert. Man sollte also darauf achten, dass "Aktueller Flow" ausgewählt ist.

![node-red_export](/assets/node-red_export.png)