import unittest
from unittest.mock import patch, MagicMock
from CheckoutManagement import CheckoutManagement

class TestCheckoutManagement(unittest.TestCase):
    def setUp(self):
        self.checkout_manager = CheckoutManagement()

    @patch('builtins.print')
    def test_checkout_book_available(self, mock_print):
        with patch.object(self.checkout_manager, 'isAvailability', return_value=True):
            self.checkout_manager.books = [{'isbn': '12345', 'title': 'Book1', 'author': 'Author1'}]
            self.checkout_manager.checkout_manager.save_data = MagicMock()
            self.checkout_manager.book_manager.save_data = MagicMock()

            self.assertTrue(self.checkout_manager.checkout_book(1, '12345'))

            # self.assertEqual(len(self.checkout_manager.checkouts), 1)
            # self.assertEqual(len(self.checkout_manager.books), 0)

            self.checkout_manager.checkout_manager.save_data.assert_called_once()
            self.checkout_manager.book_manager.save_data.assert_called_once()

            mock_print.assert_called_with("Book with ISBN 12345 has been checked out by User ID 1.")

    @patch('builtins.print')
    def test_checkout_book_unavailable(self, mock_print):
        with patch.object(self.checkout_manager, 'isAvailability', return_value=False):
            self.assertFalse(self.checkout_manager.checkout_book(1, '12345'))
            mock_print.assert_called_with("Book with ISBN 12345 is not available for checkout.")

    @patch('builtins.print')
    def test_checkin_book(self, mock_print):
        self.checkout_manager.checkouts = [{'user_id': 1, 'isbn': '12345', 'title': 'Book1', 'author': 'Author1'}]
        self.checkout_manager.books = []
        self.checkout_manager.checkout_manager.save_data = MagicMock()
        self.checkout_manager.book_manager.save_data = MagicMock()

        self.assertTrue(self.checkout_manager.checkin_book(1, '12345'))

        self.assertEqual(len(self.checkout_manager.checkouts), 0)
        self.assertEqual(len(self.checkout_manager.books), 1)

        self.checkout_manager.checkout_manager.save_data.assert_called_once()
        self.checkout_manager.book_manager.save_data.assert_called_once()

        mock_print.assert_called_with("Book with ISBN 12345 has been checked in by User ID 1.")

    @patch('builtins.print')
    def test_checkin_book_not_found(self, mock_print):
        self.checkout_manager.checkouts = [{'user_id': 1, 'isbn': '12345', 'title': 'Book1', 'author': 'Author1'}]
        self.checkout_manager.books = []
        self.assertFalse(self.checkout_manager.checkin_book(2, '12345'))
        mock_print.assert_called_with("No record found for User ID 2 and ISBN 12345.")

    def test_list_checkouts(self):
        self.checkout_manager.checkouts = [{'user_id': 1, 'isbn': '12345', 'title': 'Book1', 'author': 'Author1'}]
        with patch('builtins.print') as mock_print:
            self.checkout_manager.list_checkouts()
            mock_print.assert_called_with({'user_id': 1, 'isbn': '12345', 'title': 'Book1', 'author': 'Author1'})

if __name__ == '__main__':
    unittest.main()
