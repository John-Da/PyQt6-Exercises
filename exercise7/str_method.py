discount_precent = 10


class Book:
    totalBooks = 0

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        Book.totalBooks += 1

    def __str__(self):
        return f"{self.title} by {self.author} has discounted price as {self.get_discount_price(discount_precent):.2f} Baht"

    @classmethod
    def get_total_books(cls):
        return cls.totalBooks

    def get_discount_price(self, discount_precent):
        return self.price - (self.price * (discount_precent / 100))


books = []
books.append(Book("ชีวิตเรามีแค่สี่พันสัปดาห์", "Oliver Burkeman", 225.25))
books.append(Book("Working with AI", "Thomas and Steven", 810))
books.append(
    Book("Practicing Trustworthy Machine Learning", "Yada, Matthew and Subho", 1550)
)

total_books = Book.get_total_books()
print(f"Total books: {total_books}")
for i in range(total_books):
    print(books[i])
