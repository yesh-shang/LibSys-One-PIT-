import json
from models import Book, Borrower


class LibSys:
    def __init__(self):
        self.books = {}
        self.borrowers = {}
        self.borrowed_books = {}
        self.load_data()

    def load_data(self):
        try:
            with open("books.json", "r") as f:
                books_data = json.load(f)
                for title, data in books_data.items():
                    self.books[title] = Book.from_dict(data)
        except FileNotFoundError:
            pass

        try:
            with open("borrowers.json", "r") as f:
                borrowers_data = json.load(f)
                for email, data in borrowers_data.items():
                    self.borrowers[email] = Borrower.from_dict(data)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open("books.json", "w") as f:
            json.dump({title: book.to_dict() for title, book in self.books.items()}, f, indent=4)

        with open("borrowers.json", "w") as f:
            json.dump({email: borrower.to_dict() for email, borrower in self.borrowers.items()}, f, indent=4)

    def add_book(self):
        print("\n========== Add New Book ==========")
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        self.books[title] = Book(title, author)
        self.save_data()
        print("✅ Book added successfully!")
        print("===================================")

    def search_book(self):
        print("\n========== Search Book ==========")
        title = input("Enter book title: ")
        if title in self.books:
            book = self.books[title]
            print(f"\n📘 Title : {book.title}")
            print(f"✍️  Author: {book.author}")
            print(f"📌 Status: {book.status}")
        else:
            print("❌ Book not found.")
        print("===================================")

    def register_borrower(self):
        print("\n========== Register Borrower ==========")
        name = input("Enter borrower name: ")
        email = input("Enter borrower email: ")
        self.borrowers[email] = Borrower(name, email)
        self.save_data()
        print("✅ Borrower registered successfully!")
        print("========================================")

    def borrow_book(self):
        print("\n========== Borrow Book ==========")
        email = input("Enter borrower email: ")
        if email in self.borrowers:
            title = input("Enter book title: ")
            if title in self.books and self.books[title].status == "Available":
                self.books[title].status = "Borrowed"
                self.borrowed_books[title] = self.books[title]
                self.borrowers[email].borrowed_books.append(title)
                self.save_data()
                print("✅ Book borrowed successfully!")
            else:
                print("❌ Book is not available or does not exist.")
        else:
            print("❌ Borrower not registered.")
        print("===================================")

    def return_book(self):
        print("\n========== Return Book ==========")
        email = input("Enter borrower email: ")
        if email in self.borrowers:
            title = input("Enter book title: ")
            if title in self.borrowed_books and title in self.borrowers[email].borrowed_books:
                self.books[title].status = "Available"
                del self.borrowed_books[title]
                self.borrowers[email].borrowed_books.remove(title)
                self.save_data()
                print("✅ Book returned successfully!")
            else:
                print("❌ Book is not borrowed by this borrower.")
        else:
            print("❌ Borrower not registered.")
        print("===================================")

    def display_books(self):
        print("\n========== All Books ==========")
        if not self.books:
            print("No books available.")
        for book in self.books.values():
            print(f"\n📘 Title : {book.title}")
            print(f"✍️  Author: {book.author}")
            print(f"📌 Status: {book.status}")
            print("------------------------------")
        print("================================")

    def check_account(self):
        print("\n========== Check Borrower Account ==========")
        email = input("Enter borrower email: ")
        if email in self.borrowers:
            if not self.borrowers[email].borrowed_books:
                print("✅ You have no borrowed books.")
            else:
                print("📚 Borrowed Books:")
                for book_title in self.borrowers[email].borrowed_books:
                    print(f"\n📘 Title : {book_title}")
                    print(f"✍️  Author: {self.books[book_title].author}")
                    print("------------------------------")
        else:
            print("❌ Borrower not registered.")
        print("===========================================")
