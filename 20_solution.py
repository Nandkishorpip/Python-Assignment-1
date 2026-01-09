class Library:
    def __init__(self, books):
        # Initialize with a list of available books
        self.available_books = books
        self.borrowed_books = []

    def borrow_book(self, book_name):
        if book_name in self.available_books:
            self.available_books.remove(book_name)
            self.borrowed_books.append(book_name)
            print(f"You have successfully borrowed: {book_name}")
        elif book_name in self.borrowed_books:
            print(f"Sorry, the book '{book_name}' is already borrowed.")
        else:
            print(f"Sorry, the book '{book_name}' is not available in the library.")

    def show_borrowed_books(self):
        # Display all borrowed books
        if self.borrowed_books:
            print(f"Books borrowed: {', '.join(self.borrowed_books)}")
        else:
            print("No books have been borrowed.")

    def show_available_books(self):
        # Display all available books
        if self.available_books:
            print(f"Available books: {', '.join(self.available_books)}")
        else:
            print("No books are currently available.")


if __name__ == "__main__":
    library = Library(["Python Programming", "Data Science 101", "AI Basics", "Machine Learning Advanced"])

    library.borrow_book("Python Programming")
    library.borrow_book("Data Science 101")
    library.borrow_book("AI Basics")
    library.borrow_book("Python Programming")

    library.show_borrowed_books()


    library.show_available_books()
