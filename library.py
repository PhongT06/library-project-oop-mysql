import mysql.connector
from connect_db import connect_db

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    def add_book(self, book):
        self.books.append(book)
        book.add_book_to_db()

    def lend_book(self, title, user):
        book = self.find_book_by_title(title)
        if book and book.checkout():
            user.borrowed_books.append(book)
            print(f"Book '{title}' has been lent out to {user.name}")
        else:
            print(f"Sorry, '{title}' is not available")
        
    def return_book(self, title, user_name):
        user = self.find_user(user_name)
        if user:
            for book in user.borrowed_books:
                if book.title == title:
                    book.return_book()
                    user.borrowed_books.remove(book)
                    print(f"'{title}' has been returned by {user_name}")
                    return
            print(f"{user_name} does not have '{title}' borrowed")
        else:
            print(f"User '{user_name}' not found")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.get_title() == title:
                return book
        return None

    def search_book(self, title):
        found = False
        for book in self.books:
            if book.title == title:
                availability = "available" if book.is_available else "not available"
                print(f"{book.title} by {book.author} is {availability}")
                found = True
                break
        if not found:
            print(f"Sorry, '{title}' was not found")
        return found

    def add_user(self, user):
        self.users.append(user)
        user.add_user_to_db()

    def find_user(self, name):
        for user in self.users:
            if user.get_name() == name:
                return user
        return None

    def add_author(self, author):
        self.authors.append(author)
        author.add_author_to_db()

    def find_author(self, name):
        for author in self.authors:
            if author.get_name() == name:
                return author
        return None