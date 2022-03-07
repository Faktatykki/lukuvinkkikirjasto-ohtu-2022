import unittest
import pytest
from os import remove
from data.db import DBManager
from dotenv import load_dotenv



class TestDBManager(unittest.TestCase):
    def setUp(self):
        try:
            remove("mock_data.db")
        except FileNotFoundError:
            pass
        self.db = DBManager(env_location="src/.db_env")
        self.db._generate_mock_data()

    def test_get_all_tips_retrieves_titles(self):
        titles = []
        for tip in self.db.get_all_tips():
            titles.append(tip[0])
        self.assertEqual(titles, ["Mock tip 1", "Mock tip 2"])

    def test_get_all_tips_retrieves_urls(self):
        urls = []
        for tip in self.db.get_all_tips():
            urls.append(tip[1])
        self.assertEqual(
            urls, ["http://mock_tip_1.fi", "http://mock_tip_2.fi"])

    def test_add_tip_adds_one_tip(self):
        self.db.add_tip("test_tip", "tip.test", "Jim_Hacker")
        self.assertEqual(3, len(self.db.get_all_tips()))

    def test_add_tip_adds_tip_title(self):
        self.db.add_tip("test_tip", "tip.test", "Jim_Hacker")
        self.assertEqual("test_tip", self.db.get_all_tips()[-1][0])

    def test_add_tip_adds_tip_url(self):
        self.db.add_tip("test_tip", "tip.test", "Jim_Hacker")
        self.assertEqual("tip.test", self.db.get_all_tips()[-1][1])

    def test_add_tip_cannot_add_tip_if_no_url(self):
        self.db.add_tip("test_tip", None, "Jim_Hacker")
        self.assertEqual(2, len(self.db.get_all_tips()))

    def test_add_tip_cannot_add_tip_if_url_is_empty_string(self):
        self.db.add_tip("test_tip", "", "Jim_Hacker")
        self.assertEqual(2, len(self.db.get_all_tips()))

    def test_add_tip_cannot_add_tip_if_no_title(self):
        self.db.add_tip(None, "tip.test", "Jim_Hacker")
        self.assertEqual(2, len(self.db.get_all_tips()))

    def test_add_tip_cannot_add_tip_if_title_is_empty_string(self):
        self.db.add_tip("", "tip.test", "Jim_Hacker")
        self.assertEqual(2, len(self.db.get_all_tips()))

    def test_add_tip_cannot_add_tip_if_user_id_not_in_users(self):
        self.db.add_tip("test_tip", "tip.test", "Non_Existing_Test_User")
        self.assertEqual(2, len(self.db.get_all_tips()))

    def test_add_tip_cannot_add_tip_if_user_id_empty(self):
        with pytest.raises(TypeError) as Error:
            self.db.add_tip("test_tip", "tip.test")
        self.assertEqual(2, len(self.db.get_all_tips()))

    def test_get_user_returns_false_if_no_such_user(self):
        data = self.db.get_user("Granberryuser")
        self.assertEqual(False, data)

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
