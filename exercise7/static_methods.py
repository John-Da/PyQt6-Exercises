discount_precent = 10


class Book:
    totalBooks = 0

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        Book.totalBooks += 1

    @classmethod
    def get_total_books(cls):
        return cls.totalBooks

    def get_discount_price(self, discount_precent):
        return self.price - (self.price * (discount_precent / 100))

    def print_book_info(self):
        print(
            f"{self.title} by {self.author} has discounted price as {self.get_discount_price(discount_precent):.2f} Baht"
        )

    @staticmethod
    def is_expensive(price):
        return price > 1000

    def is_long_name(name):
        return len(name) > 30


books = []
books.append(Book("ชีวิตเรามีแค่สี่พันสัปดาห์", "Oliver Burkeman", 225.25))
books.append(Book("Working with AI", "Thomas and Steven", 810))
books.append(
    Book("Practicing Trustworthy Machine Learning", "Yada, Matthew and Subho", 1550)
)

total_books = Book.get_total_books()
print(f"Total books: {total_books}")
for i in range(total_books):
    books[i].print_book_info()

print(
    f"Is {books[0].title} expensive? {Book.is_expensive(books[0].get_discount_price(10))}"
)
print(
    f"Is {books[2].title} expensive? {Book.is_expensive(books[2].get_discount_price(10))}"
)
print(f"Is {books[0].title} a long book name? {Book.is_long_name(books[0].title)}")
print(f"Is {books[2].title} a long book name? {Book.is_long_name(books[2].title)}")
