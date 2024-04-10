import mysql.connector
from connect_db import connect_db

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def checkout(self):
        if self.is_available:
            self.is_available = False
            self.update_availability_in_db(False)
            return True
        return False

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def is_available(self):
        return self.is_available

    def return_book(self):
        self.is_available = True
        self.update_availability_in_db(True)

    def update_availability_in_db(self, availability):
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                query = "UPDATE books SET availability = %s WHERE title = %s AND author = %s"
                cursor.execute(query, (availability, self.title, self.author))
                conn.commit()
            except Exception as e:
                print(f"Error updating book availability: {e}")
            finally:
                cursor.close()
                conn.close()

    def add_book_to_db(self):
        conn = connect_db()

        if conn:
            cursor = None
            try:
                cursor = conn.cursor()
                insert_info = (self.title, self.author)
                query = "INSERT INTO books (title, author) VALUES (%s, %s)"
                cursor.execute(query, insert_info)
                conn.commit()
                print(f"Book '{self.title}' by '{self.author}' was successfully added to the database.")
            except Exception as e:
                print(f"Error: {e}")
            finally:
                if cursor:
                    cursor.close()
                conn.close()