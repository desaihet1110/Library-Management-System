import os
# Atalay Aygul
# Library Management System
# Summary PDF:
# https://drive.google.com/file/d/1ZEIfxoExRvFW1tGTJeuucS0KiQecKK6j/view?usp=sharing
# Short summary:
# I tried to write contracts for each function and use only English.
# I also tried to catch possible errors.

class Library:
    def __init__(self, filename='books.txt'):
        """
        Starts the Library instance.

        Parameters:
        filename (str): The name of the file to store books. Defaults to 'books.txt'.
        """
        self.filename = filename

    def list_books(self):
        """
        Shows all the books in the library.
        """
        try:
            with open(self.filename, 'r') as file:
                books = file.readlines()
                if not books:
                    print("There are no books to show, please save a book.")
                    return
                for book in books:
                    name, author, release_date, pages = book.strip().split(', ')
                    print(f"Book Title: {name}, Author: {author}, Release Year: {release_date}, Pages: {pages}")
        except FileNotFoundError:
            print("File doesn't exist. Please save a book first.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def add_book(self):
        """
        Includes a new book to the library.
        """
        try:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            while True:
                year = input("Enter the year of first release: ")
                if year.isdigit() and int(year) > 0:
                    break
                else:
                    print("Please type a positive whole number for the release year.")
            while True:
                pages = input("Enter number of pages: ")
                if pages.isdigit() and int(pages) > 0:
                    break
                else:
                    print("Please type a positive whole number for the number of pages.")
            with open(self.filename, 'a') as file:
                file.write(f"{title}, {author}, {year}, {pages}\n")
            print("Book successfully added.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def remove_book(self):
        """
        Removes a book from the library.
        """
        try:
            title_to_remove = input("Enter the title of the book to remove: ")
            with open(self.filename, 'r') as file:
                books = file.readlines()

            # Check if any book is removed
            removed = False
            updated_books = []
            for book in books:
                if not book.startswith(title_to_remove):
                    updated_books.append(book)
                else:
                    removed = True

            if removed:
                with open(self.filename, 'w') as file:
                    file.writelines(updated_books)
                print("Book removed successfully.")
            else:
                print(f"The book '{title_to_remove}' is not in the library.")
        except FileNotFoundError:
            print(f"The file named {self.filename} doesn't exist.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


# Create the Library instance
lib = Library()

# Menu system
while True:
    print("*** MENU ***")
    print("1) Show Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        break
    else:
        print("Invalid option. Please try again.")
