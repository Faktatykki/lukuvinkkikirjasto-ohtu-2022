from data import db
from entities import user
from werkzeug.security import check_password_hash, generate_password_hash

def signup(username:str, password:str, admin=False):
    '''Pyytää data-layeria tallentamaan uuden käyttäjän. Palauttaa käyttäjäolion jos onnistui'''
    hashed_password = generate_password_hash(password)
    res=db.add_user(username, hashed_password, admin)
    if username in res:
        return signin(username, password)
    return res

def signin(username:str, password:str):
    '''Palauttaa User-olion, jos kirjautuminen onnistuu'''
    # Jere - alkuperäinen salasana on hashattu werkzeug-kirjaston generate_password_hash-metodilla
    # Sun pitää siksi käyttää saman kirjaston check_password_hash metodia kun tsekkaat salasalan oikeellisuutta. 
    
    test_user=user.User(1, "test_user") #Tämä on vain testausta varten, jotta saan testattua signup-funktiota.
    return test_user 