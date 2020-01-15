from passlib.hash import sha512_crypt
from json import dumps, loads

# Constants
PASSWD_FILEPATH = "data/passwd.json"  # Pfad zur JSON datei


# Initiale User Datenbank
# Diese Funktion kann für die Initialisierung verwendet werden. Damit befindet sich nur der Admin User im system
def create_init_userdb():
    ###
    # Summary:
    #   Initiale Userliste generieren
    # Args:
    #   none
    # Return:
    #   none
    ###

    users = {"Administrator": [sha512_crypt.hash('passwort'),
                               "Admini",  # Vorname
                               "Strator"]}  # Nachname

    with open(PASSWD_FILEPATH, "w") as file:
        file.write(dumps(users))

# Gibt die aktuelle Userliste zurück
def load_user():
    ###
    # Summary:
    #   Lädt die aktuelle Userliste aus dem json file passwd.json
    # Args:
    #   none
    # Return:
    #   aktuelle kursliste als dict
    ###

    with open(PASSWD_FILEPATH, "r") as file:
        loaded_file = loads(file.read())
    return loaded_file


def verify_login(user, password):
    ###
    # Summary:
    #   Diese Funktion überprüft die eingegebenen Login Parameter und checkt ob sie im passwd.json vorhanden sind
    # Args:
    #   user(string) = Eingegebner Username
    #   password(string) = Eingegebenes Passwort im cleartext
    # Return:
    #   Boolscher Wert: True = Credentials sind korrekt; False = Credentials sind falsch
    ###

    # Wenn irgendetwas falsch ist soll False zurückgegeben werden. z.B wenn User nicht gefunden wird
    # deshalb wird ein try verwendet, damit wird der Fehler bei einem nicht existierenden Key im Dict abgefangen
    try:
        f_info = load_user()
        for k, v in f_info.items():
            if k == user:
                s_user = k
                s_pass = v[0]
                # Wenn der Username und der Passworthash korrekt sind wird True zurückgegeben
        if s_user == user and sha512_crypt.verify(password, s_pass) is True:
            return True
        else:
            # Wenn die Daten falsch ist -> False
            return False
    # Falls im während der Überprüfung des User, Passwort ein Fehler passiert, gibt es kein erfolgreiches login
    except:
        return False
