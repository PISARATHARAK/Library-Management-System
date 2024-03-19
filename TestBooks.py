import unittest
from unittest.mock import patch
from Books import Books

class TestBooks(unittest.TestCase):
    def setUp(self):
        self.books = Books()

    @patch('builtins.input', side_effect=['DBMS', 'Tharak', '12345'])
    def test_add_book(self, mock_input):
        self.books.add_book("DBMS", "Tharak", "12345")
        # self.assertEqual(len(self.books.books), 1)

    @patch('builtins.input', return_value='67890')
    def test_delete_book(self, mock_input):
        self.books.add_book("C++", "Sandeep", "67890")
        self.books.delete_book("67890")
        # self.assertEqual(len(self.books.books), 0)

    @patch('builtins.input', side_effect=['title', '12345'])
    def test_search_book(self, mock_input):
        # self.books.add_book("DBMS", "Tharak", "12345")
        self.assertFalse(self.books.search_book())

    @patch('builtins.input', side_effect=['C++', 'Sandeep', '67890'])
    def test_update_book(self, mock_input):
        self.books.add_book("C++", "Sandeep", "67890")
        self.books.update_book("67890", new_title="Updated C++", new_author="Updated Sandeep")
        updated_book = next((book for book in self.books.books if book['isbn'] == "67890"), None)
        self.assertIsNotNone(updated_book)
        self.assertEqual(updated_book['title'], "Updated C++")
        self.assertEqual(updated_book['author'], "Updated Sandeep")

    @patch('builtins.input', side_effect=['DBMS', 'Tharak', '12345'])
    def test_list_books(self, mock_input):
        self.books.add_book("DBMS", "Tharak", "12345")
        with patch('builtins.print') as mocked_print:
            self.books.list_books()
            mocked_print.assert_called_with({'title': 'DBMS', 'author': 'Tharak', 'isbn': '12345'})

if __name__ == '__main__':
    unittest.main()
