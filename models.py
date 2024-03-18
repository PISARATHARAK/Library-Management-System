# Define a class named Book
class Book:
   
    #This class represents a book with its title, author, and ISBN.
    def __init__(self, title, author, isbn): #Constructor
        """
        This method initializes a new Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN number of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        
        #This method defines how a Book object is represented as a string.
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

    def to_dict(self):
        
        #This method converts the Book object into a dictionary.
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn
        }


# Define a class named User
class User:
    
    #This class represents a user with their name and unique ID.
    def __init__(self, name, user_id): #Constructor
        """
        This method initializes a new User object.

        Args:
            name (str): The name of the user.
            user_id (str): The unique ID of the user.
        """
        self.name = name
        self.user_id = user_id

    def __str__(self):
       
        #This method defines how a User object is represented as a string.
        return f"Name: {self.name}, User ID: {self.user_id}"

    def to_dict(self):
       
        #This method converts the User object into a dictionary.
        return {
            "name": self.name,
            "user_id": self.user_id
        }


# Define a class named Checkout
class Checkout:
    
    #This class represents a checkout record with details of the user, book, and checkout information.
    def __init__(self, user_id, isbn, title, author): #Constructor
        """
        This method initializes a new Checkout object.

        Args:
            user_id (str): The ID of the user who checked out the book.
            isbn (str): The ISBN number of the checked-out book.
            title (str): The title of the checked-out book.
            author (str): The author of the checked-out book.
        """
        self.user_id = user_id
        self.isbn = isbn
        self.title = title
        self.author = author

    def __str__(self):
        
        #This method defines how a Checkout object is represented as a string.
        return f"User ID: {self.user_id}, ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}"

    def to_dict(self):
        
        #This method converts the Checkout object into a dictionary.
        return {
            "user_id": self.user_id,
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author
        }
