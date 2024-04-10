import mysql.connector
from connect_db import connect_db

class Author:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def add_author_to_db(self):
        conn = connect_db()
        if conn:
            cursor = None
            try:
                cursor = conn.cursor()
                query = "INSERT INTO authors (name) VALUES (%s)"
                cursor.execute(query, (self.name,))
                conn.commit()
                print("Author added successfully!")
            except mysql.connector.Error as error:
                print(f"Error adding author to database: {error}")
            finally:
                if cursor:
                    cursor.close()
                conn.close()
        else:
            print("MySQL Connection not available.")
