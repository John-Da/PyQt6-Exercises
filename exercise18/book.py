class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            return f"{self.title} is already borrowed."

        if not self.is_borrowed:
            self.is_borrowed = True
            return f"{self.title} has been borrowed."
        # Check if the book is not already borrowed
        # If it's not borrowed, mark it as borrowed
        # Return a message indicating the book has been borrowed
        # If the book is already borrowed, return a message indicating so
        # pass

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"{self.title} has been returned."
        if not self.is_borrowed:
            return f"{self.title} was not borrowed."
        # Check if the book is currently borrowed
        # If it is borrowed, mark it as no longer borrowed
        # Return a message indicating the book has been returned
        # If the book wasn't borrowed, return a message indicating so
        # pass


book1 = Book("Python Basics", "John Doe")
print(book1.borrow())
print(book1.borrow())
print(book1.return_book())
print(book1.return_book())
