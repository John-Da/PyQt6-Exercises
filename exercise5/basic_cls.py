class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_discount_price(self, discount_precent):
        return self.price - (self.price * (discount_precent / 100))

    

book = Book("ชีวิตเรามีแค่สี่พันสัปดาห์", "Oliver Burkeman", 225.25)
print(f"{book.title} by {book.author} has discounted price as {book.get_discount_price(10):.2f} Baht")
