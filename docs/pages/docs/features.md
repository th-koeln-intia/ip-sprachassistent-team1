---
title: Features
permalink: /docs/features/
subtitle: Features
layout: page
show_sidebar: false
menubar: docs_menu
---

# Wake Word

Das Wake Word oder auch Hot Word bzw. Aktivierungswort ist das wort, welches den Sprachassistenten Deep Thought aktiviert. Das Wake Word ist durch den Nutzer festzulegen und muss eingesprochen werden.

## Faktoren

Ein ideales Wake Word soll

1. Einfach sein
2. Klar verständlich sein
3. Verlässlich sein
4. Differenzierbar sein

## Marktanalyse

Es existieren diverse Sprachassistenten mit unterschiedlichen Wake Words auf den Markt. In der folgenden Tabelle sind die gängigen aufgelistet:

| Sprachassistent                | Wake Word                                                         |
| ------------------------------ | ----------------------------------------------------------------- |
| Alexa                          | "Alexa" <br /> "Amazon" <br /> "Computer" <br /> "Echo"   |
| Google Assistent               | "Hey, Google" <br /> "Okay, Google"                           |
| Siri                           | "Hey, Siri"                                                     |
| Bixby                          | "Hey, Bixbi"                                                    |
| Cortana                        | "Hey, Cortana"                                                  |
| Hallo Magenta                  | "Hallo, Magenta" <br /> "Hey, Magenta" <br /> "Hi, Magenta" |
| Intelligent Personal Assistent | "Hey, BMW"                                                      |
| MBUX                           | "Hey, Mercedes"                                                 |
| Jasper                         | "Jasper"                                                        |
| Snips                          | "Hey, Snips"                                                    |

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

Während des testens hat sich gezeigt, dass das Mikrofon sehr empfindlich ist und Hintergrundgeräusche wie einen Fernseher erkennt. Es wird versucht aus der Sprache dort einen Intent zu ziehen. Vielleicht ist es sinnvoll über ein anderes Audio-Recording zu überlegen, wie z.B. [SoX](http://sox.sourceforge.net/)

Wenn ein höherer Wert für `minimum_matches` gewählt wird, resultiert das in folgende Meldung und ermöglicht keine Aktivierung mehr:

```
rhasspy        | [DEBUG:2020-09-29 08:56:29,593] rhasspy-wake-raven: Enter refractory for 2.0 second(s)
rhasspy        | [DEBUG:2020-09-29 08:56:31,795] rhasspy-wake-raven: Exiting refractory period
```

