from werkzeug.security import check_password_hash, generate_password_hash
from data.db import DBManager
from entities.user import User


class UserLogic:
    def __init__(self, db):
        self.db = db

    def signup(self, username: str, password: str, admin=False):
        '''Pyytää data-layeria tallentamaan uuden käyttäjän. Palauttaa käyttäjäolion jos onnistui'''
        if username in [None, ""] or password in [None, ""]:
            return False
        hashed_password = generate_password_hash(password)
        res = self.db.add_user(username, hashed_password, admin)
        try:
            if "user_id" in res:
                # print("Tietokanta palauttaa1:", res["user_id"], res["username"], res["admin"])
                return self.signin(username, password)
        except:  # if we need to use except here it should not be without defining what kind of error
            pass
        return res

    def signin(self, username: str, password: str):
        '''Palauttaa User-olion, jos kirjautuminen onnistuu'''
        # Jere - alkuperäinen salasana on hashattu werkzeug-kirjaston generate_password_hash-metodilla
        # Sun pitää siksi käyttää saman kirjaston check_password_hash metodia,
        # kun tsekkaat salasalan oikeellisuutta.

        user_in_database = self.db.get_user(username)
        if user_in_database:
            passwords_match = check_password_hash(
                user_in_database["password"], password)
            if passwords_match:
                new_user = User(
                    user_in_database["user_id"], user_in_database["username"])
                return new_user
        return False
