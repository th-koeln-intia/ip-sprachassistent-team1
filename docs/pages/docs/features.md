---
title: Features
permalink: /docs/features/
subtitle: Features
layout: page
show_sidebar: false
menubar: docs_menu
---

# 📖 Inhaltsverzeichnis

| Feature                                                          | Beschreibung                                                                         | Status |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------ |
| [Wake Word](#-wake-word)                                         | Das Aktivierungswort des Sprachassistenten                                           | ✅     |
| [Hintergrungeräuschreduzierung](#-hintergrungeräuschreduzierung) | Prozess zur Eruierung einer geeigneten Technik zum Filtern von Hintergrundgeräuschen | ⭕     |
| [Lichtsteuerung](#-lichtsteuerung)                               | Die Steuerung einer Zigbee-fähigen Lichtquelle mit dem Sprachassistenten             | ✅    |
| [Text-To-Speech](#-text-to-speech)                               | Der Prozess zur Anpassung der Text-To-Speech-Engine espeak                           | ✅     |
| [Speech-To-Text](#-speech-to-text)                               | Entwicklungsdokumentation zur Verwendung von Pocketsphinx                            | ✅     |
| [Intent Recognition](#-intent-recognition)                       | Entwicklungsdokumentation zur Verwendung von Fsticuffs                               | WIP    |
| [API](#-api)                                                     | Dokumentation der entwickelten API                                                   | WIP    |

# 🎙 Wake Word

Das Wake Word oder auch Hot Word bzw. Aktivierungswort ist das wort, welches den Sprachassistenten Deep Thought aktiviert. Das Wake Word ist durch den Nutzer festzulegen und muss eingesprochen werden.

## Faktoren

Ein ideales Wake Word soll

1. Einfach sein
2. Klar verständlich sein
3. Verlässlich sein
4. Differenzierbar sein

## Marktanalyse

Es existieren diverse Sprachassistenten mit unterschiedlichen Wake Words auf den Markt. In der folgenden Tabelle sind die gängigen aufgelistet:

| Sprachassistent                | Wake Word                                                   |
| ------------------------------ | ----------------------------------------------------------- |
| Alexa                          | "Alexa" <br /> "Amazon" <br /> "Computer" <br /> "Echo"     |
| Google Assistent               | "Hey, Google" <br /> "Okay, Google"                         |
| Siri                           | "Hey, Siri"                                                 |
| Bixby                          | "Hey, Bixbi"                                                |
| Cortana                        | "Hey, Cortana"                                              |
| Hallo Magenta                  | "Hallo, Magenta" <br /> "Hey, Magenta" <br /> "Hi, Magenta" |
| Intelligent Personal Assistent | "Hey, BMW"                                                  |
| MBUX                           | "Hey, Mercedes"                                             |
| Jasper                         | "Jasper"                                                    |
| Snips                          | "Hey, Snips"                                                |

Es scheint üblich zu sein das Wake word mit einer Begrüßung zu verbinden - möglicherweise werden so falsch positive erkennungen, wenn der Name beiläufig im Alltag erwähnt wird unterbunden. Das wird auch durch den folgenden [Artikel](https://picovoice.ai/tips/choosing-a-wake-word/) bestätigt.

> A short wake word can can be made more effective by prepending it with e.g. "Hey", or "OK". These prefixes also can also help make it unambiguous that the wake phrase was intended to be triggered, and not simply a part regular speech that accidentally matched the wake phrase.

Was wiederum auffällig ist, dass Amazon mit ihrem Wake Word "Alexa" keine Begrüßung bzw. Präfix verwenden, was die Frage aufwirft ob es eine Besonderheit mit dem Namen gibt. Ein [Artikel](https://www.businessinsider.com/why-amazon-called-it-alexa-2016-7?r=DE&IR=T) verrät, dass die Entwickler beim Testprozess herausgefunden haben, dass die weichen Vokale sowie das 'x' die Erkennung in positiver Hinsicht unterstützen.

## Prozess zur Suche eines geeigneten Wake Words

Um ein geeignetes Wake Word zu finden, ist es zunächst nicht verkehrt zu definieren wie alltagstauglich das Wort ist. Wir beschränken uns hier auf den Kontext deutscher Sprache.

Das Wort sollte möglichst eindeutig sein - um Wörter mit ähnlichem Aufbau zu finden, bietet sich das digitale Wörterbuch [DWDS](https://www.dwds.de/) an. Hier kann man durch eine mächtige [Korpussuche](https://www.dwds.de/d/korpussuche) nach ähnlichen Wörtern suchen. Beispielsweise findet eine suche nach `*aus` alle Wörter, die auf `-aus` enden.

Um die phonetische eindeutigkeit zu prüfen bieten sich auch Suchmaschinen, die Reime für ein gegebenes Wort suchen, wie z.B. [rhyme](https://www.d-rhyme.de/), [Reimemaschine.de](https://www.reimemaschine.de/) oder [Woxikon](https://reime.woxikon.de/ger/finden.php) an.

Jetzt beginnt der schwierige Prozess: Das Suchen geeigneter Wörter. Die folgenden Wörter sind während des Prozesses in die engere Auswahl gekommen.

1. **Obelix** <br />
   Ein bekannter Comiccharakter aus den Comics "Asterix". Der Vorteil dieses Namens liegt in seiner Personifizierung, die Gespräche mit dem Sprachassistenten persönlicher machen sowie seine phonetische Eindeutigkeit. So existieren nahezu keine Wörter mit ähnlicher Endung - lediglich "-helix", was kein wirklich alltagsgebräuchlicher Begriff ist.
   Genauso existiert kein Reim mit gleicher Silbenanzahl, allerdings dafür die Wörter `nix`, `fix` und `nichts`, die hier problematisch werden könnten.
   <br />
   
2. **Pixie** <br />
    Auch hier liegt eine Personifizierung vor.
    Die phoentische Eindeutigkeit ist hier allerdings etwas schwieriger und umfangreicher zu bestimmen, weil die Endung `-ixie` auf unterschiedliche Weisen geschrieben wie `-ichsi`, `-iksi`, `-iksy`, `-igsi` in der Aussprache identisch oder gleich sind.
    <br />
    
3. **Kassandra** <br />
    Auch hier liegt eine Personifizierung vor.
    Der Gedanke hierbei ist, dass die Spracherkennung dieses Wort durch die deutliche Aussprache des `Kass` besser erkennt, auch wenn die Endung viele ähnliche Wörter suggerieren könnte.
    <br />
    
4. **Miriam** <br />
    Auch hier wieder Personifizierung
    Es gibt überraschend wenig Wörter, die auf `-iam` enden, vielleicht ist das ein Ansatz.

## Test der Wake Words

Um die Wake Words zu testen werden diese in Rhasspy eingesprochen. Die folgende Konfiguration wird hierfür angewendet:

```json
"wake": {
    "raven": {
    "keywords": {
            "default": {},
            "kassandra": {},
            "pixie": {},
            "obelix": {},
            "miriam": {}
        },
        "minimum_matches": "1",
        "probability_threshold": "0.5",
        "vad_sensitivity": "1"
    },
    "system": "raven"
}
```

Hierbei haben sich für die Wake Words folgendes ergeben:

1. **Obelix** <br />
Das Wake Word `Obelix` hat sich in der Konfiguration nicht als Wake Word geeignet. Beim Test lies es sich nahezu 
einfacher durch die Kombinationen `oben nichts` bzw `oben nix` auslösen als durch die Aussprache von `Obelix`. 
Desweiteren hat sich beim Test gezeigt, dass man bei dem Wort dazu verleitet wird es in einer höheren Geschwindigkeit 
auszusprechen, was je nach Training unterschiedliche resultate haben kann.
<br /> 

2. **Pixie** <br />
Das Wake Word `Pixie` hat sich bei dem Test sehr gut geschlagen und konnte sehr genau erkannt werden. Selbst eine 
undeutliche, genuschelte Aussprache oder eine Aussprache mit Pullover vor dem Mund konnte erkannt werden. Es hat sich 
allerdings gezeigt, dass Rhasspy Raven sehr stark auf die Endung `-ixie` fokussiert ist und diese schon zur Aktivierung 
ausreicht. Auch ein höherer `probability_thereshold` Wert zeigt hier keine Abhilfe. Es wird auch auf Phrasen wie 
`Schick sie` reagiert.
<br />

3. **Kassandra** <br />
Das Wake Word `Kassandra` eignet sich in der Konfiguration nicht als Wake Word. Beim Test hat sich gezeigt, dass die 
Aussprache jedes mal leicht unterschiedlich ist und es stark davon abhängig ist wie "hart" man das doppel-s ausspricht 
bzw. betont. Selbst mit einem geringen `probability_thereshold` Wert von `0.1` ist es immer noch schwierig den 
Sprachassistenten mit unterschiedlichen Aussprachen zu aktivieren.
<br />

4. **Miriam** <br />
`Miriam` hat sich auch als sehr zuverlässig erwiesen. Der Konsonant `r` hilft bei der Differenzierung zwischen Wörtern 
wie `Amsterdamm`, `Kilogramm`, `Potsdam` oder einfach bloß `Iam`. Allerdings ist der Name Miriam weit vertreten und 
könnte eine richtig negative Aktivierung hervorrufen.
<br />

5. **Trixie** <br />
Während einem Meeting im Discord ist aufgefallen, dass sich Rhasspy oft aktiviert hat - das Wake Word `Pixie` reagiert 
scheinbar auch auf Phrasen wie `Irgendwie` oder Ähnliches.
Als Abhilfe wurde das Wake Word `Trixie` verwendet, welches aufgrund des markanten `r`-Lauts bessere Ergebnisse erzielt 
hat.  

## Fazit zum Wake Word

Unsere Empfehlung für das Wake Word lautet `Hey, Trixie` mit der folgenden Konfiguration:

```json
{
  "minimum_matches": "1",
  "probability_threshold": "0.58"
}
```

## Sonstige Bemerkungen

Wenn ein höherer Wert für `minimum_matches` gewählt wird, resultiert das in folgende Meldung und ermöglicht keine Aktivierung mehr:

```
rhasspy        | [DEBUG:2020-09-29 08:56:29,593] rhasspy-wake-raven: Enter refractory for 2.0 second(s)
rhasspy        | [DEBUG:2020-09-29 08:56:31,795] rhasspy-wake-raven: Exiting refractory period
```

# 🔊 Hintergrungeräuschreduzierung

Während des Testens hat sich gezeigt, dass das Mikrofon sehr empfindlich ist was Hintergrundgeräusche wie einen Fernseher angeht. Es wird versucht aus der Sprache im Hintergrund einen Intent zu ziehen. 

Im Folgenden wird der Prozess zur Suche einer geeigneten Möglichkeit zur Reduzierung der Störgeräusche beschrieben.

## Was ist als Störgeräusche / Hintergrundgeräusch zu bewerten?

* Störgeräusche der Hardware
  * Grundrauschen
  * Geräusche der Hardware
* Hintergrundgeräusche
  * Bspw. Vogelgezwitscher, schreiendes Kind, Musik
  * Menschliche Unterhaltungen 

## Analyse der Störgeräusche

Im Folgenden sind einige Beispiele zu Störgeräuschen inkl. Soundsample zu finden.
Fürs Protokoll: Die Geräusche wurden mit folgendem Befehl aufgezeichnet: `arecord -Dsysdefault:CARD=seeed4micvoicec -f S32_LE -r 16000 -c 4`

| Störgeräusch                      | Vorhanden? | Beispielsound                                    |
| --------------------------------- | ---------- | ------------------------------------------------ |
| Grundrauschen                     | ✅          | [Sound](/assets/grundrauschen.wav)               |
| Tastaturtippen (< 1m)             | ✅          | [Sound](/assets/tippen.wav)                      |
| Fernsehr (5-7m, laut)             | ✅          | [Sound](/assets/fernseher_laut.wav)              |
| Fernsehr (5-7m, zimmerlautstärke) | ✅          | [Sound](/assets/fernseher_zimmerlautstaerke.wav) |
| Musik (< 1m, zimmerlautstärke)    | ✅          | [Sound](/assets/musik_zimmerlautstaerke.wav)     |
| Musik (< 1m, laut)                | ✅          | [Sound](/assets/musik_laut.wav)                  |

## Bestandsaufnahme der Möglichkeiten

Rhasspy hat hierzu keine geeignete eigene Funktion und da das Mikrofon permanent das Audiosignal als MQTT Nachricht übermittelt ist notwendig sich direkt auf den Audiotreiber bzw. auf das verwendete Tool zu konzentrieren.

Rhasspy bietet da von Haus aus die Möglichkeiten [arecord](https://alsa-project.org/wiki/Main_Page) und [pyaudio](https://pypi.org/project/PyAudio/) zusätzlich gibt es die Möglichkeit die Audioaufnahme über ein lokales Command zu machen sowie eine HTTP API zu verwenden. Es ist also möglich weitere Tools zu verwenden. 

Wie bereits im [Tech-Stack](/docs/tech-stack/#pocketsphinx) erwähnt, wäre ein eigenes Training des Sprachmodells nicht sinnvoll und läge nicht im Rahmen der Möglichkeiten. Desweiteren sehen wir es als Vorteil an, wenn jeder Nutzer gleichbehandelt wird und die Möglichkeit hat Deep Thought zu benutzen ohne ein eigenes Training zu erfahren. Das reduziert auch den Aufwand, der bei der Erstinstallation aufgebracht werden müsste.

Problematisch hierbei ist es vermutlich ohne ein Sprachmustertraining eine adäquate Lösung zu finden, die auch Hintergrundgeräusche mit Sprache - wie z.B. den Fernseher - herausfiltert. 

## Marktanalyse

Welche weiteren Tools gibt es, die die Möglichkeit bieten Hintergrundgeräusche zu reduzieren
* [SoX](http://sox.sourceforge.net/)
* [krisp](https://krisp.ai/de/)
* [PulseAudio](https://www.freedesktop.org/wiki/Software/PulseAudio/)

## Analyse der einzelnen Tools

### arecord

Leider bietet Rhasspy nicht die Möglichkeit die Parameter anzupassen bzw. ist das ganze sehr schlecht dokumentiert. Daher verwenden wir im Folgenden nicht das mitglieferte `arcord` von Rhasspy, sondern weichen auf ein `Local Command` aus. Die Folgende Konfiguration in der `profile.json` ist äquivalent zu der mitgelieferten.

```json
"microphone": {
    "arecord": {
        "device": "default:CARD=seeed4micvoicec"
    },
    "command": {
        "list_arguments": [],
        "sample_rate": 16000,
        "sample_width": 2,
        "channels": 1,
        "list_program": "arecord -L",
        "record_arguments": [],
        "record_program": "arecord -q -r 16000 -f S16_LE -c 1 -t raw -D default:CARD=seeed4micvoicec",
        "test_arguments": [],
        "test_program": "arecord -q -D {} -r 16000 -f S16_LE -c 1 -t raw"
    },
    "system": "command"
}
```

Jetzt können die Parameter auch selbst angepasst werden. Leider bietet `arecord` hier keine weiteren Möglichkeiten zur Filterung. 

### Pyaudio

Genauso wie bei [arecord](#arecord) bietet Rhasspy nicht gerade zugängliche Möglichkeiten die Parameter einzustellen. Man müsste hier also auch auf ein local command ausweichen. PyAudio bietet allerdings auch keine weiteren Möglichkeiten zur Filterung.

### krisp

[Krisp](https://krisp.ai/de/) ist eine kommerzielle Lösung, die zuverlässig auf Basis von künstlicher Intelligenz und mit jeder erdenklichen Hardware funktionieren soll. Die Lösung fällt leider sehr schnell raus denn es handelt sich hierbei erstens nicht um eine Open-Source Lösung, die dem Ansatz dieses Projekts widersprechen würde und zweitens sind - selbst wenn man über den letzten Punkt hinwegschauen würde - in der kostenlosen Version lediglich 120min/Woche möglich. Das ist insbesondere insofern problematisch, als dass das Mikrofon nach dem [Hermes-Protokoll](https://docs.snips.ai/reference/hermes) die Daten permanent in ein MQTT-Topic published. Es ist also die unbegrenzte Version von Nöten.

### SoX

[SoX](http://sox.sourceforge.net/) ist ein mächtiges Tool zur Audiobearbeitung, was viele Funktionen zur Frequenzmodulation bietet.
Mit SoX ist es möglich die normalen Hintergrundgeräusche herauszufiltern. Dazu wird das Grundrauschen aufgenommen und und ein sogenanntes Rauschprofil davon angelegt. Über die Funktion `noisered` kann SoX dann einen Audioeingang so modulieren, dass dieses Grundrauschen herausgefiltert wird.
Die Methode ist nur für das Grundrauschen praktikabel und ermöglicht keine tiefergreifende Filterung.
Zusätzlich ist es mit dem Tool möglich diverse weitere Effekte zur Frequenzmodulation anzuwenden.

### PulseAudio

Ähnlich wie [SoX](#sox) bietet [PulseAudio](https://www.freedesktop.org/wiki/Software/PulseAudio/) lediglich die Möglichkeit statische Hintergrundgeräusche herauszufiltern sowie eine Anpassung von Schwellwerten. 
Dazu kann mit PulseAudio ein Modul namens `module-echo-cancel` verwendet werden. Dieses Modul basiert anders als SoX nicht auf einer Beispieldatei, sondern wird über eine Reihe von [Parametern](https://wiki.archlinux.org/index.php/PulseAudio/Troubleshooting#Enable_Echo/Noise-Cancellation) gesteuert.

### Weitere Möglichkeiten auf Basis von AI/KI/NN

Zu dem Thema existiert eine [Publizierung](https://www.researchgate.net/publication/282446599_Removing_Noise_from_Speech_Signals_Using_Different_Approaches_of_Artificial_Neural_Networks) ("Removing Noise from Speech Signals Using Different Approaches of Artificial Neural Networks", Omaima Al-Allaf, 2015, University of Jordan, 10.5815/ijitcs.2015.07.02) welche weitere Möglichkeiten zur reduzierung von Hintergrundgeräuschen behandelt, die auf Basis künstlicher Intelligenzen agieren. 

### Fazit der Analyse

Es ist schwierig hier eine befriedigende Lösung für alle Use-Cases und Anforderungen zu finden. 

Als Beispiel macht es nur Sinn einen hohen Schwellwert für die Audioaufnahme bzw. Mikrofonaktivierung zu wählen, wenn der Sprachassistent nahe am Benutzer steht bzw. man davon ausgehen kann, dass dieser in einer bestimmten Lautstärke sprechen wird. Dieser Wert müsste für die beste User Experience pro Benutzer festgelegt werden und fest im System verankert sein, sodass die Bedienung des Sprachassistenten nur von einem einzigen Benutzer sinnvoll möglich wäre. 

Das Filtern des Grundrauschens ist prinzipiell möglich, resultiert allerdings lediglich in einer klareren Audioqualität. Weitere Störgeräusche sind hiervon nicht betroffen. Sinnvoll ist es vermutlich trotzdem, denn der Speech-To-Text Service könnte so zuverlässiger und robuster werden.

Das angesprochene Sprachmustertraining ist grundsätzlich die sinnvollste Lösung, denn so ist es möglich die Sprache des Benutzers zu erkennen und nur auf dessen Anweisungen zu reagieren. Genauso könnte hier erkannt werden, wann genau der Benutzer aufhört zu sprechen und was genau er gesagt hat, sodass Störgeräusche eines Fernsehers kein Problem darstellen sollten. Wie bereits angesprochen fehlen uns hierzu allerdings die technischen Möglichkeiten, Trainingsdaten und vor allem die Zeit. Auch ist die Lösung nicht sinnvoll, wenn das Gerät ohne weiteren Konfigurationsaufwand schnell für viele unterschiedliche Benutzer einsatzbereit sein soll.

Wir werden uns somit auf das Filtern des Grundrauschens sowie eine etwaige minimale Anpassung der Schwellwerte und weiterer Parameter mit SoX und arecord/ALSA beschränken. Das ganze müssen wir auch fortlaufend unter unterschiedlichen Bedinungen testen und ggf. anpassen.

## Experimentelle Implementierung von SoX in Verbindung mit arecord

SoX installieren:

```sh
sudo apt install sox
```

### Schritt 1: Grundrauschen filtern

10 Sekunden Grundrauschen aufzeichnen. Für die experimentelle Implementierung haben wir im gleichen Schritt noch eine Test-Sprachaufnahme gemacht:

```sh
 arecord -Dsysdefault:CARD=seeed4micvoicec -f S32_LE -r 16000 -c 4 -d 10 noise.wav
 arecord -Dsysdefault:CARD=seeed4micvoicec -f S32_LE -r 16000 -c 4 -d 10 sox_sound_noisy.wav
```

Jetzt kann SoX aus der `noise.wav` Datei ein Profil erstellen, was dann später verwendet werden kann. Das geschiet mit

```sh
sox noise.wav -n noiseprof noise.prof
```

Jetzt können wir das Profil auf die Test-Datei anwenden und mit den Parametern ein wenig experimentieren. Beim Testen hat sich ein Wert von `0.21` als perfekt erwiesen.

```sh
sox sox_sound_noisy.wav sox_sound_noisered.wav noisered noise.prof 0.21
```

Zum Vergleich sind die beiden Dateien [sox_sound_noisy.wav](/assets/sox_sound_noisy.wav) und [sox_sound_noisered.wav](/assets/sox_sound_noisered.wav)

Wie man sieht funktioniert es mit Sox hervorragend das Grundrauschen zu entfernen, die Sprache ist um einiges klarer.


### Schritt 2: Hintergrundgeräusche reduzieren

Wir spielen hier ein wenig mit den Funktionen von SoX und versuchen die Geräusche eines Fernsehers im Hintergrund herauszufiltern.

Wir nehmen hierzu zuerst Testsounds auf, in denen Sprache vorhanden ist und ein Fernsehr in verschiedenen Lautstärken im Hintergrund läuft.
Auch hier fürs Protokoll: Der Benutzer, der die Sprache gesprochen hat befindet sich in einer Distanz von unter einem Meter und der Fernseher von etwa sieben Meter vom Mikrofon entfernt. 

```sh
 arecord -Dsysdefault:CARD=seeed4micvoicec -f S32_LE -r 16000 -c 4 -d 10 sox_noisy_tv_silent.wav
 arecord -Dsysdefault:CARD=seeed4micvoicec -f S32_LE -r 16000 -c 4 -d 10 sox_noisy_tv_normal.wav
 arecord -Dsysdefault:CARD=seeed4micvoicec -f S32_LE -r 16000 -c 4 -d 10 sox_noisy_tv_loud.wav
```

Betrachtet man jetzt die Frequenzen der einzelnen Dateien, so fällt aus, dass zumindest das Filtern eines leisen und möglicherweise auch in zimmerlautstärke eingestellten Fernsehers möglich sein sollte.

**Frequenz `sox_noisy_tv_silent.wav` (Channel1)**
![frequency_noisy_tv_silent](/assets/frequency_silent_tv.png)

**Frequenz `sox_noisy_tv_normal.wav` (Channel1)**
![frequency_noisy_tv_normal](/assets/frequency_normal_tv.png)

**Frequenz `sox_noisy_tv_loud.wav` (Channel1)**
![frequency_noisy_tv_loud](/assets/frequency_loud_tv.png)

Das Ziel ist es also die "kleinen Wellen" auszublenden und die "großen Wellen" unverändert wiederzugeben. Hierzu eignet sich ein [Noise Gate](https://en.wikipedia.org/wiki/Noise_gate). Dieser Schritt würde je nach Einstellung auch das Grundrauschen herausfiltern.
In SoX kann man das über den `compand` Effekt erreichen. Die Erklärung der Dokumenation ist für Laien nicht ganz so leicht zu verstehen, aber es gibt einen [Post auf Sourceforge](https://sourceforge.net/p/sox/mailman/sox-users/thread/6BD30DC3-1EB7-4B3B-B866-C0777B464A3A%40senortoad.com/#msg23427259) der die Funktionsweise hervorragend in einfachen Worten erläutert.

Die nachfolgenden parametrisierten Befehle haben sich hier für die einzelnen Aufnahmen als geeignet ergben.

#### `sox_noisy_tv_silent.wav`

```sh
sox sox_noisy_tv_silent.wav silent_compand.wav compand 0.1,0.1 -inf,-42.1,-inf,-42,-42 0 -90 0.1
```

#### `sox_noisy_tv_normal.wav`

```sh
sox sox_noisy_tv_normal.wav normal_compand.wav compand 0.1,0.1 -inf,-42.1,-inf,-42,-42 0 -90 0.1
```

#### `sox_noisy_tv_loud.wav`

An dieser Datei sieht man, dass es nicht immer möglich ist über ein noise gate ein perfektes Ergebnis zu erzielen.

```sh
sox sox_noisy_tv_loud.wav loud_compand.wav compand 0.1,0.1 -inf,-33.1,-inf,-33,-33 0 -90 0.1
```

| Unbehandelt                                                | Noise Gate                                       |
| ---------------------------------------------------------- | ------------------------------------------------ |
| [sox_noisy_tv_silent.wav](/assets/sox_noisy_tv_silent.wav) | [silent_compand.wav](/assets/silent_compand.wav) |
| [sox_noisy_tv_normal.wav](/assets/sox_noisy_tv_normal.wav) | [normal_compand.wav](/assets/normal_compand.wav) |
| [sox_noisy_tv_loud.wav](/assets/sox_noisy_tv_loud.wav)     | [loud_compand.wav](/assets/loud_compand.wav)     |

### Schritt 3: Verbindung von arecord mit SoX und Einbindung in Rhasspy

Im dritten und letzen Schritt werden wir versuchen die Ergebnisse aus den vorherigen Schritten "live" anzuwenden.

#### Vorbereitungen

Wir setzen die Kommandos aus den obigen Schritten zusammen.

**Grundrauschen entfernen**

Sound für 10 Sekunden aufnehmen, Grundrauschen entfernen und in `record.wav` speichern.
Als Grundlage für das Grundrauschen verwenden wir das Rauschprofil, das sich aus [Schritt 1 der Analyse](#schritt-1-grundrauschen-filtern) ergeben hat.
```sh
arecord -Dsysdefault:CARD=seeed4micvoicec -f S32_LE -r 16000 -c 4 -d 10 | sox -t wav - -t wav record.wav noisered noise.prof 0.21
```

**Grundrauschen + Noise Gate**

Sound für 10 Sekunden aufnehmen, Grundrauschen entfernen, Noise Gate anwenden und in `record.wav` speichern.
Als Grundlage für das Grundrauschen verwenden wir das Rauschprofil, das sich aus [Schritt 1 der Analyse](#schritt-1-grundrauschen-filtern) und für das Noise Gate die Werte, die sich aus [Schritt 2 der Analyse](#schritt-2-hintergrundgeräusche-reduzieren) für einen leisen Fernseher ergeben haben.
```sh
arecord -Dsysdefault:CARD=seeed4micvoicec -f S32_LE -r 16000 -c 4 -d 10 | sox -t wav - -t wav record.wav noisered noise.prof 0.21 compand 0.1,0.1 -inf,-42.1,-inf,-42,-42 0 -90 0.1
```

#### Bestandsaufnahme

Wir verwenden Rhasspy innerhalb eines Docker Containers, wenn wir hier jetzt ein Local Command als Audioaufnahme verwenden, muss dieses Kommando in dem Container-System existieren. um das ganze zu überprüfen können wir entweder die entsprechenden Dockerfiles inspizieren oder direkt auf die Shell des Containers zugreifen und überprüfen. Wir werden letztere Möglichkeit hier verwenden.

```sh
docker exec -it rhasspy /bin/bash
```

Jetzt befinden wir uns in der Bash des Containers `rhasspy` und können verifizieren, dass arecord (Package: `alsa-utils`) und SoX (Package: `sox`) installiert sind.

```sh
apt -qq list alsa-utils sox
```

Es sollte eine Ausgabe wie in etwa die folgende resultieren:

```sh
alsa-utils/eoan,now 1.1.9-0ubuntu1 armhf [installed]
sox/eoan,now 14.4.2+git20190427-1build1 armhf [installed]
```

Auf dem `rhasspy` Docker Image ist also bereits SoX und arecord installiert und wir können die Tools verwenden. Sollte das nicht der Fall sein, wäre es erforderlich ein eigenes Docker Image zu bauen, welches die Mikrofonausgabe nach dem [Hermes-Protokoll](https://docs.snips.ai/reference/hermes) über MQTT published.

#### Anpassungen für Rhasspy

Die zusammengesetzten Kommandos aus den [Vorbereitungen](#vorbereitungen) sind noch nicht für Rhasspy angepasst und wurden auch nur unter einer Ubuntu WSL2-Instanz getestet.
Um das ganze mit Rhasspy ans Laufen zu bekommen sind noch ein paar Schritte notwendig.

Zum einen definiert das [Hermes-Protokoll](https://docs.snips.ai/reference/hermes), dass die Audiospur im RAW-Format ins MQTT gepublished wird und zum anderen soll die Aufnahme permanent laufen und nicht bloß 10 Sekunden.
Das publishen übernimmt glücklicherweise [rhasspy-microphone-cli-hermes](https://github.com/rhasspy/rhasspy-microphone-cli-hermes) für uns, das einzige was wir tun müssen, ist den stdout zu verwenden.
Das erreichen wir durch die folgende Änderung:

```sh
arecord -Dsysdefault:CARD=seeed4micvoicec -f S32_LE -r 16000 -c 4 -t raw | sox -r 16k -e signed -b 8 -c 4 -t raw - -t raw - noisered /home/noise.prof 0.21 compand 0.1,0.1 -inf,-42.1,-inf,-42,-42 0 -90 0.1
```

Leider können Pipes in dieser Form nicht von [rhasspy-microphone-cli-hermes](https://github.com/rhasspy/rhasspy-microphone-cli-hermes) verwendet werden, denn es wird hier versucht die Pipe als Parameter zu übergeben. Schuld daran ist die Funktionsweise des Python Moduls `subprocess`, welches [hier](https://github.com/rhasspy/rhasspy-microphone-cli-hermes/blob/master/rhasspymicrophone_cli_hermes/__init__.py#L108) aufgerufen wird.
Glücklicherweise bietet SoX eine paar spezielle Dateibezeichnungen mit denen das kompensiert werden kann und bspw. wie in dem folgenden Fall ein externes Programm als Input verwendet werden kann.

```sh
sox -r 16k -e signed -b 8 -c 4 -t raw "|arecord -Dsysdefault:CARD=seeed4micvoicec -f S32_LE -r 16000 -c 4 -t raw" -t raw - noisered /home/noise.prof 0.21 compand 0.1,0.1 -inf,-42.1,-inf,-42,-42 0 -90 0.1
```

So sähe das Kommando idealerweise auf Grundlage der vorherigen Analyse aus. Leider macht es Rhasspy einem nicht so einfach und unterstützt aus irgendwelchen Gründen, die leider nicht geloggt werden, nicht die "Verkettung" der beiden Kommandos. 
Wir müssen also ein klein wenig in die Trickkiste greifen und eine weitere Lösung die nur auf SoX basiert verwenden.

Wir verwenden die `alsa` Funtkionalität von SoX und verwenden so das Mikrofon als Eingang ohne `arecord` zu verwenden. Weil wir jetzt aber andere Parameter für die Aufnahme verwenden, müssen wir ein neues Rauschprofil anlegen.
```sh
sox -t alsa sysdefault:CARD=seeed4micvoicec -t wav -b 16 -c 2 -r 48k noise.wav
sox noise.wav -n noiseprof noise_sox.prof
```

Dann können wir auch hier die Effekte wieder anwenden und den Ausgang auf `stdout` umleiten.
```sh
sox -t alsa sysdefault:CARD=seeed4micvoicec -t raw -b 16 -c 2 -r 48k - noisered /home/noise_sox.prof 0.21 compand 0.1,0.1 -inf,-42.1,-inf,-42,-42 0 -90 0.1
```

Um das jetzt in Rhasspy zu integrieren verwenden wir folgende Konfiguration `profile.json`. Wichtig ist hier zu beachten, dass `sample_width` in Bytes und nicht in Bits angegeben wird.
```json
{
    "microphone": {
        "arecord": {
            "device": "default:CARD=seeed4micvoicec"
        },
        "command": {
            "list_arguments": ["-L"],
            "sample_rate": 48000,
            "sample_width": 2,
            "channels": 2,
            "list_program": "arecord",
            "record_arguments": ["-t", "alsa", "sysdefault:CARD=seeed4micvoicec", "-t", "raw", "-b", "16", "-c", "2", "-r", "48k", "-", "noisered", "/home/noise_sox.prof", "0.21", "compand", "0.1,0.1", "-inf,-42.1,-inf,-42,-42", "0", "-90", "0.1"],
            "record_program": "sox",
            "test_arguments": ["-q", "-Dsysdefault:CARD=seeed4micvoicec", "-r 16000", "-f S16_LE", "-t raw"],
            "test_program": "arecord"
        },
        "system": "command"
    }
}
```

Wenn man jetzt Rhasspy startet, werden die Filter angewendet. 
Leider funktioniert die Kombination mit Rhasspy nicht sonderlich gut - möglicherweise ist auch SoX zu langsam um die Effekte "live" anzuwenden, denn es verzögert sehr stark. Für eine genauere Untersuchung fehlt jetzt allerdings die Zeit.

### Fehlersuche

Die Ergebnisse aus dem vorherigen Schritt sind leider unbefriedigend, da eine extrem starke Verzögerung besteht. Wir möchten jetzt damit beginnen den Fehler zu suchen, dafür versuchen wir Schrittweise die Verzögerung zu reproduzieren und so den Flaschenhals auszumachen, der Optimierungen bedarf

#### 1. Schritt: SoX untersuchen

Zuerst überprüfen wir ob SoX auf dem Raspberry Pi bzw. allgemein langsam ist. Dazu beenden wir alle im Hintergrund laufenden Docker-Container und etwaige Prozesse, die Resourcen benötigen.

Dazu haben wir uns einen einfachen Test ausgedacht (Die Betrachtung des Signals über ein virtuelles Oszilloskop stellte sich als Overkill heraus):

Wir starten die Audioaufnahme über SoX direkt auf dem Raspberry Pi (Sollte SoX nicht installiert sein: `apt install sox`) und zählen laut von eins bis fünf hoch - direkt nach der gesprochenen fünf brechen wir die Aufnahme ab und hören uns die entsprechende Datei an.

Für die Aufnahme müssen wir das Kommando noch ein wenig anpassen, dass es in eine Datei schreibt und in das WAVE Format kodiert.

```sh
sox -t alsa sysdefault:CARD=seeed4micvoicec -t wav -b 16 -c 2 -r 48k test_count.wav noisered /home/pi/noise_sox.prof 0.21 compand 0.1,0.1 -inf,-42.1,-inf,-42,-42 0 -90 0.1
```

Die Aufnahme verlief fehlerfrei und ohne hörbare Verzögerungen. Jetzt starten wir wieder die Docker-Container und führen das ganze erneut durch. 

Vor dem Start der Container ist allerdings noch zu beachten, dass der `rhasspy` Container das Sound-Device übergeben bekommt und verwendet, weshalb wir dieses nicht mehr "direkt" auf dem Raspberry Pi verwenden können. Also deaktivieren wir in den Einstellungen von Rhasspy das "Audio Recording".

Fürs Protokoll betrachten wir nach dem Start der Container die Resourcenauslastung des Raspberry Pi. Dafür verwenden wir das Tool `mpstat`, welches wir zunächst allerdings installieren müssen.

```sh
sudo apt install sysstat
```

Sobald die Installation abgeschlossen ist, warten wir ein paar Minuten um einen vernünftigen Messwert zu erhalten, denn `mpstat` misst die Durchschnittsauslastung der CPU seit dem letzten Boot respektive Start des Services. Dann können wir uns mit `mpstat -P ALL` die durschnittliche Prozessorauslastung anzeigen lassen:

```sh
$ mpstat -P ALL
Linux 4.19.118-v7+ (raspberrypi)        21/10/20        _armv7l_        (4 CPU)

08:45:59     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
08:45:59     all   12.14    0.01    1.95    0.72    0.00    0.25    0.00    0.00    0.00   84.94
08:45:59       0   12.06    0.01    2.03    0.87    0.00    0.38    0.00    0.00    0.00   84.65
08:45:59       1   12.26    0.01    1.94    0.58    0.00    0.23    0.00    0.00    0.00   84.99
08:45:59       2   12.50    0.01    1.95    0.72    0.00    0.19    0.00    0.00    0.00   84.63
08:45:59       3   11.74    0.00    1.87    0.72    0.00    0.18    0.00    0.00    0.00   85.48
```

Man sieht, dass die CPU Auslastung durch die Docker-Container nicht sonderlich hoch ist, also sollten wir beim Widerholen des Tests auch wieder ein unverzögertes Ergebnis bekommen.

```sh
sox -t alsa sysdefault:CARD=seeed4micvoicec -t wav -b 16 -c 2 -r 48k test_count.wav noisered /home/pi/noise_sox.prof 0.21 compand 0.1,0.1 -inf,-42.1,-inf,-42,-42 0 -90 0.1
```

Wie erwartet ist das Ergebnis ohne wahrnehmbare Verzögerung. Das Tool SoX ist also auch auf dem Raspberry Pi in der Lage die Frequenzmodulation bzw. die Effekte auf das Audiosignal anzuwenden und es ohne wahrnehmbare Verzögerung auszugeben.

#### 2. Schritt: SoX im Docker-Container

Fraglich ist jetzt ob SoX auch im Docker-Container verzögerungsfrei arbeitet. Für einen schnellen und praxisnahen Test führen wir den Test direkt auf dem `rhasspy` Container aus. Dazu öffnen wir die Shell des Containers und führen das Kommando aus. Als Ausgabeverzeichnis wählen wir das bereits gemappte Verzeichnis aus der `docker-compose.yml` (//TODO Link GitHub), sodass wir ohne große Umstände auf die Aufnahme zugreifen können.

```sh
docker exec -it rhasspy /bin/bash
sox -t alsa sysdefault:CARD=seeed4micvoicec -t wav -b 16 -c 2 -r 48k /profiles/test_count.wav noisered /home/noise_sox.prof 0.21 compand 0.1,0.1 -inf,-42.1,-inf,-42,-42 0 -90 0.1
```

Beim Anhören ist eine minimale Verzögerung wahrnehmbar die sich im Millisekundenbereich bewegen sollte. Während das schon ein Problem für die User Experience des Sprachassistenten darstellen könnte, so sollte dieser trotzdem zeitnah das Audiosignal verarbeiten können. 

An dieser Stelle liegt also die Vermutung nahe, dass der Flaschenhals Rhasspy bzw. die entsprechende Komponente [rhasspy-microphone-cli-hermes](https://github.com/rhasspy/rhasspy-microphone-cli-hermes) ist.


#### 3. Schritt: rhasspy-microphone-cli-hermes auslagern

Im nächsten Schritt werden wir die rhasspy-microphone-cli-hermes Komponente auslagern. Zunächst direkt auf dem Raspberry Pi und bei Erfolg in einen separaten Docker-Container.

Wir installieren also zunächst die Komponente auf dem Raspberry Pi.
```sh
git clone https://github.com/rhasspy/rhasspy-microphone-cli-hermes
cd rhasspy-microphone-cli-hermes
./configure
make
make install
```

Jetzt führen wir die Komponente mit passenden Parametern aus und aktivieren zusätzlich die Debugging-Ausgabe:

```sh
bin/rhasspy-microphone-cli-hermes --record-command "sox -t alsa sysdefault:CARD=seeed4micvoicec -t raw -b 16 -c 2 -r 48k - noisered /home/pi/noise_sox.prof 0.21 compand 0.1,0.1 -inf,-42.1,-inf,-42,-42 0 -90 0.1" --sample-rate 48000 --sample-width 2 --channels 2 --host raspberrypi --debug
```

Jetzt werden die WAVE-Chunks der Audioaufnahme direkt entsprechend des [Hermes Protokoll](https://docs.snips.ai/reference/hermes) verarbeitet. In den Einstellungen von Rhasspy müssen wir jetzt noch das "Audio Recording" auf "Hermes MQTT" stellen. 

Leider bedeutet das auch, dass der Test aus den vorherigen Schritten nicht in der Form anwendbar ist. Wir testen das ganze jetzt, indem wir ein Wake-Word aufnehmen und prüfen ob wir ein verzögertes Verhalten feststellen können.

Wir nehmen eine extrem starke Latenz bei der Aufnahme des Wake-Words war. Wir nehmen trotzdem die drei Wake-Words zuende auf und prüfen jetzt die Reaktionszeit der Aktivierung und stellen fest, dass es nicht möglich ist Rhasspy aufzuwecken. Die aufgenommenen Wake-Words sind allerdings korrekt aufgenommen worden.
Wenn das Wake-Word in dem Web-Interface von Hand getriggert wird, gibt es nach einiger Zeit einen "TimeOut Error".
Die Logs der laufenden rhasspy-microphone-cli-hermes Komponente zeigen kein Fehlerhaftes verhalten. Wir betrachten also die Logs aus dem `rhasspy` Container und triggern das Wake-Word von Hand.

```sh
docker logs -f rhasspy
```

Woraufhin der folgende Fehler sichtbar werden. Der erste ist vom Aufnehmen des Wake Words und der zweite von der manuellen Aktivierung.
```
[ERROR:2020-10-21 09:52:15,622] rhasspyserver_hermes: 
Traceback (most recent call last):
  File "/usr/lib/rhasspy/.venv/lib/python3.7/site-packages/quart/app.py", line 1821, in full_dispatch_request
    result = await self.dispatch_request(request_context)
  File "/usr/lib/rhasspy/.venv/lib/python3.7/site-packages/quart/app.py", line 1869, in dispatch_request
    return await handler(**request_.view_args)
  File "/usr/lib/rhasspy/rhasspy-server-hermes/rhasspyserver_hermes/__main__.py", line 2077, in api_record_wake_example
    async for response in core.publish_wait(handle_recorded(), messages, message_types):
  File "/usr/lib/rhasspy/rhasspy-server-hermes/rhasspyserver_hermes/__init__.py", line 959, in publish_wait
    result_awaitable, timeout=timeout_seconds
  File "/usr/lib/python3.7/asyncio/tasks.py", line 449, in wait_for
    raise futures.TimeoutError()
concurrent.futures._base.TimeoutError

[..]

[ERROR:2020-10-21 09:58:24,743] rhasspyserver_hermes: 
Traceback (most recent call last):
  File "/usr/lib/rhasspy/.venv/lib/python3.7/site-packages/quart/app.py", line 1821, in full_dispatch_request
    result = await self.dispatch_request(request_context)
  File "/usr/lib/rhasspy/.venv/lib/python3.7/site-packages/quart/app.py", line 1869, in dispatch_request
    return await handler(**request_.view_args)
  File "/usr/lib/rhasspy/rhasspy-server-hermes/rhasspyserver_hermes/__main__.py", line 827, in api_listen_for_command
    handle_captured(), messages, message_types
  File "/usr/lib/rhasspy/rhasspy-server-hermes/rhasspyserver_hermes/__init__.py", line 959, in publish_wait
    result_awaitable, timeout=timeout_seconds
  File "/usr/lib/python3.7/asyncio/tasks.py", line 449, in wait_for
    raise futures.TimeoutError()
concurrent.futures._base.TimeoutError
```

An dieser Stelle können wir leider nicht mehr damit anfangen

#### 4. Schritt: UDP Streaming

Mit Rhasspy version 2.5 ist es möglich einen [UDP-Stream zu verwenden](https://rhasspy.readthedocs.io/en/latest/audio-input/#gstreamer). Wir versuchen also jetzt einen UDP-Stream an Rhasspy zu übermitteln, der dann von dem Modul [rhasspy-microphone-cli-hermes](https://github.com/rhasspy/rhasspy-microphone-cli-hermes) über [GStreamer](https://gstreamer.freedesktop.org/) empfangen und daraufhin verarbeitet wird.

Dazu ist es zunächst nötig, dass wir den entsprechenden UDP-Port für den Container freigeben, dazu fügen wir in der `docker-compose.yml` den folgenden Punkt hinzu und starten den Container neu.

```yml
rhasspy:
  [..]
  ports:
    - "12333:12333/udp"
```

Jetzt müssen wir die `profile.json` Konfiguration von Rhasspy anpassen und rhasspy neu starten.

```json
"microphone": {
  "system": "command",
  "command": {
    "record_program": "gst-launch-1.0",
    "record_arguments": "udpsrc port=12333 ! audio/x-raw, rate=16000, channels=1, format=S16LE ! filesink location=/dev/stdout",
    "sample_rate": 16000,
    "sample_width": 2,
    "channels": 1
  }
}
```

Rhasspy ist nun empfangsbereit für einen UDP-Stream, den wir direkt vom Raspberry Pi aus starten. Dazu gehen wir folgendermaßen vor.

```sh
sudo apt install gstreamer1.0-tools gstreamer1.0-plugins-good
```

Jetzt verbinden wir unser bekanntes SoX Kommando mit gstreamer, sodass ein UDP-Stream produziert wird:
```sh
sox -t alsa sysdefault:CARD=seeed4micvoicec -t raw -b 16 -c 2 -r 48k - noisered /home/pi/noise_sox.prof 0.21 compand 0.1,0.1 -inf,-42.1,-inf,-42,-42 0 -90 0.1 | gst-launch-1.0 fdsrc fd=0 ! audio/x-raw, rate=48000, channels=2, format=S16LE ! audioconvert ! audioresample ! audio/x-raw, rate=16000, channels=1, format=S16LE ! udpsink host=127.0.0.1 port=12333
```

Das Wake-Word kann ohne Probleme und auch ohne merkliche Verzögerung eingesprochen werden.

In dem Zuge ist uns die Theorie gekommen, dass der Fehler gar nicht mit dem Tooling zusammenhängt, sondern mit dem Zusammenspiel der Encodierung und Rhasspy, denn in diesem Beispiel verwenden eine Sampling-Rate von 16000 Hz und lediglich einen Channel.

#### 5. Schritt: SoX auf Sampling-Rate anpassen

`profile.json`:
```json
"microphone": {
  "command": {
    "channels": "1",
    "list_arguments": ["-L"],
    "list_program": "arecord",
    "record_arguments": "-t alsa sysdefault:CARD=seeed4micvoicec -t raw -b 16 -c 1 -r 16k - -q noisered /home/noise_sox.prof 0.21 compand 0.1,0.1 -inf,-42.1,-inf,-42,-42 0 -90 0.1",
    "record_program": "sox",
    "sample_rate": "16000",
    "test_arguments": [
      "-q",
      "-Dsysdefault:CARD=seeed4micvoicec",
      "-r 16000",
      "-f S16_LE",
      "-t raw"
    ],
    "test_program": "arecord"
  },
  "system": "command"
}
```

Mit dem Resultat, dass die Einsprache eines Wakewords problemlos verlief. Das Aufwecken verläuft auch problemlos. Allerdings sind jetzt noch Anpassungen an Pocketsphinx nötig, //TODO denn, ....

```json
"command": {
  "webrtcvad": {
    "silence_sec": "1"
  }
}
```

### Fazit //TODO Fazit bearbeiten

Das Unterdrücken von Hintergrundgeräuschen ist auch mit einfachen Mitteln ohne künstliche Intelligenzen möglich. Hier gilt es allerdings zu beachten, dass der Test unter idealen Bedingungen durchgeführt wurde und nicht auf jede Situation getestet wurde. Der gesamte Abschnitt ist also eher als Proof-Of-Concept zu betrachten, denn wenn eine Filterung wirklich angestrebt werden sollte, ist ein intensiver Praxistest von Nöten.
Die Integration mit Rhasspy funktioniert leider nicht so gut wie zuerst gedacht und wirft zeitintensive Probleme auf, die wir hier in dem Zeitplan des Projekts nicht näher untersuchen können.

Für dieses Projekt werden wir die Hintergrundgeräuschunterdrückung also nicht weiter verwenden.

# 💡 Lichtsteuerung

## Konfiguration von Zigbee2MQTT

### Paaren der Lampe mit Zigbee2MQTT

Zuerst muss die Zigbee-fähige Lampe Zigbee2MQTT bekannt sein. Wir verwenden im Folgenden die aus dem [Tech-Stack](/docs/tech-stack/) bekannte Philips Hue white and color (929001573). Wenn andere Lampen verwendet werden sollen, müssen die Schritte entsprechend der [Dokumentation von Zigbee2MQTT](https://www.zigbee2mqtt.io/information/supported_devices.html) angepasst werden.

Die einfachste Methode für unsere Lampe ist ein [Touchlink reset](https://www.zigbee2mqtt.io/information/touchlink). Dazu genügt es eine Nachricht ohne Nutzdaten in das MQTT-Topic `zigbee2mqtt/bridge/config/touchlink/factory_reset` zu publishen. Die Lampe muss sich dafür nahe (laut Dokumentation in Entfernung von unter 10cm) an dem Zigbee-Stick befinden. Zusätzlich muss in der `configuration.yaml` von Zigbee2MQTT das Attribut `permit_join: true` gesetzt sein.

Sobald sich die Glühbirne gepaart hat, sollte diese kurz aufblinken und die Paarung ist abgeschlossen.

Es ist sinnvoll nach jeder Paarung einer Lampe einen `friendly_name` in der `devices.yaml` zuzuweisen um den Überblick nicht zu verlieren und die Konfiguration später zu erleichtern. Zum Beispiel so:

Nachdem alle gewünschten Lampen erfolgreich gepaart wurden, sollte `permit_join: false` gesetzt werden.

```yml
'0x123456789abcdef0':
  friendly_name: 'lamp_living_room_1'
'0x123456789abcdef1':
  friendly_name: 'lamp_bathroom_1'  
'0x123456789abcdef2':
  friendly_name: 'lamp_bathroom_2'
'0x123456789abcdef3':
  friendly_name: 'lamp_balcony_1'
```

Wir werden im Folgenden zwei Möglichkeiten beschreiben einen Touclink reset durchzuführen:

#### Touchlink Reset über Node-Red

Im Web-Interface von [Node-Red](http://raspberrypi:1880/) ist ein Flow Namens `Touchlink Reset` verfügbar, der mit einem einfachen Klick eine entsprechende Nachricht in das MQTT-Topic published.

![Node-Red Touchlink Reset Flow](/assets/Node-Red_Tochlink_Reset.png)

#### Touchlink Reset über MQTT-Explorer

Im Folgenden verwenden wir den [MQTT Explorer](http://mqtt-explorer.com/) um den MQTT-Broker anzusteuern und beginnen damit uns auf dem bereitgestellten Mosquitto-Broker anzumelden:

![MQTT-Explorer Login](/assets/MQTT_Explorer_1.png)

Der Login sollte erfolgreich sein und wir können eine leere Nachricht auf das oben genannte Topic publishen:

![MQTT-Explorer Publish](/assets/MQTT_Explorer_2.png)

### Konfigurieren der Gruppen

In der `groups.yaml` werden die Gruppen der Lampen genau spezifiziert. Derzeit unterstützt der Sprachassistent die Folgenden Gruppen (//TODO Am Ende alle Gruppen einfügen):

* living_room
* bedroom
* dining_room
* kitchen
* hallway
* bathroom

Weitere Gruppen können hier zwar definiert und über MQTT verwendet werden, allerdings ist der Sprachassistent noch nicht für diese Trainiert. Wenn der Sprachassistent diese auch ansprechen soll, muss die Konfiguration entsprechend der [Dokumentation](#erweiterung-der-gruppen) angepasst werden.

Damit die Lampen Gruppenweise angesteuert werden können, müssen diese den Gruppen über ihre ID zugeordnet werden, das sähe dann für das obige Beispiel weiterführend so aus:

```yml
'1':
    friendly_name: living_room
    devices:
        - '0x123456789abcdef0'
'2':
    friendly_name: bathroom
    devices:
        - '0x123456789abcdef1'
        - '0x123456789abcdef2'
'3':
    friendly_name: balcony
    devices:
        - '0x123456789abcdef3'
```

Wichtig ist hier, dass die numerische Gruppen-ID eindeutig ist.

## Konfiguration von Rhasspy

Der Sprachassistent ist bereits vorkonfiguriert. Hier sind lediglich Schritte zur Erweiterung nötig.

### Erweiterung der Gruppen

Sollten weitere Gruppen über den Sprachassistenten angesteuert werden sollen und diese bereits nach [Konfigurieren der Gruppen](#konfigurieren-der-gruppen) definiert worden sein, dann muss für Rhasspy die Datei `profiles/de/slots/light_rooms` angepasst werden. Das Format hier richtet sich nach der [Dokumentation von Rhasspy](https://rhasspy.readthedocs.io/en/latest/training/#sentencesini).

Wichtig ist hier, dass eine Substitution für das Attribut `room` auf den `friendly_name` der `groups.yml` von Zigbee2MQTT durchgeführt wird um die entsprechende Gruppe anzusteuern.

Als Beispiel weiterführend für das obige Beispiel um den Sprachassistenten für die Steuerung der Gruppe `balcony` zu erweitern:

```
(Balkon | Terasse | Draussen){room:balcony}
```

Jetzt muss der Sprachassistent neu trainiert werden. Das geschiet entsprechend der [Anleitung](/getting-started/installation/#rhasspy-trainieren).

Die Gruppen sind jetzt einsatzbereit und können verwendet werden.


## Node-Red Flows

In der Bibliothek von Node-Red sind unterschiedliche Flows vorhanden, die eingesetzt werden können.

### `LightAPIFlow.json`

Dieser Flow implementiert die Lichtsteuerung über die API [/lights/set](#lightsset). Der Request Body wird über JavaScript-Funktionsblöcke erstellt und an die API übergeben.

### `LightsAPIFlow_Raw.json`

Dieser Flow implementiert die Lichtsteuerung über die API [/lights/set/raw](#lightssetraw). Der Request Body aus Rhasspy wird direkt an die API übergeben, die Logik liegt komplett innerhalb der API.

### `ChangeLightBrightness.json` / `ChangeLightColor.json` / `SwitchLight.json`

Diese drei Flows sollten nur dann aktiv sein, wenn die API nicht verwendet werden soll. Hier liegt die gesamte Logik in Node-Red, die über JavaScript-Funktionsblöcke implementiert wird.


# 🗣 Text To Speech

## Konfiguration von Espeak

Die Standard-Implementierung von Rhasspy für die Espeak Text-To-Speech Engine bietet nicht viel Raum für Optionen, daher müssen wir uns einem kleinen Trick innerhalb der `profile.json` bedienen und die Standartwerte mit Parametern überschreiben.

Zunächst einmal spricht die Standardeinstellung von Espeak zu schnell und ist desweiteren auch eine männliche Stimme, die für unsere Personifizierung über das Wakeword Trixie ungeeignet ist. Espeak bietet allerdings für die Sprachen verschiedene Stimmarten, die mit einem Suffix bestimmt werden können. Nach durchprobieren hat sich `de+f4` als am natürlichsten ergeben. Die Anpassung der Parameter für Wortpausen sowie Sprechgeschwindigkeit und Pitch sind ebenfalls durch ausprobieren entstanden und im Hinblick auf die Ziele des Forschungsprojekts so gewählt, dass die Stimme gut verständlich ist. 

Die Konfiguration sieht insgesamt so aus:

```json
"text_to_speech": {
        "espeak": {
            "arguments": [
                "-v",
                "de+f4",
                "-s",
                "120",
                "-g",
                "1",
                "-p",
                "45"
            ]
        },
        "system": "espeak"
    }
```

Die Stimme ist leider nicht besonders natürlich, denn es handelt sich hierbei lediglich um einen Sprachsynthesizer, der auf der Verkettung von Diphonen basiert.

# 📝 Speech To Text

Wir verwenden [Pocketsphinx](https://rhasspy.readthedocs.io/en/latest/speech-to-text/#pocketsphinx) als Speech-To-Text Dienst.

## Einrichtung

Beim ersten Start wird ein Download eines von vortrainierten akustischen Modells sowie Wörterbuch benötigt.
Es handelt sich dabei um die [CMU Sphinx](https://sourceforge.net/projects/cmusphinx/) Datenbank.
Ein eigenes Training ist hier erstmal nicht sinnvoll was aus der 
[Dokumentation](https://cmusphinx.github.io/wiki/tutorialam/) auch hervorgeht, denn wir haben weder genügend Zeit noch 
genug Daten dafür.

## Technische Schwierigkeiten

Das Speech-To-Text-System ist hierbei auf dem Raspberry Pi ziemlich langsam - es ist allerdings möglich die Aufgabe auf
ein leistungsstärkeres System zu übertragen. Besonders beim Language Model Mixing (siehe nächsten Abschnitt) ist die Hardware des Rhaspberry zu schwach und es wird ausdrücklich empfohlen die Berechnung über einen Server laufen zu lassen.

Es geht nicht aus der Dokumentation hervor, allerdings müssen für Pocketsphinx die Intents (`sentences.ini`) gepflegt 
sein, weil aus dieser ein Sprachmodell erstellt wird. Das bedeutet es können noch so viele Wörter im Wörterbuch stehen, 
Pocketsphinx erkennt standardmäßig nur die Satzbestandteile, die auch in der `sentences.ini` stehen, selbst wenn auf der 
remote-Instanz bloß der Speech-To-Text Dienst läuft. Dieses Verhalten kann man abändern, indem man den Wert `mix_weight` bei PocketSphinx erhöht.
Je höher dieser Wert ist, desto mehr wird die `sentences.ini` mit dem language Model von PocketSphinx vermischt und es werden auch Wörter erkannt, die nicht in der `sentences.ini` eingetragen wurden. Aufgrund der Größe des mitgelieferten Language Models nimmt die Spracherkennung mit einem mix_weight > 0 sehr viel mehr Rechenkapazität in Anspruch.

# 🕹 Intent Recognition

Wir verwenden als intent recognition service [Fsticuffs](https://rhasspy.readthedocs.io/en/latest/intent-recognition/#fsticuffs), welches die [rhasspy-nlu](https://github.com/rhasspy/rhasspy-nlu) nutzt und auf [OpenFst](http://www.openfst.org/twiki/bin/view/FST/WebHome) basiert.

## Glossar

Um den Elefanten im Raum direkt anzusprechen und die Funktionsweise zu erläutern werden wir jetzt erstmal die Begrifflichkeiten erläutern.

### NLU

NLU steht für **N**atural **L**anguage **U**nderstanding und bezeichnet im wesentlichen den Prozess natürliche Sprache in für einen Computer verständliche Form zu bringen.

### FST

Bei FSTs handelt es sich um die sogenannten **f**inite-**s**tate **t**ransducers oder auf deutsch: Endlicher Transduktor. Es handelt sich hierbei um eine spezielle Form der endlichen Automaten, die zusätzlich zu dem Eingabealphabet ein Ausgabealphabet besitzen.
Ein FST kann zusätzlich auch gewichtet sein - das bedeutet, dass man den Zustandsübergangsfunktionen des Automats einen Wert zuweist. Dieser Aspekt macht den FST besonders attraktiv für die Sprachsynthese um ein Eingabezeichen mit unterschliedlichen Phonemen zu verknüpfen.

Als Beispiel ist hier ein Automat, der die Schreibweise und Aussprache von "OpenFst" verknüpft und determiniert.

![FST](/assets/openfst.jpg)<br/>
<i><sub>Quelle: [http://www.openfst.org/twiki/bin/view/FST/WebHome](http://www.openfst.org/twiki/bin/view/FST/WebHome)</sub></i>

### OpenFst

OpenFst ist eine quelloffene Python-Bibliothek um FSTs zu konstruieren und zu verwenden.

### rhasspy-nlu

Hierbei handelt es sich um die hauseigene NLU Bibliothek von Rhasspy. Es wird hierbei eine Datei `sentences.ini` gepflegt, die alle Sätze beinhaltet, welche erkannt werden sollen. Diese Sätze werden mit ihren Phonemen der Lautsprache verknüpft und daraus kann dann ein FST erstellt werden.
Hierbei muss jedes potenziell ausgesprochene Wort mit seinen Phonemen verknüpft sein, dazu kann man ein Wörterbuch anlegen und eigene Wörter nach dem [CMU Pronouncing Dictionary](https://github.com/cmusphinx/cmudict) definieren.
Der Schritt ist nicht zwingend notwendig, denn rhasspy-nlu bietet die Möglichkeit Aussprachen zu "erraten". Dazu wird die Bibliothek [Phonetisaurus](https://github.com/AdolfVonKleist/Phonetisaurus) verwendet.

### Fsticuffs

Fsticuffs basiert auf der rhasspy-nlu Bibliothek und implementiert die NLU für das [Hermes Protokoll](https://docs.snips.ai/reference/hermes), welches Rhasspy verwendet.

## Konfiguration von Rhasspy

Unser Ziel ist es eine einfache und zuverlässige Funktionsweise von Deep Thought zu gewährleisten, daher sollten etwaige Konfigurationen vorzugsweise auf der obersten Abstraktionsebene `rhasspy-nlu` erfolgen.

### Konfiguration von Fsticuffs

In erster Linie geht es in diesem Abschnitt darum welche Möglichkeiten es zur Konfiguration von Fsticuffs gibt, ohne das Ziel diese umzusetzen.

Das Web-Interface von Rhasspy bietet hier lediglich ein Kontrollkästchen `Fuzzy` an. Wenn aktiviert, lässt Fsticuffs bestimmte unscharfe Übereinstimmungen zu.
Zusätzlich ist es laut Dokumentation möglich einen eigenen Intent-Graphen zu übergeben. Das dürfte dann sinnvoll sein, wenn man den Graphen extern programmatisch erzeugen will.
Zuletzt gibt es noch die Option `ignore_unknown_words`, welche unbekannte (nicht in der `sentences.ini` definierte Wörter) ignoriert und somit mehr Sätze zulässt.

Wir werden es hier erstmal bei der Standard-Konfiguration belassen - sprich: Lediglich `Fuzzy` ist aktiviert.


# 💻 API

## Lichtsteuerung

Es gibt eine eigens entwickelte API für die Lichtsteuerung.

### Unit-Tests

Die API besitzt eigene Unit-Tests zur Gewährleistung der Funktionalität. Zum ausführen der Tests einfach Das Kommando `pytest` unterhalb des Verzeichnisses `/src/api` ausführen. 

### Endpunkte

#### `/lights/set`

Der Endpunkt erwartet einen POST-Request mit einem JSON Objekt, welcher eine vordefinierte Form haben muss. 

```json
{
    "friendly_name": "living_room",
    "payload": {
        "state": "ON",
        "brightness": 255,
        "color": "#55ffaa"
    },
    "feedback": {
        "text": "Okay ich ändere das Licht im Wohnzimmer"
    }
}
```

`friendly_name` und `payload` sind hierbei die erforderlichen Attribute. Die Attribute unter `payload` sind hierbei frei wählbar. 

Aus dem Request wird ein MQTT-Publish auf das Topic `zigbee2mqtt/<friendly_name>/set` mit der jeweiligen Nachricht, die im `payload` Objekt definiert ist.
Nachdem der Publish ausgeführt wurde, wird ein entsprechender Feedback-Text über Text-To-Speech ausgegeben.

Die Schnittstelle ist sehr flexibel einsetzbar, denn sie ist nicht restriktiv.

#### `/lights/set/raw`

Der Endpunkt erwartet einen POST-Request mit einem JSON Objekt, der entsprechend von Rhasspy erzeugt wurde. Wichtig ist hierbei hauptsächlich, dass `entities` entsprechend den Erwartungen der Schnittstelle entspricht.

```json
"entities": [
        {
            "entity": "room",
            "value": "living_room",
            //[..]
        },
        {
            "entity": "state",
            "value": "on",
            //[..]
        },
        {
            "entity": "brightness",
            "value": 255,
            //[..]
        },
        {
            "entity": "color",
            "value": "#ffffff",
            //[..]
        }
    ]
//[..]
```

Die Schnittstelle erstellt aus dem Request eine kompatible MQTT-Nachricht, die dann im jeweiligen Topic gepublished wird.
Danach wird ein entsprechender Feedback-Text über Text-To-Speech ausgegeben, der den eingesprochenen Text wiederholt.