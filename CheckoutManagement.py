import logging
from models import Book
from models import Checkout
from storage import BookFileManager
from storage import CheckoutManager

class CheckoutManagement:
    def __init__ (self):
        # Initialize checkout and book managers with file names
        self.checkout_manager = CheckoutManager("checkout.json")
        self.book_manager = BookFileManager("books.json")
        
        # Load existing checkout and book data
        self.checkouts = self.checkout_manager.load_data()
        self.books = self.book_manager.load_data()

        # logging.basicConfig(filename='checkout_operations.log', level=logging.INFO,
        #                     format='%(asctime)s - %(levelname)s - %(message)s - File: %(pathname)s')
    
    #Used to check whether is available or not
    def isAvailability(self,isbn):
        for book in self.books:
            if book['isbn']==isbn:
                print("Book is Available")
                logging.info(f"Book with ISBN {isbn} is available")
                return True
        print("Book is Not Available")
        logging.info(f"Book with ISBN {isbn} is not available")
        return False
    
    def checkout_book(self, user_id, isbn):
    # Check if the book with the given ISBN exists and is available
        if self.isAvailability(isbn):
            for book in self.books:
                if book['isbn'] == isbn:
                    # Create a new checkout object and add it to checkouts list
                    new_checkout = Checkout(user_id, isbn, book['title'], book['author'])
                    self.checkouts.append(new_checkout.to_dict())
                    
                    # Remove the checked-out book from the list of books
                    self.books.remove(book)
                    
                    # Save the updated data to the respective files
                    self.checkout_manager.save_data(self.checkouts)
                    self.book_manager.save_data(self.books)
                    
                    print(f"Book with ISBN {isbn} has been checked out by User ID {user_id}.")
                    logging.info(f"Book with ISBN {isbn} has been checked out by User ID {user_id}")
                    return True
            
        # If the book is not available or not found
        print(f"Book with ISBN {isbn} is not available for checkout.")
        logging.info(f"Book with ISBN {isbn} is not available for checkout")
        return False

    
    def checkin_book(self, user_id, isbn):
        # Check if a checkout record exists for the given user and book
        for checkout in self.checkouts:
            if checkout["user_id"] == user_id and checkout["isbn"] == isbn:
                # Remove the checkout record from checkout list
                self.checkouts.remove(checkout)
                
                # Create a new Book object and add it to the list of books
                checkin_book = Book(checkout['title'], checkout['author'], checkout['isbn'])
                self.books.append(checkin_book.to_dict())
                
                # Save the updated data
                self.checkout_manager.save_data(self.checkouts)
                self.book_manager.save_data(self.books)
                
                print(f"Book with ISBN {isbn} has been checked in by User ID {user_id}.")
                logging.info(f"Book with ISBN {isbn} has been checked in by User ID {user_id}")
                return True
        
        print(f"No record found for User ID {user_id} and ISBN {isbn}.")
        logging.info(f"No record found for User ID {user_id} and ISBN {isbn}")
        return False
    
    def list_checkouts(self):
        if(len(self.checkouts)==0):
            print("No checkouts in the list")
            return 
        for c_outs in self.checkouts:
            print(c_outs)

if __name__ == "__main__":
    # Test the checkout management system
    C1 = CheckoutManagement()
    C1.checkout_book(1, "12345")
    C1.checkout_book(1, "67890")
    C1.checkout_book(2, "3567")
    C1.checkout_book(3, "90876")
    C1.list_checkouts()

    C1.checkin_book(1, "12345")
    C1.checkin_book(3, "90876")
    C1.list_checkouts()
