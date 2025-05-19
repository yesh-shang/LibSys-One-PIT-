class Book:
    def __init__(self, title, author, status="Available"):
        self.title = title
        self.author = author
        self.status = status

    def to_dict(self):
        return {"title": self.title, "author": self.author, "status": self.status}

    @staticmethod
    def from_dict(data):
        return Book(data["title"], data["author"], data["status"])


class Borrower:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.borrowed_books = []

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "borrowed_books": self.borrowed_books
        }

    @staticmethod
    def from_dict(data):
        borrower = Borrower(data["name"], data["email"])
        borrower.borrowed_books = data["borrowed_books"]
        return borrower
