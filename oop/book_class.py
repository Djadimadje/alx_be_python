class Book:
    def __init__(self, title, author, year):
        """
        Constructor to initialize a Book instance.
        :param title: Title of the book (str).
        :param author: Author of the book (str).
        :param year: Publication year of the book (int).
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor to print a message when the object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation of the Book instance.
        :return: A string in the format "(title) by (author), published in (year)".
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation of the Book instance.
        :return: A string that can recreate the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
