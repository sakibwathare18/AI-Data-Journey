class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # New books are available by default

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Title: {self.title} | Author: {self.author} | Status: {status}")

    def borrow(self):
        if self.available:
            self.available = False
            print(f"Success: You have borrowed '{self.title}'.")
            return True
        else:
            print(f"Error: '{self.title}' is already borrowed.")
            return False

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"Success: Thank you for returning '{self.title}'.")
            return True
        else:
            print(f"Error: '{self.title}' was not checked out.")
            return False


class Library:
    def __init__(self):
        # This is a LIST OF OBJECTS (instances of the Book class)
        self.books = []

    def add_book(self, book_object):
        # We append the actual object, not a dictionary
        self.books.append(book_object)
        print(f"Book '{book_object.title}' added to the library system.")

    def display_books(self):
        if not self.books:
            print("The library is currently empty.")
            return
        
        print("\n--- Current Books in Library ---")
        for book in self.books:
            # We call the display method belonging to each individual Book object
            book.display()

    def search_book(self, title):
        for book in self.books:
            # Accessing the property of the object directly using dot notation
            if book.title.lower() == title.lower():
                print("\nBook Found:")
                book.display()
                return book
        print(f"Book with title '{title}' not found.")
        return None

    def borrow_book(self, title):
        book = self.search_book(title)
        if book:
            # Call the borrow method inside that specific book object
            book.borrow()

    def return_book(self, title):
        book = self.search_book(title)
        if book:
            # Call the return method inside that specific book object
            book.return_book()


# --- Interactive Menu Loop ---
def main():
    library = Library()

    # Pre-populating with a few Book objects as requested
    library.add_book(Book("The Hobbit", "J.R.R. Tolkien"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("Python Crash Course", "Eric Matthes"))

    while True:
        print("\n===== LIBRARY =====")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            if title and author:
                new_book = Book(title, author) # Creating a new object instance
                library.add_book(new_book)     # Passing the object to library
            else:
                print("Title and Author cannot be empty.")

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            title = input("Enter title to search: ").strip()
            library.search_book(title)

        elif choice == "4":
            title = input("Enter title to borrow: ").strip()
            library.borrow_book(title)

        elif choice == "5":
            title = input("Enter title to return: ").strip()
            library.return_book(title)

        elif choice == "6":
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1 and 6.")

# Run the program
if __name__ == "__main__":
    main()
