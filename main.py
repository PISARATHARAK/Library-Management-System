# This is a deliberately poorly implemented main script for a Library Management System.
import logging
import os
from Books import Books
from Users import Users
from CheckoutManagement import CheckoutManagement



# Configure logging
logging.basicConfig(filename='library_management.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(filename)s - %(message)s')

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Search Book")
    print("6. Add User")
    print("7. List Users")
    print("8. Update User")
    print("9. Delete User")
    print("10. Search User")
    print("11. Checkout Book")
    print("12. Checkin Book")
    print("13.List all Checkouts")
    print("14. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            Books().add_book(title, author, isbn)
            print("Book added.")
        elif choice == '2':
            Books().list_books()
        elif choice== '3':
            
            isbn = input("Enter ISBN of the book to update: ")
            new_title = input("Enter new title (or press Enter to keep existing): ")
            new_author = input("Enter new author (or press Enter to keep existing): ")
            
            Books().update_book(isbn, new_title=new_title.strip() or None, 
                                new_author=new_author.strip() or None)
        elif choice == '4':
            isbn=input("Enter the isbn number to delete that book:")
            Books().delete_book(isbn)
        elif choice == '5':
            Books().search_book()
        elif choice == '6':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            Users().add_user(name, user_id)
            print("User added.")

        elif choice=='7':
            Users().list_users()
        
        elif choice=='8':
            user_id = input("Enter the User id of the User to update: ")
            new_name = input("Enter new name (or press Enter to keep existing): ")
            
            Users().update_user(user_id,  new_name=new_name.strip() or None)

        elif choice=='9':
            user_id=input("Enter the user id to delete that user:")
            Users().delete_user(user_id)
        
        elif choice=='10':
            Users().search_user()

        elif choice == '11':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            CheckoutManagement().checkout_book(user_id, isbn)
            
        
        elif choice== '12':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            CheckoutManagement().checkin_book(user_id,isbn)
            
        elif choice=='13':
            CheckoutManagement().list_checkouts()
        elif choice == '14':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
