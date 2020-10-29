---
title: Wecker
permalink: /results/alarm/
subtitle: Entwicklungsergebnisse Wecker
layout: page
show_sidebar: false
menubar: results_menu
---

# Entwicklung des Weckers

### Anlegen einer Sentences Datei

Damit die neuen Sprachbefehle überhaupt erkannt werden können, mussten wir die Sprachbefehle in der Sentences.ini definieren. Wir entschieden uns dafür, dass wir für den Wecker eine extra [alarm.ini](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/rhasspy/profiles/de/intents/alarm.ini) anlegen würden, damit wir die Implementierung der einzelnen Features stärker voneinander trennen. Dadurch wurde unser Projekt übersichtlicher und wir gerieten weniger oft in die Situation, dass wir Merge Konflikte lösen mussten.

Bei der Definition der einzelnen Sentences bzw. Intents, stießen wir auf das Problem, dass Pocketsphinx nur Wörter erkennt, die explizit in einer Sentences.ini definitiert sind. Da wir nun aber sowohl die Zahlen 0 bis 23 für die Stunden, als auch 1 bis 59 für die Minuten benötigten, machten wir uns auf die Suche nach einer einfacheren Lösung als die Zahlen alle einzeln aufzuschreiben. Glücklicherweise bietet Rhasspy die Möglichkeit ein [Zahlenintervall](https://rhasspy.readthedocs.io/en/latest/training/#number-ranges) in der Form 0..23 bzw. 1..59 anzugeben. 

Als nächstes galt es die Herausforderung zu lösen, die gesprochenen Zahlen in Variablen zu übergeben. Hierzu kann man bei Rhasspy den Variablennamen nach dem entsprechenden Ausdruck in geschweifte Klammern schreiben. [Siehe offizielle Dokumentation](https://rhasspy.readthedocs.io/en/latest/training/#tags)
```
(0..23){alarm_hour} Uhr [(1..59){alarm_minute}]
```

Der so erhaltene Intent reagiert allerdings nicht auf alle Uhrzeiten. Beispielsweise könnten wir mit diesem Intent die Uhrzeit 01:12 nicht erkennen. Dies liegt daran, dass 0..23 für die Stunden nur das Wort "eins" enthält, nicht aber das Wort "ein". Der Intent musste also noch um das Wort "ein" erweitert werden, welches dann zu "1" konvertiert werden musste. Zur Konvertierung von "ein" zu "1" bedienten wir uns an der Möglichkeit [Substitutions](https://rhasspy.readthedocs.io/en/latest/training/#substitutions) zu verwenden. So änderte sich der Intent zu 
```
((0..23)|ein:1){alarm_hour} Uhr [(1..59){alarm_minute}]
```

Leider wurde die "1" nun als String gesehen und nicht wie alle anderen Zahlen als Integer. Damit wir später in der Verarbeitung des Intents mit einem einheitlichen Datentypen arbeiten konnten, mussten wir die "1" explizit casten. Dafür bietet uns Rhasspy ebenfalls eine [eigene schreibweise](https://rhasspy.readthedocs.io/en/latest/training/#converters) innerhalb der Sentences.ini. Der finale Satz, um eine Uhrzeit zu erkennen sieht so aus:
```
((0..23)|ein:1){alarm_hour!int} Uhr [(1..59){alarm_minute!int}] 
```

### Intent Handling

Es gibt mehrere Möglichkeiten wie man die Intents von rhasspy verarbeiten kann. [Siehe offizielle Dokumentation](https://rhasspy.readthedocs.io/en/latest/intent-handling/) 

Wir haben uns für die Möglichkeit der Websockets entschieden und einen Node-Red Workflow erstellt, welcher die Daten vom Websocket entgegennimmt und an die entsprechenden Workflows weiterleitet.

![Node Red Alarm Switch](/assets/NodeRedAlarmSwitch.png)


### Den Weckern Namen geben

Leider haben wir keine Möglichkeit gefunden in der sentences.ini eine Variable einzufügen, die mit einem beliebigen gesprochenen Wort befüllt werden kann. Wir mussten deshalb darauf verzichten den Weckern Namen zu geben. Aufgrund der daraus resultierenden schwierigeren Dialogführung mit dem Nutzer, haben wir uns dafür entschieden, dass man vorerst nur einen Wecker gleichzeitig anlegen kann. In der API ist allerdings schon alles so eingerichtet, dass in Zukunft relativ leicht auch mehrere Wecker gleichzeitig verwaltet werden können. Eine zukünftige Lösung für das Namensproblem wäre, eine Liste anzulegen, die die möglichen Weckernamen vorgibt. Hierzu könnte man auf die [Slots Lists](https://rhasspy.readthedocs.io/en/latest/training/#slots-lists) zurückgreifen.


### Timezone richtig einstellen

Damit der Wecker auch zur richtigen Uhrzeit Alarm schlägt, musste die Uhrzeit zwischen dem Raspberry und dem Flask-Container synchronisiert werden. Hierzu wurden "/etc/timezone:/etc/timezone:ro" und "/etc/localtime:/etc/localtime:ro" als Volume-Einträge des Flask-Services in der [docker-compose.yml](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/docker-compose.yml) hinzugefügt.


### Datenbank

Damit die Wecker auch nach einem Stromausfall noch funktionieren, haben wir uns dafür entschieden die Informationen in einer Datenbank zu speichern. Da wir nur sehr begrenzten Arbeitsspeicher zur Verfügung haben, fallen Datenbanksysteme wie MySQL weg. Wir könnten die Informationen des Weckers in einer Config-Datei speichern, gehen aber davon aus, dass wir bei späteren Features noch öfters eine Datenbank gebrauchen können. Deshalb haben wir uns für eine Verwaltung mit Sqlite entschieden, da diese weniger Arbeitsspeicher verbraucht und wir im Vergleich zu beispielsweise MongoDB viel mehr Erfahrung mit SQLite hatten.  


### Wecker triggern

Damit der Wecker zur richtigen Zeit ausgelöst wird, haben wir ein Flask Command erstellt, welches über die Konsole aufgerufen werden kann. Dieses überprüft, ob zur aktuellen Uhrzeit ein Wecker ausgelöst werden soll und löst diesen dann aus. 

Damit das Script keine Minute verpasst, aber gleichzeitig nicht durchgehend laufen muss, rufen wir dieses einmal pro Minute mithilfe eines [Cronjobs](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/src/api/crontab.txt) auf. Dieser Cronjob ruft dann lediglich den Befehl flask check-alarm auf. Damit die Cronjobs aktiv sind, mussten wir noch eine [entry.sh](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/src/api/entry.sh) zum [Flask-Dockerfile](https://github.com/th-koeln-intia/ip-sprachassistent-team1/blob/master/docker/flask/Dockerfile) hinzufügen.


### Weckton wiedergeben

Zur Weckton Wiedergabe hatten wir uns zuerst dazu entschieden, den Weckton über die Topic hermes/audioServer/default/playBytes/alarm-{id} auszulösen. Da der Weckton so allerdings nur einmal abgespielt wird, mussten wir uns etwas überlegen, um den Wecker unendlich oft in Schleife laufen zu lassen. Zuerst kam uns die Idee, die Dauer des Wecktons zu speichern und den Weckton in diesem Intervall immer wieder abzuspielen. Mit dieser Methode stößt man allerdings auf Probleme wenn man eine schlechte Verbindung zwischen der API, Mosquitto und Rhasspy hat. Dann kann es nämlich passieren, dass der Befehl zum Abspielen des Sounds bereits mehrere Sekunden braucht bis der Sound überhaupt abgespielt wird. Dadurch würde der nächste Durchlauf zu früh starten.  

Deshalb haben wir die Schleife so gebaut, dass sie nach dem Absenden des Tons die Topic "hermes/audioServer/default/playFinished" subscribed. Sobald dann die id im payload gleich der gesendeten alarm-id ist, kann man sich sicher sein, dass der vorherige Ton erfolgreich abgespielt wurde und man kann den nächsten Ton ausgeben. 


### Weckton abbrechen 

Leider fiel uns relativ spät auf, dass die Wake-Word Erkennung automatisch ausgeschaltet wird, wenn eine Audio-Ausgabe über rhasspy stattfindet [https://rhasspy.readthedocs.io/en/latest/wake-word/#mqtthermes](https://rhasspy.readthedocs.io/en/latest/wake-word/#mqtthermes). Das bedeutete für uns, dass wir entweder eine Pause zwischen den einzelnen Tonausgaben implementieren mussten oder die Tonausgabe nicht über Rhasspy steuern dürfen. Auf Grund der mangelnden Zeit und der vermutlichen weiteren Probleme mit Variante 2 entschieden wir uns für die Variante mit der eingebauten Pause zwischen den Sounds. Bei Variante 2 wären wir wahrscheinlich noch darauf gestoßen, dass das Wake-Word nicht erkannt wird durch die Hintergrundgeräusche des Wecktons. 

Die eigentliche Logik hinter dem Abbrechen-Intent ist hingegen relativ einfach. Sobald der Intent aktiviert wird, setzt die API den Status des Weckers auf inactive. Sobald nun der nächste Schleifendurchlauf zum Abspielen des Wecktons startet, wird überprüft ob der Status auf inactive ist. Sollte das der Fall sein, so bricht die Weckton-Schleife ab und setzt den Status des Weckers wieder auf active. 