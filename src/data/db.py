import sqlite3
from os import getenv
from xmlrpc.client import boolean
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

class DBManager:
    def __init__(self, env_location=None, app=None):
        if env_location:
            load_dotenv(env_location)
        else:
            load_dotenv(".db_env")
        if getenv("DEV_ENVIRON"):
            self.init_connection = self._init_connection_to_sqlite
            self._generate_tables_to_sqlite()
        else:
            self.db = SQLAlchemy(app)
            self.init_connection = self._init_connection_to_sql_server

    def _init_connection_to_sqlite(self):
        """Init a connection to local database for testing"""
        self.connect = sqlite3.connect("mock_data.db")
        self.cursor = self.connect.cursor()

    def _init_connection_to_sql_server(self):
        """Set self.cursor to point to sqlalchemy session"""
        self.cursor = self.db.session
        self.connect = self.cursor
        #reruns are needless, but this may lessen separate methods

    def _generate_table(self, table: str):
        table_items = getenv(f"{table.upper()}_TABLE_COLUMNS").split(",")
        for i in range(len(table_items)):
            table_items[i] = table_items[i].split(";")
        sql = f"CREATE TABLE IF NOT EXISTS {table} ("
        for column_name, column_type in table_items:
            sql += column_name + " " + column_type + ", "
        sql = sql[:-2] + ")"
        self.cursor.execute(sql)

    def _generate_tables_to_sqlite(self):
        self.init_connection()
        self._generate_table("tips")
        self._generate_table("users")
        self.connect.commit()

    def _generate_mock_data(self):
        self._generate_tables_to_sqlite()
        self.init_connection()
        mock_tips = [("Mock tip 1", "http://mock_tip_1.fi"), ("Mock tip 2", "http://mock_tip_2.fi")]
        self.cursor.executemany("INSERT INTO tips VALUES (?, ?)", mock_tips)
        mock_users = [("1", "Jim_Hacker", "minister", "false"), ("2", "Humphrey_Appleby", "yes_minster", "true")]
        self.cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", mock_users)
        self.connect.commit()

    def get_all_tips(self): # refactor! Select all the tip info asked for in param
        '''hakee tietokannasta kaikki vinkit'''
        self.init_connection()
        return self.cursor.execute("SELECT title, url FROM tips").fetchall()

    def add_tip(self, title: str, url: str) -> bool: #refactor -> take tip info list instead of specifically title and url
        '''yrittää lisätä tietokantaan uuden vinkin. Jos onnistuu = palauttaa True, jos ei = False'''
        if "" in [title, url] or None in [title, url]:
            return False
        try:
            self.init_connection()
            self.cursor.execute("INSERT INTO tips VALUES (?, ?)", (title, url))#further refactor to fit the .env usage here too
            self.connect.commit()
        except Exception as exception:
            print(exception)
            return False
        return True

    def add_user(self, username: str, hashed_password: str, admin: boolean):
        '''Tallentaa uuden käyttäjän tietokantaan.
        Palauttaa dictionaryn, jossa user-id, käyttäjänimi ja admin jos onnistuu.
        Muutoin palauttaa False'''
        if "" in [username, hashed_password] or None in [username, hashed_password]:
            return False
        if getenv("DEV_ENVIRON"):
            self.cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?)", ("1", username, hashed_password, str(admin)))
            self.connect.commit()
            data = {"user_id": 1, "username": username, "admin": admin} #hardcoded 3 -> but basically just because sqlite implementation is just for test
            return data
        else:
            sql = "INSERT INTO users (username, password, admin) VALUES (:username, :password, :admin) RETURNING id, username, admin"
            res=self.cursor.execute(sql, {"username": username, "password": hashed_password, "admin": admin})
            self.connect.commit()
            data={}
            for row in res:
                data["user_id"]=row[0]
                data["username"]=row[1]
                data["admin"]=row[2]
            if data == {}:
                return False
            return data

    def get_user(self, username: str):
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
                data["user_id"]=row[0]
                data["username"]=row[1]
                data["password"]=row[2]
            if data == {}:
                return False
            return data
        except Exception: # Pitäisi löytää mikä tietty exception tässä tulee ja testata vain sitä
            return False