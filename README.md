# Ausgangslage

## Funktion/Projektidee
Kursverwaltungs-Tool
Auf der Startseite ist es für die Teilnehmenden möglich sich an verschiedenen Kursen anzumelden.
Wenn der Kurs voll ist, ist es nicht mehr möglich sich anzumelden(der Kurs wird nicht mehr angezeigt).
Der Kursleiter hat die Möglichkeit sich einzuloggen und eine Liste der Teilnehmenden darzustellen. -> Export

## Workflow
### Dateneingabe
Die Daten werden vom Benutzer über das Webinterface eingegeben.
### Datenverarbeitung/Speicherung
Die eingegebenen Daten werden sofort verarbeitet und in der Kursverwaltung abgelegt.
Die Daten werden in einer JSON Datei aufbewahrt.

### Datenausgabe
Die Daten werden wieder über das Webinterface ausgegeben.
Je nach Aufwand könnte noch ein Export implementiert werden, der heruntergeladen werden kann. 


## Vorgehen
1. Ablaufdiagram zeichnen, welches definiert, welche Seiten und Funktionen definiert die benötigt werden
2. Erarbeiten der Datenstruktur -> 
    kurs_mgmt.py Funktion init_gen_kursliste, mithilfe dieser Funktion befülle ich initial meine JSON Datei, welche als weitere Grundlage dient.

## Feature Beschrieb

### Hauptseite / Main
- Anzeige aller Kurse, welche noch nicht voll sind
- Anmeldung am Kurs für teilnehmer

### Login
- Anmeldung mit User und Passwort, Passwort ist gespeichert als sha512 Hash
- Session mit Cookie wird erstellt.

### Kursleiter übersicht
- Anzeige aller Kurse
- Anzeige der angemeldeten Teilnehmer
- Löschen der Kurse
- Wenn der Kurs voll ist, wird er grün markiert