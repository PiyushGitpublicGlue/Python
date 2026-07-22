class Book():
    def __init__(self,title,author):
        self.is_borrowed=False
        self.title=title
        self.author=author

class Library():
    def __init__(self):
        self.book=[]

    def add_book(self,book_obj):
        self.book.append(book_obj)
        print(f"Added - Title: {book_obj.title}, Author: {book_obj.author}, Borrowed:{book_obj.is_borrowed}")

    def borrow_book(self,title):
        for bo in self.book:
            if bo.title==title:
                if bo.is_borrowed==False:
                    bo.is_borrowed=True
                    print(f"You checked out {title}")
                else:
                    print(f"Sorry, {title} is already checked out.")
                return
        print(f"We don't have {title} book.")


book1 = Book("The Hobbit", "J.R.R. Tolkien")
book2 = Book("1984", "George Orwell")

my_library = Library()
my_library.add_book(book1)
my_library.add_book(book2)

my_library.borrow_book("1984")        # "You checked out 1984"
my_library.borrow_book("1984")        # "Sorry, 1984 is already checked out."
my_library.borrow_book("Dune")        # "We don't have that book."
