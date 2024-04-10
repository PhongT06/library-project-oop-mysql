from book import Book
from user import User
from author import Author
from library import Library
from connect_db import connect_db
import _mysql_connector

############## Having an issue trying to connecto to MYSQL when borrowing a book for some reason

# Define functions for each menu option (Book Operations, User Operations, Author Operations, Quit)

def main():
    print("Welcome to the Library Management System!")

    library = Library()

    while True:
        print("\nMain Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        choice = input("Please enter your choice between (1-4): ")

        if choice == '1':
            book_operations(library)
        elif choice == '2':
            user_operations(library)
        elif choice == '3':
            author_operations(library)
        elif choice == '4':
            print("Thank you for using the Library Management System!")
            print("Have a nice day!")
            break
        else:
            print("Invalid choice! Please choose a valid number between (1-4).")

def book_operations(library):
    print("\nBook Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
    choice = input("Please enter your choice between (1-5): ")

    if choice == '1':
        add_new_book(library)
    elif choice == '2':
        borrow_book(library)
    elif choice == '3':
        return_book(library)
    elif choice == '4':
        search_book(library)
    elif choice == '5':
        display_all_books(library)
    else:
        print("Invalid choice! Please enter a valid number between (1-5).")

def add_new_book(library):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    book = Book(title, author)
    library.add_book(book)
    add_book(book.get_title(), book.get_author())
    print(f"Added book: {title} by {author}")

def add_book(title, author):
    conn = connect_db()

    if conn:
        cursor = None
        try:
            cursor = conn.cursor()
            insert_info = (title, author)
            query = "INSERT INTO books (title, author) VALUES (%s, %s)"
            cursor.execute(query, insert_info)
            conn.commit()
            print("Book added successfully!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            conn.close()

def borrow_book(library):
    try:
        title = input("Enter the title of the book to borrow: ")
        user_name = input("Enter your name: ")
        user = library.find_user(user_name)
        if user:
            print(f"User {user_name} found: {title}")
            library.lend_book(title, user)

            conn = connect_db()
            if conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id FROM books WHERE title = %s", (title,))
                book_id = cursor.fetchone()

                if book_id:
                    query = "INSERT INTO borrowed_books (book_id, user_id) VALUES (%s, %s)"
                    cursor.execute(query, (book_id[0], user.id))
                    conn.commit()
                    print("Book borrowed successfully!")
                else:
                    print("Book not found.")
                
                cursor.close()
                conn.close()
        else:
            print("User not found!")
    except Exception as e:
        print(f"Error: {e}")

def return_book(library):
    try:
        title = input("Enter the title of the book that you want to return: ")
        user_name = input("Enter your name: ")
        user = library.find_user(user_name)
        if user:
            library.return_book(title, user_name)
            conn = connect_db()
            if conn:
                cursor = conn.cursor()
                query = "DELETE FROM borrowed_books WHERE book_name = %s AND user_name = %s"
                cursor.execute(query, (title, user_name))
                conn.commit()
                cursor.close()
                conn.close()
        else:
            print("User not found!")
    except Exception as e:
        print(f"Error: {e}")

def search_book(library):
    title = input("Please enter the title of the book you wish to search for: ")
    if library.search_book(title):
        print("Book found successfully!")
    else:
        print("Book not found.")

def display_all_books(library):
    print("All books: ")
    for book in library.books:
        print(f"Title: {book.title}, Author: {book.author}")
    if not library.books:
        print("No books available in the library.")

def user_operations(library):
    print("\nUser Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    choice = input("Please enter a choice between (1-3): ")

    if choice == '1':
        add_new_user(library)
    elif choice == '2':
        view_user_details(library)
    elif choice == '3':
        display_all_users(library)
    else:
        print("Invalid choice! Please choose a number between (1-3).")

def add_new_user(library):
    name = input("Enter user's name: ")
    library_id = input("Enter library ID: ")
    user = User(name, library_id)
    library.add_user(user)
    add_user_to_db(name, library_id)  

def add_user_to_db(name, library_id):
    conn = connect_db()

    if conn:
        cursor = None  
        try:
            cursor = conn.cursor()
            insert_info = (name, library_id)
            query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
            cursor.execute(query, insert_info)
            conn.commit()
            print("User added successfully!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()  
            conn.close()

def view_user_details(library):
    name = input("Enter user's name: ")
    user = library.find_user(name)
    if user:
        print(f"User details:")
        print(f"Name: {user.name}")
        print(f"Library ID: {user.get_library_id()}")
        print(f"Borrowed books: {', '.join(book.title for book in user.borrowed_books)}")
    else:
        print("User not found!")

def display_all_users(library):
    print("All users: ")
    try:
        for user in library.users:
            print(f"Name: {user.name}, Library ID: {user.get_library_id()}, Borrowed books: {', '.join(book.title for book in user.borrowed_books)}")
    except Exception as e:
        print(f"Error: {e}")

def author_operations(library):
    print("\nAuthor Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        add_new_author(library)
    elif choice == '2':
        view_author_details(library)
    elif choice == '3':
        display_all_authors(library)
    else:
        print("Invalid choice! Please choose a number between (1-3).")

def add_new_author(library):
    name = input("Enter author's name: ")
    author = Author(name)
    library.add_author(author)
    add_author_to_db(name)  

def add_author_to_db(name):
    conn = connect_db()
    if conn:
        cursor = None
        try:
            cursor = conn.cursor()
            query = "INSERT INTO authors (name) VALUES (%s)"
            cursor.execute(query, (name,))
            conn.commit()
            print(f"Author '{name}' added successfully")
        except mysql.connector.Error as err:
            print(f"Error adding author to database: {err}")
        finally:
            if cursor:
                cursor.close()
            conn.close()
    else:
        print("MySQL Connection not available.")

def view_author_details(library):
    name = input("Enter author's name: ")
    author = library.find_author(name)
    if author:
        print(f"Author details:")
        print(f"Name: {author.name}")
    else:
        print("Author not found!")

def display_all_authors(library):
    print("All authors:")
    try:
        for author in library.authors:
            print(f"Name: {author.name}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()





