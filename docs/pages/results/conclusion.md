---
title: Fazit
permalink: /results/conclusion/
subtitle: Fazit zur Implementierung
layout: page
show_sidebar: false
menubar: results_menu
---

# Fazit

## Kriterien

Für unser Fazit haben wir uns Kritierien überlegt, an welchen man die Praxistauglichkeit der Implementierung messen kann. Diese sind wie folgt:

| Kriterium                                        | Erläuterung                                                                                     |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| Bedienbarkeit                                    | Wie leicht ist der Sprachassistent zu bedienen?                                                 |
| Robustheit / Stabilität                          | Wie robust ist der Sprachassistent?                                                             |
| Datenschutz                                      | Wie steht es um den Datenschutz?                                                                |
| Erweiterbarkeit                                  | Ist der Sprachassistent in seinen Funktionen erweiterbar?                                       |
| Lizenz                                           | Bieten die Lizenzen Möglichkeiten zur Erweiterung?                                              |
| Zuverlässigkeit                                  | Wie zuverlässig erkennt der Sprachassistent die Befehle und werden diese richtig interpretiert? |
| Eignung für die Behinderten- und Erziehungshilfe | Ist der Assistent für den Einsatz geeignet?                                                     |
| Hardware                                         | Eignet sich die verwendete Hardware?                                                            |
| Sicherheit                                       | Wie steht es um die Sicherheit?                                                                 |
| Lernkurve                                        | Wie schnell kann sich ein neuer Entwickler zurechtfinden?                                       |
| Support                                          | Sind die verwendeten Dienste zukunftssicher?                                                    |

## Bedienbarkeit

Der Sprachassistent ist sehr einfach zu bedienen. Unser Wake-Word ist sehr zuverlässig genauso wie der verwendete Dienst. Der Speech-To-Text Dienst Pocketsphinx erkennt gesprochene Sätze und Wörter sehr gut - es kommt nur selten zu unerwünschten Ergebnissen.
Allerdings müssen wir durch unsere implementierte Hintergrundgeräuschreduzierung Abstriche in der Bedienbarkeit machen, denn eine Bedienung aus der Ferne oder auch leise Sprache könnte als Hintergrundgeräusch erkannt werden und schränkt die Bedienbarkeit ein. Auf der anderen Seite wiederum sollte eine Bedienung aus der Nähe um einiges zuverlässiger funktionieren.

## Robustheit / Stabilität

Während der Entwicklung ist kein Dienst abgestürzt und allgemein scheint Rhasspy über eine art "Monitoring" der einzelnen Dienste zu verfügen und würde etwaige nicht erreichbare Dienste neu starten. 
Unsere Docker-Umgebung ist ähnlich ausgelegt, wir verwenden die Restart-Policy `unless-stopped`, wodurch die Container nur dann beendet werden, wenn sie händisch gestoppt werden. Selbst bei einem Neustart des Raspberry Pis starten die Container wieder und es ist kein manuelles Starten nötig.

## Datenschutz

Der Sprachassistent läuft komplett Offline, es werden keine Daten über das Internet übertragen - auch wenn eine solche Implementierung prinzipiell möglich wäre. In unserer Implementierung erfolgt die gesamte Verarbeitung lokal auf dem Endgerät. Allerdings müssen für das Wake-Word einzelne Audioaufnahmen gespeichert werden, was eventuell Datenschutzrechtliche Konsequenzen haben könnte.
Das Dialoge-Management von Rhasspy garantiert, dass lediglich der Wake-Word Dienst permanent das Mikrofon "abhört". Alle anderen Dienste aktivieren sich erst bei der Erkennung des Wake-Words.

## Erweiterbarkeit

Durch Rhasspy zieht sich eine dezentrale Struktur, was viele Möglichkeiten zur Erweiterung bietet. Die Integration neuer Kommandos ist sehr leicht, vorrausgesetzt man hat sich in die verwendete Grammatik eingearbeitet und sich Gedanken über die mögliche Struktur der Sprachbefehle macht. Hier gibt es allerdings keine technologische Einschränkung.
Durch die Struktur der MQTT-Nachrichten sollte es auch gut möglich sein eigene Dienste zu entwickeln.

## Lizenz

Alle verwendeten Dienste stehen unter der MIT-Lizenz, sodass wirunsere Implementierung auch unter diese Lizenz stellen können. Die Lizenz ist sehr freizügung und ist somit kein Hindernis für die Verwendung.

## Zuverlässigkeit

Unser Wake-Word hat sich als sehr zuverlässig erweisen und ebenso Raven als Wake-Word Dienst. Auch Pocketsphinx hat sich als sehr zuverlässig erwiesen, denn hier werden nur definierte Befehle erkannt und erlaubt auch gewisse Fehlertoleranzen.
Durch unsere implementierte Hintergrundgeräuschreduzierung sollte eine Bedienung aus der Nähe um einiges zuverlässiger funktionieren.

## Eignung für die Behinderten- und Erziehungshilfe

Der Sprachassistent soll grundsätzlich für den Einsatz in der Behinderten- und Erziehungshilfe geeignet sein. Letzendlich müssen wir hier besonderes Augenmerk auf die Kommunikation mit dem Benutzer setzen.
Unser Wake-Word Service ist besonders geeignet, denn er basiert auf individuellen Sprachmustern der Benutzer, was auch etwaigen sprachbehinderten Nutzern ermöglicht den Assistenten aufzuwecken.
Der Text-To-Speech Dienst wiederum ist sehr schwer verständlich und klingt auch sehr unnatürlich. Dieser Dienst ist für den Einsatz nicht geeignet.
Zuletzt müsste man die Spracherkennung sowie das interpretieren des Befehls untersuchen. Hier sehen wir Grundsätzlich kein Problem für den Einsatz, insbesondere weil die Dienste lediglich die definierten Befehle erkennen und hier auch Fehlertoleranzen haben. 

## Hardware

Die uns zur Verfügng gestellte Hardware funktioniert für den Einsatz des Sprachassistenten gut. Möglicherweise würde ein Raspberry Pi 4 zur Beschleunigung des Speech-To-Text Services bessere Ergebnisse erzielen - allerdings ist die Bedienung auch mti dem Raspberry Pi 3 gut möglich.
Die Logitech Z120 Lautsprecher wiederum funktionieren überhaupt nicht gut: Hier liegt über den Audioausgang des Raspberry Pis ein extremes Rauschen an und die Sprachausgabe ist nahezu unverständlich. Andere Geräte wiederum funktionieren hier Störungsfrei.

## Sicherheit

In usnerer Implementierung haben wir den Faktor Sicherheit nicht intensiv behandelt - lediglich im Docker-Networking Port-Mapping betrieben.
Der MQTT-Broker ist von außerhalb erreichbar und eröffnet hier einen Angriffspunkt, denn man kann beliebige Nachrichten lesen und schreiben. Hier wäre ein notwendiger Schritt einen passwortgeschützten Zugang einzurichten.
Ähnlich sieht es bei Node-Red und Rhasspy aus. Die jeweiligen Web-Interfaces sind von außen erreichbar und lassen sich ohne Authentifizierung bedienen.
Zu guter letzt ist auch der gesamte Raspberry Pi mit den Standard-Zugangsdaten über SSH erreichbar - bevor man das System produktiv einsetzt sollte man hier also noch nacharbeiten.

## Lernkurve

Insgesamt haben wir die Entwicklung sehr positiv erfahren. Sobald man sich in die Service-Struktur von Rhasspy sowie dem Hermes-Protokoll eingearbeitet hat, fiel die Entwicklung sehr leicht und ging schnell von der Hand. Ebenso konnte man vieles durch Trial-and-Error ausprobieren ohne befürchten zu müssen, dass man einen Fehler produziert.

## Support

Grundsätzlich werden alle Dienste noch weiterentwickelt, allerdings arbeiten die Entwickler von Pocketsphinx an einer neue Bibliothek [Vosk](https://github.com/alphacep/vosk-api). Es ist möglich, dass hier in Zukunft der Support nachlassen wird.