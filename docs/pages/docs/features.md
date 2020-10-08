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

### Fazit

Das Unterdrücken von Hintergrundgeräuschen ist auch mit einfachen Mitteln ohne künstliche Intelligenzen möglich. Hier gilt es allerdings zu beachten, dass der Test unter idealen Bedingungen durchgeführt wurde und nicht auf jede Situation getestet wurde. Der gesamte Abschnitt ist also eher als Proof-Of-Concept zu betrachten, denn wenn eine Filterung wirklich angestrebt werden sollte, ist ein intensiver Praxistest von Nöten.
Die Integration mit Rhasspy funktioniert leider nicht so gut wie zuerst gedacht und wirft zeitintensive Probleme auf, die wir hier in dem Zeitplan des Projekts nicht näher untersuchen können.

Für dieses Projekt werden wir die Hintergrundgeräuschunterdrückung also nicht weiter verwenden.