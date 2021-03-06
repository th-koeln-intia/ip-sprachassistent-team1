---
title: Troubleshooting
permalink: /docs/troubleshooting/
subtitle: Ich bin bei der Verwendung bzw. der Weiterentwicklung von Deep Thought auf ein Problem gestoßen - wie behebe ich das?
layout: page
show_sidebar: false
menubar: docs_menu
---

# Bekannte Probleme und Lösungen

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

* **Wenn ich die `profile.json` von Rhasspy bearbeite, wird diese auch nach einem Neustart nicht verwendet**
  
Rhasspy ist was das angeht ziemlich frickelig. Aus der [profile.json](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/rhasspy/profiles/de/profile.json) wird eine [supervisord.conf](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/rhasspy/profiles/de/supervisord.conf) und eine [docker-compose.yml](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/rhasspy/profiles/de/docker-compose.yml) Datei erstellt, die daraufhin Rhasspy als Konfiguration dienen. Das passiert allerdings nicht nach einem neustart, sondern nur dann, wenn man im Web Interface in den Einstellungen "Save Settings" drückt.
Zur Lösung genügt es also sich in das Web-Interface von Rhasspy einzuloggen und unter den Einstellungen den Button "Save Settings" zu drücken.

* **Ich kann meine Node-Red Flows nicht importieren, es wird immer nur ein Node hinzugefügt**

Das liegt daran, dass fälschlicherweise nicht der gesamte Node-Red Flow exportiert wurde, sondern nur der einzelne Node. Sobald man einen Node auswählt und dann den Flow exportieren möchte wird standardmäßig nur der einzelne Node exportiert. Man sollte also darauf achten, dass "Aktueller Flow" ausgewählt ist.

![node-red_export](/assets/node-red_export.png)

* **Mein Wake-Word funktioniert nicht**

Eine mögliche Ursache ist, dass der Einstellungswert `minimum_matches` nicht auf 1 gesetzt ist. Wenn dieser höher gewählt es, resultiert das in folgender Meldung und das Wake-Word kann aus einem unbekannten Grund nicht erkannt werden:

```
rhasspy        | [DEBUG:2020-09-29 08:56:29,593] rhasspy-wake-raven: Enter refractory for 2.0 second(s)
rhasspy        | [DEBUG:2020-09-29 08:56:31,795] rhasspy-wake-raven: Exiting refractory period
```

* **Ich habe eine enorme Verzögerung meiner Sprachbefehle oder diese erhalten einen Timeout**

Es könnte sich hierbei um einen Fehler der Verarbeitung des Audio-Signals handeln.
Die Integration in Rhasspy funktioniert nur mit einer Sampling-Rate von 16000 Hz und einem Channel. Grund dafür ist, dass der Dienst [rhasspy-silence](#rhasspy-silence) auf [wbrtcvad](https://github.com/wiseman/py-webrtcvad) basiert, welches zwingend ein Mono-Signal voraussetzt. Theoretisch sollte zumindest eine andere Sampling-Rate möglich sein, denn wbrtcvad unterstützt nach eigener Aussage auch Sampling-Raten von 8000 Hz, 32000 Hz und 48000 Hz. Rhasspy arbeitet intern allerdings standardmäßig mit 16000 Hz und eine Parametrisierung des Werts ist nicht möglich, solange man keine eigene Instanz der entsprechenden Dienste aufsetzt.
Dass Rhasspy mit einer anderen Abtastrate bzw. anderer Anzahl Kanälen nicht zurecht kommt, scheint ein Bug zu sein, denn eigentlich sollte das Signal entsprechend für rhasspy-silence [konvertiert](https://github.com/rhasspy/rhasspy-microphone-cli-hermes/blob/master/rhasspymicrophone_cli_hermes/__init__.py#L173) werden.

* **Nach einem Neustart braucht der Assistent lange um den ersten Sprachbefehl zu verarbeiten**

Wenn unser Speech-To-Text Dienst das erste mal nach einem Start verwendet wird, dauert die Initaliserung dieses relativ lange. Künftige Sprachbefehle werden allerdings schneller verarbeitet. Es ist möglich den Dienst auf einen [Server mit besserer Leistung auszulagern](https://rhasspy.readthedocs.io/en/latest/speech-to-text/#remote-http-server) und somit die Initaliserungszeit und die Erkennungszeit zu verringern.

* **Warum klappt das publishen von tts über Python an Hermes nicht?**

Es könnte sich hierbei um einen kleinen Syntaxfehler innerhalb des JSONS handeln. Beispielsweise trat das Problem bei uns bei folgendem Code auf:

```python
publish.single("hermes/tts/say", "{'text': 'Okay'}", hostname="mosquitto") 
```

Hier lag das Problem daran, dass Strings in JSON immer mit einem " gekennzeichnet sein müssen anstatt eines '.
Der funktionierende Code sah dann also so aus:

```python
publish.single("hermes/tts/say", '{"text": "Okay"}', hostname="mosquitto")
```