from pickle import NONE
import unittest
from data.db import DBManager
from dotenv import load_dotenv
from os import getenv

class TestDBManager(unittest.TestCase):
    def setUp(self):
        self.db = DBManager(env_location="src/.env")
        self._generate_mock_data()
        load_dotenv("src/.db_env") # ei ehkä tarpeen

    def _generate_mock_data(self): #migrate this to db_test.py instead
        self.db._generate_tables_to_sqlite()
        self.db.init_connection()
        mock_tips = [("Mock tip 1", "http://mock_tip_1.fi"), ("Mock tip 2", "http://mock_tip_2.fi")]
        self.db.cursor.executemany("INSERT INTO tips VALUES (?, ?)", mock_tips)
        mock_users = [("1", "Jim_Hacker", "minister", "false"), ("2", "Humphrey_Appleby", "yes_minster", "true")]
        self.db.cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", mock_users)
        self.db.connect.commit()

    def test_get_all_tips_retrieves_title_column_title(self):
        self.assertEqual(self.db.get_all_tips()[0][0], "title") 

    def test_get_all_tips_retrieves_url_column_title(self):
        self.assertEqual(self.db.get_all_tips()[0][1], "url") 

    def test_get_all_tips_retrieves_titles(self):
        self._generate_mock_data()
        titles = []
        for tip in self.db.get_all_tips()[1:]:
            titles.append(tip[0])
        self.assertEqual(titles, ["Mock tip 1", "Mock tip 2"])

    def test_get_all_tips_retrieves_urls(self):
        self._generate_mock_data()
        urls = []
        for tip in self.db.get_all_tips()[1:]:
            urls.append(tip[1])
        self.assertEqual(urls, ["http://mock_tip_1.fi", "http://mock_tip_2.fi"])

    def test_add_tip_adds_one_tip(self):
        self.db.add_tip("test_tip", "tip.test")
        self.assertEqual(4, len(self.db.get_all_tips()))

    def test_add_tip_adds_tip_title(self):
        self.db.add_tip("test_tip", "tip.test")
        self.assertEqual("test_tip", self.db.get_all_tips()[-1][0])

    def test_add_tip_adds_tip_url(self):
        self.db.add_tip("test_tip", "tip.test")
        self.assertEqual("tip.test", self.db.get_all_tips()[-1][1])
        
    def test_add_tip_cannot_add_tip_if_no_url(self):
        self.db.add_tip("test_tip", None)
        self.assertEqual(3, len(self.db.get_all_tips()))

    def test_add_tip_cannot_add_tip_if_url_is_empty_string(self):
        self.db.add_tip("test_tip", "")
        self.assertEqual(3, len(self.db.get_all_tips()))

    def test_add_tip_cannot_add_tip_if_no_title(self):
        self.db.add_tip(None, "tip.test")
        self.assertEqual(3, len(self.db.get_all_tips()))

    def test_add_tip_cannot_add_tip_if_title_is_empty_string(self):
        self.db.add_tip("", "tip.test")
        self.assertEqual(3, len(self.db.get_all_tips()))

    def test_get_user_returns_empty_dict_if_no_such_user(self):
        data = self.db.get_user("Granberryuser")
        self.assertEqual({}, data)

    def test_get_user_returns_user_if_user_exists(self):
        data = self.db.get_user("Jim_Hacker")
        self.assertNotEqual(False, data)

    def test_add_user_adds_correct_username(self):
        self.db.add_user("test_user", "password27", False)
        data = self.db.get_user("test_user")
        self.assertEqual(data["username"], "test_user")

    def test_add_user_cannot_add_user_if_no_password(self):
        self.db.add_user("test_user", None, False)
        data = self.db.get_user("test_user")
        self.assertEqual(data, False)

    def test_add_user_cannot_add_user_if_password_empty_string(self):
        self.db.add_user("test_user", "", False)
        data = self.db.get_user("test_user")
        self.assertEqual(data, False)

    def test_add_user_cannot_add_user_if_no_username(self):
        self.db.add_user(None, "password27", False)
        data = self.db.get_user(None)
        self.assertEqual(data, False)

    def test_add_user_cannot_add_user_if_username_empty_string(self):
        self.db.add_user("", "password27", False)
        data = self.db.get_user("")
        self.assertEqual(data, False)
