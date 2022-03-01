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
    '''Tallentaa uuden käyttäjän tietokantaan. Palauttaa user-id:n ja käyttäjänimen, jos onnistuu. Muutoin palauttaa False'''
    try:
        sql = "INSERT INTO users (username, password) VALUES (:username, :password) RETURNING id, username, admin"
        res=db.session.execute(sql, {"username": username, "password": hashed_password})
        db.session.commit()
        print(res)
        return res
    except Exception as exception:
        print(exception)
        return exception