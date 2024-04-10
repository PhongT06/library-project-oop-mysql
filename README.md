The Library Management System is a command-line-based application to navigate through a menu to add books, users and authors and to borrow and return library books.

Features 
Add a new book to the library 
Borrow a book from the library 
Return a borrowed book to the library 
Search for a book by title 
View details of all books in the library 
Add a new user to the system 
View details of a user 
Display all users in the system
Add a new author to the system 
View details of an author 
Display all authors in the system

Class Structure 
Book: Represents individual books with attributes such as title, author, availability status. 
User: Represents library users with attributes like name, library ID, and a list of borrowed book titles. 
Author: Represents book authors with attributes like name. Library: Manages the collection of books, users, and authors.

MYSQL

Set up the MySQL database by executing the provided SQL script create_database.sql.
Update the database connection details in the connect_db.py file to match your MySQL server configuration.
Run the main Python script main.py to start the library management system
