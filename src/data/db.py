from xmlrpc.client import boolean
from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)


def get_all_tips():
    '''hakee tietokannasta kaikki vinkit'''

    sql = db.session.execute("SELECT title, url FROM tips")
    result = sql.fetchall()

    return result


def add_tip(title: str, url: str) -> bool:
    '''yrittää lisätä tietokantaan uuden vinkin. Jos onnistuu = palauttaa True, jos ei = False'''
    try:
        sql = "INSERT INTO tips (title, url) VALUES (:title, :url)"
        db.session.execute(sql, {"title": title, "url": url})
        db.session.commit()
    except Exception as exception:
        print(exception)
        return False
    return True

def add_user(username:str, hashed_password:str, admin:boolean):
    '''Tallentaa uuden käyttäjän tietokantaan.
    Palauttaa dictionaryn, jossa user-id, käyttäjänimi ja admin jos onnistuu.
    Muutoin palauttaa False'''

    try:
        sql = "INSERT INTO users (username, password, admin) VALUES (:username, :password, :admin) RETURNING id, username, admin"
        res=db.session.execute(sql, {"username": username, "password": hashed_password, "admin": admin})
        db.session.commit()
        data={}
        for row in res:
            data["user_id"]=row[0]
            data["username"]=row[1]
            data["admin"]=row[2]
        return data
    except Exception as exception:
        return exception

def get_user(username: str):
    '''
        Tarkistaa, löytyykö tietokannasta usernamea vastaava käyttäjä.
        Jos löytyy, palauttaa sanakirjan, jossa id, käyttäjänimi ja salasanahash
        Jos ei, palauttaa False
    '''
    try:
        sql = "SELECT * FROM users WHERE username=(:username)"
        user = db.session.execute(sql, {"username": username})
        db.session.commit()
        data = {}
        for row in user:
            data["user_id"]=row[0]
            data["username"]=row[1]
            data["password"]=row[2]
        return data
    except Exception:
        return False


