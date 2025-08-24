#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from datetime import date, timedelta

# Function to write data to a file
def write_data(filename, data):
    with open(filename, 'w') as file:
        file.write('\n'.join(', '.join(line) for line in data) + '\n')

# Function to read data from a file
def read_data(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        return [line.strip().split(', ') for line in file]

# Function to add a new book
def add_book():
    books = read_data('books.txt')
    print()
    book_id = input("Enter Book ID: ").strip()
    if any(book[0] == book_id for book in books):
        print("Book Already Registered.")
        return
    print()
    print('Enter New Book Info:')
    title = input("Enter Book Title: ").strip()
    author = input("Enter Book Author: ").strip()
    books.append([book_id, title, author, 'Available'])
    write_data('books.txt', books)
    print("Book added successfully.")

# Function to register a new member
def register_member():
    members = read_data('members.txt')
    print()
    member_id = input("Enter Member ID: ").strip()
    if any(member[0] == member_id for member in members):
        print("Member already exists.")
        return
    print()
    print('Enter New Member Info:')
    name = input("Enter Member Name: ").strip()
    contact = input("Enter Contact Details: ").strip()
    members.append([member_id, name, contact, 'Active'])
    write_data('members.txt', members)
    print("Member registered successfully.")

# Function to lend a book
def lend_book():
    books = read_data("books.txt")
    lending = read_data("lend.txt")
    book_id = input("Please enter book ID: ").strip()

    for book in books:
        if book[0] == book_id:
            if book[-1] == 'Available':
                book[-1] = 'Lent'
                today = date.today()
                return_date = today + timedelta(days=14)
                member_id = input("Please enter your Member ID: ").strip()

                lending.append([book_id, member_id, str(today), str(return_date), ""])

                write_data('books.txt', books)
                write_data('lend.txt', lending)
                print("Book has been lent out successfully!")
                return
            elif book[-1] == 'Not Available' or book[-1] == 'Lent':
                print("Book is not available for lending.")
                return
    
    print("Book not found.")

# Function to return a book
def book_return():
    books = read_data("books.txt")
    lending = read_data("lend.txt")
    book_id = input("Please enter book ID: ").strip()

            
    for book in books:
        if book[0] == book_id and book[-1] == 'Lent': 
            book[-1] = 'Available'
            write_data('books.txt', books)
            write_data('lend.txt', lending)
            print("Book has been returned, thank you")
            return
            
        elif book[0] == book_id and book[-1] == 'Not Available':
            print("Book is currently not available")
            return
    
    print("Book has not been lent / Book has already been returned.")

# Function to display books
def display_books():
    books = read_data('books.txt')
    print("\nBook Inventory:")
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Status: {book[3]}")
    print()

# Function to display members
def display_members():
    members = read_data('members.txt')
    print("\nMember Information:")
    for member in members:
        print(f"ID: {member[0]}, Name: {member[1]}, Contact: {member[2]}, Status: {member[3]}")
    print()

# Main menu function
def menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. Register a new member")
        print("3. Lend a book")
        print("4. Return a book")
        print("5. Display Book Inventory")
        print("6. Display Member Information")
        print("7. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_book()
        elif choice == '2':
            register_member()
        elif choice == '3':
            lend_book()
        elif choice == '4':
            book_return()
        elif choice == '5':
            display_books()
        elif choice == '6':
            display_members()
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


# Initial data for Books (books.txt)
data_books = [
    ["1", "Red,White and Royal Blue", "Casey McQuiston", "Available"],
    ["2", "It Ends With Us", "Colleen Hoover", "Not Available"],
    ["3", "The Song of Achilles", "Madeline Miller", "Available"],
    ["4", "The Little Prince", "Antoine de Saint-Exupéry", "Available"]
]

# Initial data for Members (members.txt)
data_members = [
    ["1", "Mary Ann", "maryann@gmail.com", "Active"],
    ["2", "John Doe", "johndoe@gmail.com", "Active"],
    ["3", "John Appleseed", "appleseed@gmail.com", "Active"],
    ["4", "Jenny Click", "jenny@gmail.com", "Active"]
]

# Write initial data to books.txt
write_data('books.txt', data_books)

# Write initial data to members.txt
write_data('members.txt', data_members)

# Create empty lend.txt if it doesn't exist
if not os.path.exists("lend.txt"):
    open("lend.txt", 'w').close()

# Main function call to start the program
menu()