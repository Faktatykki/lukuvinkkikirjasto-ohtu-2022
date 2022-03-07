import sqlite3
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


class DBManager:
    def __init__(self, env_location=None, app=None) -> None:
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

    def _init_connection_to_sqlite(self) -> None:
        """Alusta yhteys lokaaliin SQLiten tietokantaan, käytetään testauksessa"""
        self.connect = sqlite3.connect("mock_data.db")
        self.cursor = self.connect.cursor()

    def _init_connection_to_sql_server(self):
        """Aseta self.cursor osoittamaan SQLAlchemyn sessioon

        - reruns are needless, but this may lessen separate methods
        """
        self.cursor = self.db.session
        self.connect = self.cursor

    def _generate_table(self, table: str) -> None:
        """Luo tietokantataulu SQLiteen
        
        Sarakkeiden nimet ja tyypit haetaan .db_env ympäristömuuttujasta taulun nimen perusteella

        Args:
            table (str): Generoitavan taulun nimi
        """
        table_items = getenv(f"{table.upper()}_TABLE_COLUMNS").split(",")
        for i in range(len(table_items)):
            table_items[i] = table_items[i].split(";")
        sql = f"CREATE TABLE IF NOT EXISTS {table} ("
        for column_name, column_type in table_items:
            sql += column_name + " " + column_type + ", "
        sql = sql[:-2] + ")"
        self.cursor.execute(sql)

    def _generate_tables_to_sqlite(self) -> None:
        """Generoi SQLite tietokantataulut"""
        self.init_connection()
        self._generate_table("tips")
        self._generate_table("users")
        self.connect.commit()

    def _generate_mock_data(self) -> None:
        """Generoi testidataa tietokantaan"""
        self._generate_tables_to_sqlite()
        self.init_connection()
        mock_tips = [
            ("Mock tip 1", "http://mock_tip_1.fi"),
            ("Mock tip 2", "http://mock_tip_2.fi")
        ]
        self.cursor.executemany("INSERT INTO tips (title, url) VALUES (?, ?)", mock_tips)
        mock_users = [
            ("Jim_Hacker", "minister", "false"),
            ("Humphrey_Appleby", "yes_minster", "true")
        ]
        self.cursor.executemany(
            "INSERT INTO users (username, password, admin) VALUES (?, ?, ?)", mock_users)
        self.connect.commit()

    def get_all_tips(self) -> tuple:
        """Hae kaikki vinkit tietokannasta

        TODO:
        - Refactor: Valitse vinkin kentät annettujen parametrien perusteella
        - Refactor #2: Tee vinkeistä oma luokka, joka sisältää kaiken yksittäisen vinkin datan

        Returns:
            tuple: Vinkit tuplena; (title, url)
        """
        self.init_connection()
        tips = self.cursor.execute("SELECT title, url FROM tips").fetchall()
        return tips

    def add_tip(self, title: str, url: str, username: str) -> bool:
        """Lisää uusi vinkki tietokantaan

        Args:
            title (str): Vinkin otsikko
            url (str): Vinkin URL
            username (str): Vinkin lisääjän käyttäjänimi

        Returns:
            bool: True, jos vinkki lisätty onnistuneesti. Muutoin, False
        """
        if "" in [title, url, username] or None in [title, url, username]:
            return False
        try:
            user_id = self.get_user(username)["user_id"]
            print(f'user_id {user_id} lisää uuden vinkin')
            sql = "INSERT INTO tips (title, url, user_id) VALUES (:title, :url, :user_id)"
            self.cursor.execute(sql, {"title": title, "url": url, "user_id": user_id})
            self.connect.commit()
        except Exception as exception:
            print(exception)
            return False
        return True

    def add_user(self, username: str, hashed_password: str, admin: bool) -> tuple:
        """Lisää uusi käyttäjä tietokantaan

        Args:
            username (str): Käyttäjänimi
            hashed_password (str): Salasana, hashattu Werkzeug generate_password_hash:lla
            admin (bool): Käyttäjän admin status, True=admin, False=normaali käyttäjä

        Returns:
            tuple: Palauttaa käyttäjän tiedot tuplena, (user_id, username, admin)
        """        

        if "" in [username, hashed_password] or None in [username, hashed_password]:
            return False
        if getenv("DEV_ENVIRON"):
            self.cursor.execute("INSERT INTO users (username, password, admin) VALUES (?, ?, ?)",
                                (username, hashed_password, admin))
            self.connect.commit()
            data = self.get_user(username)
            # data = {"user_id": 1, "username": username, "admin": admin}
        else:
            sql = """INSERT INTO users (username, password, admin)
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

    def get_user(self, username: str):
        """Hakee tietokannasta käyttäjän käyttäjänimen perusteella

        TODO:
        - Refactor: Käyttäjä -luokan palautus, sisältäen kaiken käyttäjän datan
        - Epäonnistunut haku tuottaa Exceptionin

        Args:
            username (str): Haettavan käyttäjän nimi

        Returns:
            tuple: Käyttäjätiedot tuplena; (user_id, username, password_hash), tai False, jos käyttäjää ei löytynyt
        """
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
