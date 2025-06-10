class Book:
    totalBooks = 0  # Class variable to track total books created

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        Book.totalBooks += 1  # Increment totalBooks when a new book is created

    def shortDescription(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    @classmethod
    def getTotalBooks(cls):
        return cls.totalBooks

# 1) Create three Book objects
book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)

# 2) Print the short description of each
# print(book1.shortDescription())
# print(book2.shortDescription())
# print(book3.shortDescription())

# 3) Create a list of the three books
books = [book1, book2, book3]


for book in books:
   print( book.shortDescription())

# 4) Print the total number of books
print("Total number of books:", Book.getTotalBooks())
