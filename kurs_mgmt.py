from json import dumps, loads
from datetime import datetime
from user_functions import load_user

# Constants
COURSELIST_FILENAME = "kursliste"  # Name des Kurslistenfiles
STUDENT_LIST_LOCATION = 7  # Stelle des Teilnehmer Arrays im kursliste dict

def init_gen_kursliste():
    ###
    # Summary:
    #  Für die initiale Generierung einer Kursliste kann diese Funktion verwendet werden
    # Args:
    #   none
    # Return:
    #   kursliste (dict): Initiale Kursliste
    ###
    # Key ist der Kursname -> Problem Kurse mit gleichen Namen sind nicht möglich
    kursliste = {"Schwimmen": ["In diesem Kurs lernt man Schwimmen",  # Beschreibung
                               (20, 4, 2020),  # Datum
                               (18, 45, 00),  # Zeit
                               "Schwimmbad Chur",  # Ort
                               3,  # MIN Teilnehmer Zahl
                               10,  # MAX Teilnehmer Zahl
                               "Hans Friederich",  # Kursleiter
                               # Teilnehmer Liste
                               [["Michael", "Greuter", (1999, 4, 11), "Heiliger Weg 2", "Chur"],
                                ["Vanessa", "Herbst", (1998, 2, 21), "Nichtheilig 2", "Flims"]
                                ]],
                 "Mountainbiken": ["Fahrrad fahren in den Bergen",
                                   (23, 9, 2020),
                                   (17, 30, 00),  # Zeit
                                   "Bahnhof Chur",
                                   2,
                                   8,
                                   "Sybille Tschan",
                                   [["Mark", "Alterman", (1998, 2, 1), "Kleine Strasse 13", "Felsberg"],
                                    ["Margrit", "chen", (1997, 12, 21), "Bikerweg 12", "Davos"]
                                    ]],
                 "Freeride Grundkurs": ["In diesem Kurs lernt man die Grundlagen des Freeriden",
                                        (4, 2, 2020),
                                        (9, 15, 00),  # Zeit
                                        "Laax Talstation",
                                        3,
                                        5,
                                        "Sybille Tschan",
                                   [["Mark", "Neumann", (1998, 2, 1), "Grosse Strasse 132", "Landquart"],
                                    ["Laura", "Graf", (1997, 12, 21), "Skiweg 12", "Thusis"],
                                    ["Rudy", "Hemp", (1987, 11, 1), "Irgendwo 1", "Cazis"],
                                    ["Weihnachts", "Mann", (1872, 11, 27), "Eisblock 65", "Nordpol"],
                                    ["Heiko", "Hirsch", (1987, 4, 7), "Strasse 44", "Vaduz"]
                                    ]]
                 }

    return kursliste


def save_json(filename, save_file):
    ###
    # Summary:
    #  Funktion um das DICT als JSON auf dem Filesystem zu speichern
    # Args:
    #   filename(string) = Filename des zu speichernden Files
    #   save_file(dict) = aktuelles, noch dict, welches als json gespeichert werden soll
    # Return:
    #   none
    ###
    url = str("data/" + filename + ".json")
    with open(url, "w") as file:
        file.write(dumps(save_file))


def load_json(filename):
    ###
    # Summary:
    #  Lädt ein dict aus dem JSON file, welches den filenamen hat welches übergeben wurde im pfad /data
    # Args:
    #   filename(string) = Filename des zu ladenden Files
    # Return:
    #   loaded_file(dict) = Geladenes Json File als dictionary
    ###
    url = str("data/" + filename + ".json")
    with open(url, "r") as file:
        loaded_file = loads(file.read())
    return loaded_file


def get_course_list():
    ###
    # Summary:
    #  Gibt die aktuelle Kursliste zurück
    # Args:
    #   none
    # Return:
    #   aktuelle kursliste als dict
    ###
    return load_json(COURSELIST_FILENAME)


def save_course_list(courselist):
    ###
    # Summary:
    #  Übergibt die aktuelle Kursliste zum speichern
    # Args:
    #   aktuelle kursliste als dict
    # Return:
    #   none
    ###
    save_json(COURSELIST_FILENAME, courselist)


def add_student(sign_vorname, sign_nachname, sign_geb, sign_address, sign_ort, course):
    ###
    # Summary:
    #  # Neuer Student wird zu einem Kurs hinzugefügt
    # Args:
    #   sign_vorname(string) : Vorname
    #   sign_nachname(string) : Nachname
    #   sign_geb(string) : Geburtstagsdatum im Format Y-m-d als String
    #   sign_address(string) : Adresse
    #   sign_ort(string) : Heimatort
    #   course(string) : Name des Kurses (Key des dict)
    # Return:
    #   none
    ###

    # Abholen der aktuellen Daten
    courselist = get_course_list()

    # Formatierung des eingegeben Geburtsdatums in einen tuple
    geb = tuple(str(datetime.strptime(sign_geb, '%Y-%m-%d').strftime('%d/%m/%Y')).split('/'))

    # Zusammensetzen aller Informationen zu einer Liste
    temp_list = [sign_vorname, sign_nachname, geb, sign_address, sign_ort]

    # Update des Dicts
    courselist[course][STUDENT_LIST_LOCATION].append(temp_list)

    # Speichern auf das Filesystem
    save_course_list(courselist)


def add_kurs(i_titel, i_beschreibung, i_datum, i_zeit, i_minT, i_maxT, i_ort, kursleiter):
    ###
    # Summary:
    #  Neuen Kurs hinzufügen
    # Args:
    #   i_titel(string) : Titel
    #   i_beschreibung(string) : Kursbeschreibung
    #   i_datum(string) : Datum im Format Y-m-d
    #   i_zeit(string) : Zeit
    #   i_minT(integer) : Minimale Teilnehmerzahl
    #   i_maxT(integer) : Maximale Teilnehmerzahl
    #   i_ort(string) : Ort
    #   kursleiter(string) : Username des Kursleiters
    # Return:
    #   none
    ###

    # Laden der aktuellen Benutzerliste
    user_list = load_user()
    # Laden der aktuellen Kursliste
    courselist = get_course_list()

    # Name des Kursleiters wird aus der Userliste geholt
    l_name = str(user_list[kursleiter][1] + " " + user_list[kursleiter][2])
    # Datum formatieren und als Tuple speichern
    datum = tuple(str(datetime.strptime(i_datum, '%Y-%m-%d').strftime('%d/%m/%Y')).split('/'))
    # Zeitstring zu Tuple machen
    zeit = tuple(i_zeit.split(":"))
    # Zusammensetzen aller Informationen
    temp_list = [i_beschreibung, datum, zeit, i_ort, i_minT, i_maxT, l_name, []]

    # Speichern des neuen Kurses
    courselist[i_titel] = temp_list

    # Speichern der aktualisieren Kursliste
    save_course_list(courselist)


def del_kurs(kursname):
    ###
    # Summary:
    #  Löscht einen Kurs aus der aktuellen Kursliste
    # Args:
    #   kursname(string) : Name des Kurses, welcher dem Key im dict entspricht
    # Return:
    #   none
    ###

    # Abrufen der aktuellen Kursliste
    courselist = get_course_list()

    # Entfernen des Kurses
    del courselist[kursname]
    # Speichern der aktualisieren Kursliste
    save_course_list(courselist)

# Unten stehende Zeile auskommentieren damit die initialen Kurse beim start generiert werden
# save_json(COURSELIST_FILENAME, init_gen_kursliste())

