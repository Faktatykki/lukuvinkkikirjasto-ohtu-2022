from flask_sqlalchemy import SQLAlchemy

class DBManager():
    def __init__(self, app):
        self.db = SQLAlchemy(app)

    def get_all_tips(self):
        '''Hakee tietokannasta kaikki vinkit'''
        sql = self.db.session.execute("SELECT title, url FROM tips")
        result = sql.fetchall()
        return result

    def add_tip(self, title: str, url: str) -> bool:
        '''Yrittää lisätä tietokantaan uuden vinkin. Jos onnistuu = palauttaa True, jos ei = False'''
        try:
            sql = "INSERT INTO tips (title, url) VALUES (:title, :url)"
            self.db.session.execute(sql, {"title": title, "url": url})
            self.db.session.commit()
        except Exception as exception:
            print(exception)
            return False
        return True
