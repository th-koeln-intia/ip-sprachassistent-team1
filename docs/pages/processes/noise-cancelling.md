---
title: Hintergrundgeräuschreduzierung
permalink: /results/noise-cancelling/
subtitle: Entwicklungsergebnisse zur Implementierung der Hintergrundgeräusche.
layout: page
show_sidebar: false
menubar: docs_menu
---


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

Rhasspy hat zur Filterung von Hintergrundgeräuschen keine geeignete eigene Funktion, allerdings ist es möglich den [Speech-To-Text Service ein wenig zu sensibilisieren](#rhasspy-silence). Wenn wir uns nun auf die Filterung von Hintergrundgeräuschen beschränken, ist notwendig sich direkt auf den Audiotreiber bzw. auf das verwendete Tool zu konzentrieren, da das Mikrofon permanent das Audiosignal als MQTT Nachricht übermittelt.

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

Leider bietet Rhasspy nicht die Möglichkeit die Parameter anzupassen bzw. ist das ganze sehr schlecht dokumentiert. Daher verwenden wir im Folgenden nicht das mitglieferte `arcord` von Rhasspy, sondern weichen auf ein `Local Command` aus. Die folgende Konfiguration von `command` ist äquivalent zu der Standard-Konfiguration von `arecord`.

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

### rhasspy-silence

Bei [rhasspy-silence](https://github.com/rhasspy/rhasspy-silence) handelt es sich um eine Implementierung von [Sprechpausenerkennung](https://de.wikipedia.org/wiki/Sprechpausenerkennung). Dieser Dienst wird unter anderem von unserem Speech-To-Text-Service [rhasspy-asr-pocketsphinx-hermes](https://github.com/rhasspy/rhasspy-asr-pocketsphinx-hermes/) verwendet, weshalb es hier Möglichkeiten zur Optimierung gibt.

Interessant ist das gerade deshalb, weil hier möglicherweise eine Filterung bei einer guten Parametrisierung obsolet werden würde, allerdings ist auch eine Kombinierung denkbar, denn eine Hintergrundgeräuschreduzierung kann auch in ein klareres Klangbild resultieren.

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
arecord -Dsysdefault:CARD=seeed4micvoicec -f S32_LE -r 16000 -c 4 -d 10 \
 | \
sox -t wav - -t wav record.wav noisered noise.prof 0.21
```

**Grundrauschen + Noise Gate**

Sound für 10 Sekunden aufnehmen, Grundrauschen entfernen, Noise Gate anwenden und in `record.wav` speichern.
Als Grundlage für das Grundrauschen verwenden wir das Rauschprofil, das sich aus [Schritt 1 der Analyse](#schritt-1-grundrauschen-filtern) und für das Noise Gate die Werte, die sich aus [Schritt 2 der Analyse](#schritt-2-hintergrundgeräusche-reduzieren) für einen leisen Fernseher ergeben haben.
```sh
arecord -Dsysdefault:CARD=seeed4micvoicec -f S32_LE -r 16000 -c 4 -d 10 \
 | \
sox -t wav - \
-t wav record.wav \
noisered noise.prof 0.21 \
compand 0.1,0.1 -inf,-42.1,-inf,-42,-42 0 -90 0.1
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
arecord -Dsysdefault:CARD=seeed4micvoicec -f S32_LE -r 16000 -c 4 -t raw \ 
  | \
sox -r 16k -e signed -b 8 -c 4 -t raw - \
 -t raw - \
 noisered /home/noise.prof 0.21 \
 compand 0.1,0.1 -inf,-42.1,-inf,-42,-42 0 -90 0.1
```

Leider können Pipes in dieser Form nicht von [rhasspy-microphone-cli-hermes](https://github.com/rhasspy/rhasspy-microphone-cli-hermes) verwendet werden, denn es wird hier versucht die Pipe als Parameter zu übergeben. Schuld daran ist die Funktionsweise des Python Moduls `subprocess`, welches [hier](https://github.com/rhasspy/rhasspy-microphone-cli-hermes/blob/master/rhasspymicrophone_cli_hermes/__init__.py#L108) aufgerufen wird.
Glücklicherweise bietet SoX eine paar spezielle Dateibezeichnungen mit denen das kompensiert werden kann und bspw. wie in dem folgenden Fall ein externes Programm als Input verwendet werden kann.

```sh
sox -r 16k -e signed -b 8 -c 4 -t raw "|arecord -Dsysdefault:CARD=seeed4micvoicec -f S32_LE -r 16000 -c 4 -t raw" \
  -t raw - \
  noisered /home/noise.prof 0.21 \
  compand 0.1,0.1 -inf,-42.1,-inf,-42,-42 0 -90 0.1
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
sox -t alsa sysdefault:CARD=seeed4micvoicec \
  -t raw -b 16 -c 2 -r 48k - \
  noisered /home/noise_sox.prof 0.21 \ 
  compand 0.1,0.1 -inf,-42.1,-inf,-42,-42 0 -90 0.1
```

Die Integration in Rhasspy funktioniert nur mit einer Sampling-Rate von 16000 Hz und einem Channel. Grund dafür ist, dass der Dienst [rhasspy-silence](#rhasspy-silence) auf [wbrtcvad](https://github.com/wiseman/py-webrtcvad) basiert, welches zwingend ein Mono-Signal voraussetzt. Theoretisch sollte zumindest eine andere Sampling-Rate möglich sein, denn wbrtcvad unterstützt nach eigener Aussage auch Sampling-Raten von 8000 Hz, 32000 Hz und 48000 Hz. Rhasspy arbeitet intern allerdings standardmäßig mit 16000 Hz und eine Parametrisierung des Werts ist nicht möglich, solange man keine eigene Instanz der entsprechenden Dienste aufsetzt.
Dass Rhasspy mit einer anderen Abtastrate bzw. anderer Anzahl Kanälen nicht zurecht kommt, scheint ein Bug zu sein, denn eigentlich sollte das Signal entsprechend für rhasspy-silence [konvertiert](https://github.com/rhasspy/rhasspy-microphone-cli-hermes/blob/master/rhasspymicrophone_cli_hermes/__init__.py#L173) werden.

Also müssen wir das Kommando noch leicht abändern. Zusätzlich fügen wir den Paramter `-q` hinzu, der verhindert, dass SoX den Status loggt, um die Logs freizuhalten.
```sh
sox -t alsa sysdefault:CARD=seeed4micvoicec \
  -t raw -b 16 -c 1 -r 16k - \
  -q \
  noisered /home/noise_sox.prof 0.21 \
  compand 0.1,0.1 -inf,-42.1,-inf,-42,-42 0 -90 0.1
```

Um das jetzt in Rhasspy zu integrieren verwenden wir folgende Konfiguration `profile.json`. Wichtig ist hier zu beachten, dass `sample_width` in Bytes und nicht in Bits angegeben wird.
```json
{
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
}
```

Die Filter werden jetzt angewendet. Allerdings sind jetzt noch Anpassungen an Pocketsphinx nötig, denn das Unterdrücken der Hintergrundgeräusche geschiet in unserer Implementierung nahezu direkt nach Sprechpausen, was Pocketsphinx als Stille wahrnimmt und je nach Länge der Sprechpause als Abbruchbedingung wertet.

Wir setzen den Parameter für den Zeitraum, in dem es still sein muss, damit Pocketsphinx eine Abbruchbedingung wahrnimmt auf eine Sekunde. Eine weitere Möglichkeit wäre es die "attack" und "release" Werte des Noise-Gates anzupassen.

```json
"command": {
  "webrtcvad": {
    "silence_sec": "1.5"
  }
}
```

##### Alternative: UDP-Streaming mit GStreamer

Mit Rhasspy Version 2.5 ist es möglich einen [UDP-Stream zu verwenden](https://rhasspy.readthedocs.io/en/latest/audio-input/#gstreamer). Wir versuchen also jetzt einen UDP-Stream an Rhasspy zu übermitteln, der dann von dem Modul [rhasspy-microphone-cli-hermes](https://github.com/rhasspy/rhasspy-microphone-cli-hermes) über [GStreamer](https://gstreamer.freedesktop.org/) empfangen und daraufhin verarbeitet wird.

Dazu ist es zunächst nötig, dass wir den entsprechenden UDP-Port für den Container freigeben, dazu fügen wir in der `docker-compose.yml` den folgenden Punkt hinzu und starten den Container neu.

```yml
rhasspy:
  [..]
  ports:
    - "12333:12333/udp"
```

Jetzt müssen wir die `profile.json` Konfiguration von Rhasspy anpassen.

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
sox -t alsa sysdefault:CARD=seeed4micvoicec \
  -t raw -b 16 -c 2 -r 48k - \
  noisered /home/pi/noise_sox.prof 0.21 \
  compand 0.1,0.1 -inf,-42.1,-inf,-42,-42 0 -90 0.1 \
  | \
gst-launch-1.0 fdsrc fd=0 ! \
  audio/x-raw, rate=48000, channels=2, format=S16LE ! \
  audioconvert ! \
  audioresample ! \
  audio/x-raw, rate=16000, channels=1, format=S16LE ! \
  udpsink host=127.0.0.1 port=12333
```

Es ist sinnvoll, das ganze wieder in einem weiteren Docker-Container auszulagern.


### Fazit

Das Unterdrücken von Hintergrundgeräuschen ist auch mit einfachen Mitteln ohne künstliche Intelligenzen möglich. Hier gilt es allerdings zu beachten, dass der Test unter idealen Bedingungen durchgeführt wurde und nicht auf jede Situation getestet wurde. Der gesamte Abschnitt ist also eher als Proof-Of-Concept zu betrachten, denn wenn eine Filterung wirklich angestrebt werden sollte, ist ein intensiver Praxistest von Nöten.

Die Integration mit Rhasspy funktioniert über SoX leider auf Anhieb nicht so gut wie zuerst gedacht, ist allerdings mit ein wenig Hirnschmalz lösbar.

Um ein geeigneten Prozess zur Hintergrundgeräuschfilterung über SoX zu implementieren, muss man sich mit der Frequenzmodulation von Audiosignalen auseinandersetzen sowie untersuchen wie das WAV/RAW-Audioformat und die Signalverarbeitung derer funktioniert. Das kann unter Umständen aufwendig werden.

Zu guter Letzt ist es wichtig nochmal zu erwähnen, dass die Implementierung hier unter idealen Bedingungen und nur im Rahmen der Möglichkeiten des Projekts getestet wurde. Es ist von ungemeiner Bedeutung die Hintergrundgeräuschfilterung intensiv unter unterschiedlichen Bedingungen zu testen und den Prozess anhand der Ergebnisse anzupassen und auf den Use-Case zuzuschneiden, denn eine schlechte Implementierung würde enorme Auswirkungen auf die User Experience haben.
Als Beispiel sind wir mit dieser Referenzimplementierung in der Lage einen zimmerlauten Fernseher auf 7m Abstand herauszufiltern, das bedeutet allerdings auch, dass Menschen (potenzielle Benutzer des Sprachassistenten), die in 7m Entfernung stehen und in Zimmerlautstärke sprechen herausgefiltert werden.

Es ist durchaus möglich, dass GStreamer (Siehe: [Alternative: UDP-Streaming mit GStreamer](#alternative-udp-streaming-mit-gstreamer)) weitere Möglichkeiten zur Filterung bietet, die über die Grenzen von SoX hinausgehen, denn hier gibt es unzählige Plugins die zum einen verfügbar sind und zum anderen auch selbst entwickelt werden können.
