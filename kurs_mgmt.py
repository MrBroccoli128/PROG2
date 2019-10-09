from json import dumps, loads
from datetime import date, time

KURSLISTE_FILENAME = "kursliste"

def init_gen_kursliste():
    # Key ist der Kursname -> Problem Kurse mit gleichen Namen sind nicht möglich
    kursliste = {"Schwimmen": ["In diesem Kurs lernt man Schwimmen",  # Beschreibung
                               (2020, 6, 24),  # Datum
                               (18, 0, 0),  # Zeit
                               "Schwimmbad Chur",  # Ort
                               3,  # MIN Teilnehmer Zahl
                               10,  # MAX Teilnehmer Zahl
                               "Hans Friederich",  # Kursleiter
                               [["Michael", "Greuter", (1999, 4, 11), "Heiliger Weg 2", "Chur"],
                                ["Vanessa", "Herbst", (1998, 2, 21), "Nichtheilig 2", "Flims"]
                                ]],
                 "Mountainbiken": ["Fahrrad fahren in den Bergen",
                                   (2020, 9, 2),
                                   (17, 30, 0),  # Zeit
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

    return load_json(KURSLISTE_FILENAME)


save_json(KURSLISTE_FILENAME, init_gen_kursliste())
