import unittest
from os import remove
from logic.app_logic import AppLogic
from data.db import DBManager


class TestAppLogic(unittest.TestCase):
    def setUp(self):
        try:
            remove("mock_data.db")
        except FileNotFoundError:
            pass
        self.db = DBManager(env_location="src/.db_env")
        self.db._generate_mock_data()
        self.logic = AppLogic(self.db)

    def test_get_all_tips_returns_titles(self):
        titles = []
        for tip in self.logic.get_all_tips():
            titles.append(tip[0])
        self.assertEqual(titles, ["Mock tip 1", "Mock tip 2"])

    def test_get_all_tips_retrieves_urls(self):
        urls = []
        for tip in self.logic.get_all_tips():
            urls.append(tip[1])
        self.assertEqual(
            urls, ["http://mock_tip_1.fi", "http://mock_tip_2.fi"])

    def test_add_tip_adds_one_tip(self):
        self.logic.add_tip("test_tip", "tip.test", "Jim_Hacker")
        self.assertEqual(3, len(self.db.get_all_tips()))

    def test_add_tip_adds_tip_title(self):
        self.logic.add_tip("test_tip", "tip.test", "Jim_Hacker")
        self.assertEqual("test_tip", self.db.get_all_tips()[-1][0])

    def test_add_tip_adds_tip_url(self):
        self.logic.add_tip("test_tip", "tip.test", "Jim_Hacker")
        self.assertEqual("tip.test", self.db.get_all_tips()[-1][1])

    def test_add_tip_cannot_add_tip_if_no_url(self):
        self.logic.add_tip("test_tip", None, "Jim_Hacker")
        self.assertEqual(2, len(self.db.get_all_tips()))

    def test_add_tip_cannot_add_tip_if_url_is_empty_string(self):
        self.logic.add_tip("test_tip", "", "Jim_Hacker")
        self.assertEqual(2, len(self.db.get_all_tips()))

    def test_add_tip_cannot_add_tip_if_no_title(self):
        self.logic.add_tip(None, "tip.test", "Jim_Hacker")
        self.assertEqual(2, len(self.db.get_all_tips()))

    def test_add_tip_cannot_add_tip_if_title_is_empty_string(self):
        self.logic.add_tip("", "tip.test", "Jim_Hacker")
        self.assertEqual(2, len(self.db.get_all_tips()))

    def test_search_tips_with_empty_param_returns_empty_list(self):
        tips = self.logic.search_tips_by_title("")
        self.assertEqual(0, len(tips))

    def test_search_tips_with_right_param_returns_correct_results(self):
        tips = self.logic.search_tips_by_title("Mock")
        self.assertEqual(2, len(tips))

    def test_add_tip_can_be_done_without_username(self):
        self.logic.add_tip("test_tip", "tip.test")
        self.assertEqual(3, len(self.db.get_all_tips()))