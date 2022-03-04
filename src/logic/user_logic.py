from werkzeug.security import check_password_hash, generate_password_hash
from data import db
from entities import user


def signup(username:str, password:str, admin=False):
    '''Pyytää data-layeria tallentamaan uuden käyttäjän. Palauttaa käyttäjäolion jos onnistui'''
    hashed_password = generate_password_hash(password)
    res=db.add_user(username, hashed_password, admin)
    try:
        if "user_id" in res:
            # print("Tietokanta palauttaa1:", res["user_id"], res["username"], res["admin"])
            return signin(username, password)
    except:
        pass
    return res

def signin(username:str, password:str):
    '''Palauttaa User-olion, jos kirjautuminen onnistuu'''
    # Jere - alkuperäinen salasana on hashattu werkzeug-kirjaston generate_password_hash-metodilla
    # Sun pitää siksi käyttää saman kirjaston check_password_hash metodia,
    # kun tsekkaat salasalan oikeellisuutta.

    user_in_database = db.get_user(username)
    if user_in_database:
        passwords_match = check_password_hash(user_in_database["password"], password)
        if passwords_match:
            new_user = user.User(user_in_database["user_id"], user_in_database["username"])
            return new_user
    return False
