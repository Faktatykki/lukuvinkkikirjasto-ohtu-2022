from sqlalchemy import false
from werkzeug.security import check_password_hash, generate_password_hash
from data import db
from entities import user


def signup(username:str, password:str, admin=False):
    '''Pyytää data-layeria tallentamaan uuden käyttäjän. Palauttaa käyttäjäolion jos onnistui'''
    hashed_password = generate_password_hash(password)
    res=db.add_user(username, hashed_password, admin)
    try:
        print('onko resissä user id', res)
        if "user_id" in res:
            # print("Tietokanta palauttaa1:", res["user_id"], res["username"], res["admin"])
            return signin(username, password)
    except:
        pass
    return res

def signin(username:str, password:str):
    '''Palauttaa User-olion, jos kirjautuminen onnistuu'''
    user_in_database = db.get_user(username)
    print('user_in_database', user_in_database)
    if user_in_database:
        passwords_match = check_password_hash(user_in_database["password"], password)
        print('passwords_match',passwords_match)
        if passwords_match:
            new_user = user.User(user_in_database["user_id"], user_in_database["username"])
            print('nyy user',new_user)
            return new_user
    return False
