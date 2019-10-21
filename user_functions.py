from passlib.hash import sha512_crypt
from json import dumps, loads

PASSWD_FILEPATH = "data/passwd.json"


def create_init_userdb():
    users = {"Administrator": sha512_crypt.hash('passwort')}

    with open(PASSWD_FILEPATH, "w") as file:
        file.write(dumps(users))


def load_user(username):
    with open(PASSWD_FILEPATH, "r") as file:
        loaded_file = loads(file.read())

    return loaded_file


def verify_login(user, password):
    # Wenn irgendetwas falsch ist soll False zurückgegeben werden.
    try:
        f_info = load_user(user)
        for k, v in f_info.items():
            if k == user:
                s_user = k
                s_pass = v
        if s_user == user and sha512_crypt.verify(password, s_pass) is True:
            return True
        else:
            return False

    except:
        return False


def create_user(username, password):
    with open(PASSWD_FILEPATH, "w") as file:
        file.write(dumps(save_file))

# create_init_userdb()


