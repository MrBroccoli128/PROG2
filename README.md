# Ausgangslage

## Funktion/Projektidee
Kursverwaltungs-Tool
Auf der Startseite ist es für die Teilnehmenden möglich sich an verschiedenen Kursen anzumelden.
Wenn der Kurs voll ist, ist es nicht mehr möglich sich anzumelden(der Kurs wird nicht mehr angezeigt).
Der Administrator hat die Möglichkeit sich einzuloggen. In diesem Bereich kann er Kurse erstellen, löschen und eine Liste der Teilnehmenden anschauen. 

## Workflow
### Dateneingabe
Die Daten werden vom Benutzer über das Webinterface eingegeben.
### Datenverarbeitung/Speicherung
Die eingegebenen Daten werden sofort verarbeitet und in der Kursverwaltung abgelegt.
Die Daten werden in einer JSON Datei aufbewahrt.

### Datenausgabe
Die Daten werden wieder über das Webinterface ausgegeben.


## Vorgehen
1. Ablaufdiagram zeichnen(Papier), welches definiert, welche Seiten und Funktionen definiert die benötigt werden
2. Erarbeiten der Datenstruktur
3. Umsetzung der Hauptseite mit der Anzeige der Kurse
4. Umsetzung der Kursanmeldung durch einen Studenten
5. Bauen der Login Page
6. Kursleiterseite erstellen
7. Administrative Funktionen für Kursleiter umsetzen
8. Dokumentation, verbesserungen

## Featurebeschrieb

### Hauptseite / Main
- Anzeige aller Kurse, welche noch nicht voll sind
- Anmeldung am Kurs für Teilnehmer

### Login
- Anmeldung mit User und Passwort, Passwort ist gespeichert als sha512 Hash
- Session mit Cookie wird erstellt.
- Username: Administrator Passwort: passwort

### Kursleiter übersicht
- Anzeige aller Kurse
- Anzeige der angemeldeten Teilnehmer
- Löschen der Kurse
- Wenn der Kurs voll ist, wird er grün markiert

## Bedinungsanleitung
Die Applikation benötigt keine speziellen Schritte zur Installation. Vom / Verzeichnis wird man auf die Startseite weitergeleitet.

Startseite:
- Durch einen Klick auf den Button Anmelden kann sich man sich bei jeweiligen Kurs anmelden.
- Um zur Administratorensicht zu gelangen muss man sich über die Schaltfläche "Login" anmelden. -> Benutzername: Administraator Password: passwort

Kursleiter Übersicht:
Nach der Authentifizierung können die Kurse administriert werden. -> Durch die Anmeldung wird ein Cookie erstellt, d.h solange man nicht auf Logout klickt steht diese Übersicht zur Verfügung. 
Wie das Label "Neuen Kurs erstellen" bereits vermuten lässt, kann über diesen Button ein neuer Kurs angelegt werden.
Der Button Teilnehmer zeigt die Anmeldungen für den jeweiligen Kurs an.
Falls der Kurs nicht statt findet kann er auch gelöscht werden.
Wenn ein Kurs grün umrahmt ist bedeutet dies das der Kurs voll ist und für die normalen Benutzer nicht mehr angezeigt wird.


Zurücksetzen der Applikation
Kurse:
Um die Applikation auf die Standard Kurse, welche bei der Abgabe vorhanden waren zurückzusetzen, kann um kurs_mgmt.py 
Zu unterst die Zeile "save_json(COURSELIST_FILENAME, init_gen_kursliste())" auskommentiert werden.
# Reflexion
Zu Anfang musste ich zuerst den Umgang mit Flask lernen. Das hatte zur folge das ich sehr viele HTML Seiten hatte. 
Nachdem ich das Ganze etwas besser verstande hatte konnte ich die meisten Funktionen der Applikation auf 2 HTML Seiten abbilden.

Mir hat das Projekt sehr gefallen, jedoch würde ich mir nächstes mehr Zeit nehmen die Datenstruktur zu planen.
Ein weiteres Problem war das ich zu Anfang nicht alles bis zu Ende durchgedacht habe. Dies führte dazu das ich einige Mal zurück musste.
Mein Ziel war es stets das meine Applikation skalierbar und ausbaubar bleibt. Dies ist mir an einen Orten besser gelungen als an anderen.