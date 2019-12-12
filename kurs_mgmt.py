from json import dumps, loads
from datetime import datetime
from user_functions import load_user

# Constants
COURSELIST_FILENAME = "kursliste"  # Name des Kurslistenfiles
STUDENT_LIST_LOCATION = 7  # Stelle des Teilnehmer Arrays im kursliste dict


# Für die initiale Generierung einer Kursliste kann diese Funktion verwendet werden
def init_gen_kursliste():
    # Key ist der Kursname -> Problem Kurse mit gleichen Namen sind nicht möglich
    kursliste = {"Schwimmen": ["In diesem Kurs lernt man Schwimmen",  # Beschreibung
                               (2020, 6, 24),  # Datum
                               (18, 00, 00),  # Zeit
                               "Schwimmbad Chur",  # Ort
                               3,  # MIN Teilnehmer Zahl
                               10,  # MAX Teilnehmer Zahl
                               "Hans Friederich",  # Kursleiter
                               # Teilnehmer Liste
                               [["Michael", "Greuter", (1999, 4, 11), "Heiliger Weg 2", "Chur"],
                                ["Vanessa", "Herbst", (1998, 2, 21), "Nichtheilig 2", "Flims"]
                                ]],
                 "Mountainbiken": ["Fahrrad fahren in den Bergen",
                                   (2020, 9, 2),
                                   (17, 30, 00),  # Zeit
                                   "Laax Talstation",
                                   2,
                                   8,
                                   "Sybille Tschan",
                                   [["Mark", "Neumann", (1998, 2, 1), "Grosse Strasse 132", "Landquart"],
                                    ["Laura", "Graf", (1997, 12, 21), "Bikerweg 12", "Thusis"]
                                    ]]
                 }

    return kursliste


def save_json(filename, save_file):
    ####
    # Funktion um das DICT als JSON auf dem Filesystem zu speichern
    # Filename = Name des Files in welches gespeichert werden soll
    # save_file = Beinhaltet das dict das gespeichert wird
    ####
    url = str("data/" + filename + ".json")
    with open(url, "w") as file:
        file.write(dumps(save_file))


def load_json(filename):
    ####
    # Lädt ein dict aus dem JSON file, welches den filenamen hat welches übergeben wurde im pfad /data
    ####
    url = str("data/" + filename + ".json")
    with open(url, "r") as file:
        loaded_file = loads(file.read())
    return loaded_file


def get_course_list():
    # gibt die aktuelle Kursliste zurück
    return load_json(COURSELIST_FILENAME)


def save_course_list(courselist):
    # Speichern der übergebenen Kursliste
    save_json(COURSELIST_FILENAME, courselist)


# Neuer Student wird zu einem Kurshinzugefügt
def add_student(sign_vorname, sign_nachname, sign_geb, sign_address, sign_ort, course):
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


# Löschen eines Kurses
def del_kurs(kursname):
    # Abrufen der aktuellen Kursliste
    courselist = get_course_list()

    # Entfernen des Kurses
    del courselist[kursname]
    # Speichern der aktualisieren Kursliste
    save_course_list(courselist)

# Unten stehende Zeile auskommentieren damit die initialen Kurse beim start generiert werden
# save_json(COURSELIST_FILENAME, init_gen_kursliste())

# init_gen_kursliste()
