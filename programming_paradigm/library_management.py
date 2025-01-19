class Book:
    """
    A class to represent a book in the library.
    """

    def __init__(self, title, author):
        """
        Initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """
        Check out the book (mark it as unavailable).
        """
        if self._is_checked_out:
            print(f"'{self.title}' is already checked out.")
        else:
            self._is_checked_out = True
            print(f"'{self.title}' has been checked out.")

    def return_book(self):
        """
        Return the book (mark it as available).
        """
        if not self._is_checked_out:
            print(f"'{self.title}' is already available.")
        else:
            self._is_checked_out = False
            print(f"'{self.title}' has been returned.")

    def is_available(self):
        """
        Check if the book is available.

        Returns:
            bool: True if the book is available, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Return a string representation of the book.

        Returns:
            str: A string in the format "Title by Author".
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    A class to represent a library that manages a collection of books.
    """

    def __init__(self):
        """
        Initialize a Library instance.
        """
        self._books = []  # Private list to store books

    def add_book(self, book):
        """
        Add a book to the library.

        Args:
            book (Book): The book to add.
        """
        self._books.append(book)
        print(f"Added '{book.title}' to the library.")

    def check_out_book(self, title):
        """
        Check out a book by its title.

        Args:
            title (str): The title of the book to check out.
        """
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        print(f"Book with title '{title}' not found.")

    def return_book(self, title):
        """
        Return a book by its title.

        Args:
            title (str): The title of the book to return.
        """
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book with title '{title}' not found.")

    def list_available_books(self):
        """
        List all available books in the library.
        """
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(book)
        else:
            print("No available books.")
