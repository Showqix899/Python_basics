
class Library:

    def __init__(self,name):
        self.name = name
        self.books=[]


    def add_book(self,book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author


library=Library("IIUC CENTRAL LIBRARY")

book1=Book("Harry Potter", "j.K Rowling")
book2=Book("Lord Of The Rings","J.R.R Tolkien")
book3=Book("Game Of Thrones","Goerge Martin")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

for book in library.list_books():
    print(book)

