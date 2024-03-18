import logging
from models import Book
from storage import BookFileManager

class Books:
    def __init__(self): #Constructor
        self.book_manager = BookFileManager("books.json")
        self.books = self.book_manager.load_data()

        # # Configure logging
        # logging.basicConfig(filename='book_operations.log', level=logging.INFO,
        #                     format='%(asctime)s - %(levelname)s - %(message)s - File: %(pathname)s')
    #function to add books
    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book.to_dict())  # Convert Book object to dictionary for saving in json file
        self.book_manager.save_data(self.books)  # Save updated data to json file

        # Log the operation
        logging.info(f"Added book: Title='{title}', Author='{author}', ISBN='{isbn}'")

    #function to list all the books
    def list_books(self):
        for book in self.books:
            print(book)

    #function to update the book in the json file
    def update_book(self, isbn, new_title=None, new_author=None):
        for book in self.books:
            if book['isbn'] == isbn:  # Use book.isbn instead of book[isbn]
                if new_title is not None:
                    book['title'] = new_title
                if new_author is not None:
                    book['author'] = new_author
                
                print(f'Book with ISBN Number {isbn} is Updated')
                self.book_manager.save_data(self.books)
                # Log the operation
                logging.info(f"Updated book with ISBN '{isbn}': New title='{new_title}', New author='{new_author}'")

                return True
        print(f'Book with ISBN Number {isbn} not found')
        return False


    #function to delete the book from json file
    def delete_book(self, isbn):
        for book in self.books:
            if book['isbn'] == isbn:  # Use book.isbn instead of book['isbn']
                self.books.remove(book)
                print(f"Book with ISBN Number {isbn} is deleted")
                self.book_manager.save_data(self.books)  # Save updated data
                # Log the operation
                logging.info(f"Deleted book with ISBN '{isbn}'")
                return True
        print(f'Book with ISBN Number {isbn} not found')
        return False

    #function to Search for the book in the json file
    def search_book(self):
        while True:
            attribute = input("Enter the Attribute you want to search for:").lower()
            valid = ["title", "isbn", "author"]
            if attribute not in valid:
                continue
            value = input(f"Enter the {attribute} you are searching for:")
            for book in self.books:
                if book[attribute] == value:  # Use getattr to access attribute dynamically
                    print(f"Book with {attribute} {value} is found")
                    return True
            print(f"No Book with {attribute} {value} is found")
            return False
    

if __name__ == "__main__":
    B1 = Books()

    B1.add_book("DBMS", "Tharak", "12345")
    B1.add_book("C++", "Sandeep", "67890")
    B1.add_book("C", "Sai Kumar", "3567")
    B1.add_book("ABCD", "DEFG", "90876")
    B1.add_book("TOC", "Dilip", "2130200")
    B1.list_books()

    B1.update_book("67890", new_author="Nani")
    B1.list_books()

    B1.delete_book("90876")
    B1.list_books()

    B1.search_book()
