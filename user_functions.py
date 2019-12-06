from passlib.hash import sha512_crypt
from json import dumps, loads

# Constants
PASSWD_FILEPATH = "data/passwd.json"  # Pfad zur JSON datei


# Initiale User Datenbank
# Diese Funktion kann für die Initialisierung verwendet werden. Damit befindet sich nur der Admin User im system
def create_init_userdb():
    users = {"Administrator": [sha512_crypt.hash('passwort'),
                               "Admini", #  Vorname
                               "Strator"]} #  Nachname

    with open(PASSWD_FILEPATH, "w") as file:
        file.write(dumps(users))


create_init_userdb()
# Gibt die aktuelle Userliste zurück
def load_user():
    with open(PASSWD_FILEPATH, "r") as file:
        loaded_file = loads(file.read())

    return loaded_file


# Diese Funktion überprüft die eingegebenen Login Parameter
# Und gibt nur bei richtigem Usernamen und Passwort ein True zurück
def verify_login(user, password):
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
            return False
    # Falls im Try ein Fehler passiert, False
    except:
        return False


def create_user(username, password):

    c_users = load_user()

    if username not in c_users.keys():
        return True

    else:
        return False



