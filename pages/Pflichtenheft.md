# Pflichtenheft

## Interaktive Biochemie Lernplattform


#### Entwickler:
* Kira Främbs
* Rustam Gilyazev
* Beatrice Wagner


### 1. Zielbestimmung

   #### Musskriterien:
   * Das Produkt gibt eine Übersicht über die separaten Reaktionen und Reaktionsketten der biochemischen Vorgänge einer Zelle.
   * Dem Entwickler soll es möglich sein, neue Reaktionen und Reaktionsketten in das Programm einzufügen.
   * Der Benutzer soll sein Wissen anhand kleiner Tests prüfen können.
   #### Wunschkriterien:
   * Der Benutzer soll sein Wissen anhand kleiner Tests prüfen können.
   * Die Richtigkeit der gebildeten Reaktionen soll überprüft werden.
   #### Abgrenzungskriterien:
   * Das Produkt soll keine chemischen Grundlagen erklären. Diese werden zur Benutzung vorausgesetzt. 

### 2. Produkteinsatz:

   #### Anwendungsgebiet

   * Das Produkt soll eine Lernhilfe im Bereich der Biochemie darstellen. Erlerntes Wissen soll durch mit Hilfe der Software getestet und vertieft werden können.
   
   #### Zielgruppe:

   * Das Produkt ist für Schüler und Studenten bestimmt, die das Fach Biochemie lernen.
   * Es kann außerdem von Lehrenden als Ergänzung zum Lehrstoff dienen.
   
   #### Betriebsbedingungen:
    
   * Da es sich um eine Lernplattform handelt, sollte die Nutzung in einer ruhigen Umgebung stattfinden.


### 3. Produktumgebung

   * Python 3.7
   * PyQt5 Designer
   
### 4. Produkt-Funktionen


   * F10: Der Benutzer soll die dargestellten biochemischen Reaktionen und Reaktionsketten einsehen können.
   * F20: Der Benutzer kann neue Reaktionsketten erstellen.
   * F30: Das Programm kann neue Bilder von Strukturformeln erstellen.
    
### 5. Produkt-Daten

   * Das Produkt enthält alle für die dargestellten biochemischen Reaktionswege nötigen Daten.
   * D10: Jeder dargestellte Reaktionsweg hat einen Namen.
   * D20: Jeder Reaktionsweg enthält 1 bis n angeordnete Reaktionen und die beteiligten Enzyme.
   * D30: Jede Reaktion besteht aus mindestens einem Edukt und mindestens einem Produkt. Die inneren Produkte bilden die Edukte der jeweils darauffolgenden Reaktion.
   * D40: Edukte und Produkte sind Moleküle. Diese bestehen aus mindestens einem Objekt der Klasse Bond.

### 6. Produkt-Leistungen

   * L10: Das Erstellen der Bilder soll nicht länger als 6 Sekunden dauern.
    
### 7. Benutzeroberfläche

   * Die Bedienung erfolgt über die Maus.
   * Der Benutzer kann durch die Reaktionsketten scrollen.
   * Neue Reaktionen werden über die Tastatur eingegeben.

### 8. Qualtitätsbestimmung

Produktqualität | Sehr gut | Gut | Normal | Nicht relevant
--------------- | -------- | --- | ------ | --------------
Angemessenheit | | X | | 
Richtigkeit | X | | | 
Sicherheit | | | X | 
Fehlertoleranz | | X | | 
Wiederherstellbarkeit | | | X | 
Verständlichkeit | X | | | 
Erlernbarkeit | X | | | 
Bedienbarkeit | X | | | 
Modifizierbarkeit | | X | | 
Stabilität | | | X | 
Anpassbarkeit | | | X | 

### 9. Glossar

* https://github.com/Kiratsuwa/biochemistry/blob/master/pages/dictionary.md 
