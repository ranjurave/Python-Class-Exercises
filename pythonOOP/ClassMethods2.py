class Book:
    TYPE = ("hardcover","papercover")
    def __init__(self, bname, book_type, bweight ):
        self.bname = bname
        self.bweight = bweight
        self.book_type = book_type

    def __repr__(self):
        return f"{self.bname} has {self.bweight}g weight"

    @classmethod
    def hardcover(cls, bname, page_weight):
        return cls(bname, cls.TYPE[0], page_weight+200)

    @classmethod
    def papercover(cls, bname, page_weight):
        return cls(bname, cls.TYPE[1], page_weight)


book1 = Book.hardcover("Harry Potter", 800)
book2 = Book.papercover("Python", 500)
print(book1)
print(book2)