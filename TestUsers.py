from Users import Users
import unittest
from unittest.mock import patch
from models import User
from storage import UserFileManager

class TestUsers(unittest.TestCase):
    def setUp(self):
        # Initialize Users object for testing
        self.users = Users()

    def test_add_user(self):
        # Test adding a user
        with patch('builtins.input', side_effect=["John", "1"]):
            self.users.add_user("John","1")
        self.assertEqual(self.users.users[0]['name'], "John")
        self.assertEqual(self.users.users[0]['user_id'], "1")

    def test_update_user(self):
        # Test updating a user
        self.users.users = [{"name": "John", "user_id": "1"}, {"name": "Alice", "user_id": "2"}]
        self.assertTrue(self.users.update_user("1", new_name="John"))
        self.assertEqual(self.users.users[0]['name'], "John")

    def test_delete_user(self):
        # Test deleting a user
        self.users.users = [{"name": "John", "user_id": "1"}, {"name": "Alice", "user_id": "2"}]
        self.assertTrue(self.users.delete_user("1"))
        self.assertEqual(len(self.users.users), 1)

    def test_search_user(self):
        # Test searching for a user
        self.users.users = [{"name": "John", "user_id": "1"}, {"name": "Alice", "user_id": "2"}]
        with patch('builtins.input', side_effect=["name", "John"]):
            self.assertTrue(self.users.search_user())

if __name__ == "__main__":
    unittest.main()
