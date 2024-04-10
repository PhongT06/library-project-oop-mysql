import _mysql_connector
from connect_db import connect_db
class User:
    def __init__(self, name, library_id, borrowed_books=None):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    def get_name(self):
        return self.name

    def get_library_id(self):
        return self.library_id

    def get_borrowed_books(self):
        return self.borrowed_books

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def add_user_to_db(self):
        conn = connect_db()

        if conn:
            cursor = None
            try:
                cursor = conn.cursor()
                insert_info = (self.name, self.library_id)
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