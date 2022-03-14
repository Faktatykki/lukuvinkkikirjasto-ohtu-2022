import unittest
from unittest.mock import ANY
from os import remove
from data.db import DBManager


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
            titles.append(tip[1])
        self.assertEqual(titles, ["Mock tip 1", "Mock tip 2"])

    def test_get_all_tips_retrieves_urls(self):
        urls = []
        for tip in self.db.get_all_tips():
            urls.append(tip[2])
        self.assertEqual(
            urls, ["http://mock_tip_1.fi", "http://mock_tip_2.fi"])

    def test_get_all_tips_retrieves_tips_for_logged_in_user(self):
        tips = []
        for tip in self.db.get_all_tips(2):
            tips.append(tip)
        self.assertEqual(
            tips, [
                (ANY, "Mock tip 1", "http://mock_tip_1.fi", ANY, ANY, ANY),
                (ANY, "Mock tip 2", "http://mock_tip_2.fi", ANY, ANY, ANY)
            ]
        )

    def test_add_tip_adds_one_tip(self):
        self.db.add_tip("test_tip", "tip.test", "Jim_Hacker")
        self.assertEqual(3, len(self.db.get_all_tips()))

    def test_add_tip_adds_tip_title(self):
        self.db.add_tip("test_tip", "tip.test", "Jim_Hacker")
        self.assertEqual("test_tip", self.db.get_all_tips()[-1][1])

    def test_add_tip_adds_tip_url(self):
        self.db.add_tip("test_tip", "tip.test", "Jim_Hacker")
        self.assertEqual("tip.test", self.db.get_all_tips()[-1][2])

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

    def test_add_tip_can_be_done_without_username(self):
        self.db.add_tip("test_tip", "tip.test")
        self.assertEqual(3, len(self.db.get_all_tips()))

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

    def test_searches_by_title_are_case_insensitive(self):
        tips = self.db.get_tips_by_title("mock")
        self.assertEqual(2, len(tips))

    def test_searches_by_title_with_non_matching_param_returns_empty_list(self):
        tips = self.db.get_tips_by_title("Operating Systems")
        self.assertEqual(0, len(tips))

    def test_mark_tip_as_read_and_unread(self):
        user = self.db.get_user("Jim_Hacker")
        tips = self.db.get_all_tips(user["user_id"])
        # Merkitse vinkki luetuksi
        is_updated = self.db.toggle_read(tips[-1][0], user["user_id"])
        self.assertTrue(is_updated)
        self.assertEqual(self.db.get_all_tips(user["user_id"])[-1][4], '1')
        # Merkitse vinkki lukemattomaksi
        is_updated = self.db.toggle_read(tips[-1][0], user["user_id"])
        self.assertTrue(is_updated)
        self.assertEqual(self.db.get_all_tips(user["user_id"])[-1][4], '0')

    def test_marking_tip_doesnt_change_read_status_of_another_user(self):
        user_jim = self.db.get_user("Jim_Hacker")
        user_hum = self.db.get_user("Humphrey_Appleby")
        tips = self.db.get_all_tips(user_jim["user_id"])
        is_updated = self.db.toggle_read(tips[-1][0], user_jim["user_id"])
        self.assertTrue(is_updated)
        self.assertEqual(self.db.get_all_tips(user_jim["user_id"])[-1][4], '1')
        self.assertEqual(self.db.get_all_tips(user_hum["user_id"])[-1][4], '0')
