from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

def get_all_tips():
    sql = db.session.execute("SELECT title, url FROM tips")
    result = sql.fetchall()

    return result