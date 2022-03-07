import sqlite3
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


class DBManager:
    def __init__(self, env_location=None) -> None:
        if env_location:
            load_dotenv(env_location)
        if getenv("DEV_ENVIRON"):
            self.init_connection = self._init_connection_to_sqlite
        else:
            self.db = SQLAlchemy()
            self.init_connection = self._init_connection_to_sql_server

    def _init_connection_to_sqlite(self) -> None:
        """Init a connection to local database for testing"""
        self.connect = sqlite3.connect("mock_data.db")
        self.cursor = self.connect.cursor()

    def _init_connection_to_sql_server(self) -> None:
        """Set self.cursor to point to sqlalchemy session"""
        self.cursor = self.db.session

    def _generate_table(self, table: str) -> None:
        table_items = getenv(f"{table.upper()}_TABLE_COLUMNS").split(",")
        for i in range(len(table_items)):
            table_items[i] = table_items[i].split(";")
        sql = f"CREATE TABLE IF NOT EXISTS {table} ("
        for column_name, column_type in table_items:
            sql += column_name + " " + column_type + ", "
        sql = sql[:-2] + ")"
        self.cursor.execute(sql)

    def _generate_tables_to_sqlite(self) -> None:
        self.init_connection()
        self._generate_table("tips")
        self._generate_table("users")
        self.connect.commit()

    def get_all_tips(self) -> list:
        '''hakee tietokannasta kaikki vinkit'''
        self.init_connection()
        return self.cursor.execute("SELECT * FROM tips").fetchall()

    # refactor -> take tip info list instead of specifically title and url
    def add_tip(self, title: str, url: str, username: str) -> bool:
        '''yrittää lisätä tietokantaan uuden vinkin. Jos onnistuu = palauttaa True, jos ei = False'''
        if "" in [title, url, username] or None in [title, url, username] or not self.get_user(username):
            return False
        try:
            self.init_connection()
            self.cursor.execute("INSERT INTO tips VALUES (?, ?, ?)", (
                title,
                url,
                self.get_user(username)["user_id"])
            )  # further refactor to fit the .env usage here too
            self.connect.commit()
        except Exception as exception:
            print(exception)
            return False
        return True

    def add_user(self, username: str, hashed_password: str, admin: bool):
        '''Tallentaa uuden käyttäjän tietokantaan.
        Palauttaa dictionaryn, jossa user-id, käyttäjänimi ja admin jos onnistuu.
        Muutoin palauttaa False'''
        if "" in [username, hashed_password] or None in [username, hashed_password]:
            return False
        try:
            if getenv("DEV_ENVIRON"):
                self.cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?)",
                                    ("1", username, hashed_password, str(admin)))
                self.connect.commit()
                # hardcoded 3 -> but basically just because sqlite implementation is just for test
                data = {"user_id": 3, "username": username, "admin": admin}
            else:
                sql = """INSERT INTO
                    users (username, password, admin)
                    VALUES (:username, :password, :admin)
                    RETURNING id, username, admin"""
                res = self.cursor.execute(
                    sql, {"username": username, "password": hashed_password, "admin": admin})
                self.connect.commit()
                data = {}
                data["user_id"], data["username"], data["admin"] = res
            if not data:
                return False
            return data
        except Exception as exception:
            # Pitäisi löytää mikä tietty exception tässä tulee ja testata vain sitä
            return exception

    def get_user(self, username: str) -> dict:
        '''Tarkistaa, löytyykö tietokannasta usernamea vastaava käyttäjä.
        Jos löytyy, palauttaa sanakirjan, jossa id, käyttäjänimi ja salasanahash
        Jos ei, palauttaa False
        '''
        try:
            sql = "SELECT * FROM users WHERE username=(:username)"
            user = self.cursor.execute(sql, {"username": username})
            self.connect.commit()
            data = {}
            for row in user:
                data["user_id"] = row[0]
                data["username"] = row[1]
                data["password"] = row[2]
            if not data:
                return False
            return data
        except Exception:  # Pitäisi löytää mikä tietty exception tässä tulee ja testata vain sitä
            return False

    def get_all_users(self) -> dict:
        """Hakee kaikki käyttäjät tietokannasta sanakirjana muodossa {'user_id': 'username'}

        Returns:
            dict: Kaikkien tietokannan käyttäjien ID:t ja käyttäjänimet
        """
        try:
            sql = "SELECT id, username FROM users"
            users = self.cursor.execute(sql)
            self.connect.commit()
            data = {}
            for row in users:
                data[row[0]] = row[1]
            if not data:
                return False
            return data
        except Exception:  # Pitäisi löytää mikä tietty exception tässä tulee ja testata vain sitä
            return False
