class Book:
    def __init__(self, title, author):
        """
        Base class for a book.
        :param title: Title of the book (str).
        :param author: Author of the book (str).
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        String representation of the Book instance.
        :return: A string in the format "Book: (title) by (author)".
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Derived class for an eBook.
        :param title: Title of the book (str).
        :param author: Author of the book (str).
        :param file_size: File size of the eBook in KB (int).
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        String representation of the EBook instance.
        :return: A string in the format "EBook: (title) by (author), File Size: (file_size)KB".
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Derived class for a print book.
        :param title: Title of the book (str).
        :param author: Author of the book (str).
        :param page_count: Number of pages in the book (int).
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        String representation of the PrintBook instance.
        :return: A string in the format "PrintBook: (title) by (author), Page Count: (page_count)".
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """
        Class representing a library, using composition to manage a collection of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book to the library.
        :param book: An instance of Book, EBook, or PrintBook.
        """
        self.books.append(book)

    def list_books(self):
        """
        Lists all books in the library.
        """
        for book in self.books:
            print(book)
