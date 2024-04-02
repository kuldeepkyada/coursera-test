class library:
  def __init__(self):
    self.noBooks = 0
    self.books = []

  def addBook(self,book):
    self.books.append(book)
    self.noBooks = len(self.books)

  def count(self):
    print(f"There are {self.noBooks} books in the library")

c = library()
c.addBook("Harry potter")
c.addBook("Rich Dad Poor Dad")
c.addBook("Albert Einstein")
c.count()