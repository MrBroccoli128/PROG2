# Ausgangslage

## Funktion/Projektidee
Kursverwaltungs-Tool
Auf der Startseite ist es für die Teilnehmenden möglich sich an verschiedenen Kursen anzumelden.
Der Kursleiter hat die Möglichkeit sich einzuloggen und eine Liste der Teilnehmenden darzustellen. -> Export
Durch mein persönliches Intresse werde ich versuchen eine saubere Userverwaltung zu erstellen.
## Workflow

### Dateneingabe
Die Daten werden vom Benutzer über das Webinterface eingegeben.
### Datenverarbeitung/Speicherung
Die eingegebenen Daten werden sofort verarbeitet und in der Kursverwaltung abgelegt.
Die Daten werden in einer JSON Datei aufbewahrt.

### Datenausgabe
Die Daten werden wieder über das Webinterface ausgegeben.
Je nach Aufwand könnte noch ein Export implementiert werden, der heruntergeladen werden kann. 


### Vorgehen
1. Ablaufdiagram zeichnen, welches definiert, welche Seiten und Funktionen definiert die benötigt werden
2. Erarbeiten der Datenstruktur -> 
    kurs_mgmt.py Funktion init_gen_kursliste, mithilfe dieser Funktion befülle ich initial meine JSON Datei, welche als weitere Grundlage dient.
