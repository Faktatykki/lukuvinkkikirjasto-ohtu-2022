import unittest
from entities import user


class TestUser(unittest.TestCase):
    def setUp(self):
        self.test_user = user.User(1, "test_user")
        self.admin_user = user.User(0, "admin_user", True)

    def test_konstruktori_luo_käyttäjän_oikein(self):
        self.assertEqual(self.test_user.user_id, 1)
        self.assertEqual(self.test_user.username, "test_user")
        self.assertEqual(self.test_user.admin, False)

        self.assertEqual(self.admin_user.user_id, 0)
        self.assertEqual(self.admin_user.username, "admin_user")
        self.assertEqual(self.admin_user.admin, True)

        self.assertNotEqual(self.test_user.user_id, 2)
