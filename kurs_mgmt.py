from json import dumps, loads
from datetime import date, time


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


kurse = init_gen_kursliste()

# print(len(kurse[4]))

with open("data/kursliste.json", "w") as kurs_file:
    kurs_file.write(dumps(kurse))

# with open("File/telebuch.json", "w") as telefonbuch_file:
# telefonbuch_file.write(dumps(telefonb))


# telefonb = loads(telefonbuch_file.read())
