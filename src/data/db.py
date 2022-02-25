from app import app
from flask_sqlalchemy import SQLAlchemy

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
        db.session.execute(sql, {"title":title, "url":url})
        db.session.commit()
    except Exception as e:
        return False

    return True

    
