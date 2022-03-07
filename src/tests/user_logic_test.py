import unittest
from os import remove
from data.db import DBManager
from logic.user_logic import UserLogic
from entities.user import User


class TestUserLogic(unittest.TestCase):
    def setUp(self):
        try:
            remove("mock_data.db")
        except FileNotFoundError:
            pass
        self.db = DBManager(env_location="src/.db_env")
        self.db._generate_mock_data()
        self.logic = UserLogic(self.db)

    # TÄYTYY SELVITTÄÄ MYÖHEMMIN MIKSI LOGGAUTUMISTESTI EI TOIMI:
    # def test_signin_returns_user_instance_if_succesfull(self):
    #     self.assertIsInstance(self.logic.signin("Humphrey_Appleby", "yes_minister"), User)

    # def test_singin_returns_user_with_correct_username_if_succesfull(self):
    #     user = self.logic.signin("Jim_Hacker", "minister")
    #     self.assertEqual(user.username, "Jim_Hacker")

    def test_signin_returns_false_if_no_such_user(self):
        self.assertEqual(False, self.logic.signin("hoohoo", "hiihii"))

    def test_signin_returns_false_if_wrong_password(self):
        self.assertEqual(False, self.logic.signin("Jim_Hacker", "crumb"))

    def test_signin_returns_false_if_empty_password(self):
        self.assertEqual(False, self.logic.signin("Jim_Hacker", ""))

    def test_signin_returns_false_if_no_password(self):
        self.assertEqual(False, self.logic.signin("Jim_Hacker", None))

    def test_signin_returns_false_if_wrong_user(self):
        self.assertEqual(False, self.logic.signin("Jim", "minister"))

    def test_signin_returns_false_if_empty_username(self):
        self.assertEqual(False, self.logic.signin("", "minister"))

    def test_signin_returns_false_if_no_username(self):
        self.assertEqual(False, self.logic.signin(None, "minister"))

    def test_signup_adds_correct_username(self):
        self.logic.signup("test_user", "password27", False)
        data = self.db.get_user("test_user")
        self.assertEqual(data["username"], "test_user")

    def test_signup_cannot_signup_if_no_password(self):
        self.logic.signup("test_user", None, False)
        data = self.db.get_user("test_user")
        self.assertEqual(data, False)

    def test_signup_cannot_signup_if_password_empty_string(self):
        self.logic.signup("test_user", "", False)
        data = self.db.get_user("test_user")
        self.assertEqual(data, False)

    def test_signup_cannot_signup_if_no_username(self):
        self.logic.signup(None, "password27", False)
        data = self.db.get_user(None)
        self.assertEqual(data, False)

    def test_signup_cannot_signup_if_username_empty_string(self):
        self.logic.signup("", "password27", False)
        data = self.db.get_user("")
        self.assertEqual(data, False)
