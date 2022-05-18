class Book:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Book : {self.name}"

class BookShelf:
    def __init__(self, *book):
        self.book = book
    def __str__(self):
        return f"Book shelf with {len(self.book)} in it"
    def displayLibrary(self) -> Book:
        for b in self.book:
            print(b)

b1 = Book("Harry Potter")
b2 = Book("Python")
bShelf = BookShelf(b1,b2)
# print(b1)
# print(b2)
print(bShelf)
bShelf.displayLibrary()


