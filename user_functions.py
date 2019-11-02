from passlib.hash import sha512_crypt
from json import dumps, loads

PASSWD_FILEPATH = "data/passwd.json"


def create_init_userdb():
    users = {"Administrator": [sha512_crypt.hash('passwort'),
                               "Admini", #  Vorname
                               "Strator"]} #  Nachname

    with open(PASSWD_FILEPATH, "w") as file:
        file.write(dumps(users))


def load_user():
    with open(PASSWD_FILEPATH, "r") as file:
        loaded_file = loads(file.read())

    return loaded_file


def verify_login(user, password):
    # Wenn irgendetwas falsch ist soll False zurückgegeben werden. z.B wenn User nicht gefunden wird
    try:
        f_info = load_user()
        for k, v in f_info.items():
            if k == user:
                s_user = k
                s_pass = v[0]
        if s_user == user and sha512_crypt.verify(password, s_pass) is True:
            return True
        else:
            return False

    except:
        return False


def create_user(username, password):

    c_users = load_user()

    if username not in c_users.keys():
        c_users = load_user()
        return True

    else:
        return False

print(verify_login("Administrator", "passwort"))
# create_init_userdb()


