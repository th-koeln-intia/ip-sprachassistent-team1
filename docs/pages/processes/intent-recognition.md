---
title: Intent Recognition
permalink: /results/intent-recognition/
subtitle: Entwicklungsergebnisse zur Implementierung der Intent Recognition
layout: page
show_sidebar: false
menubar: docs_menu
---

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