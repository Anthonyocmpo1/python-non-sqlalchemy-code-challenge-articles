class Article:
    def __init__(self, author, magazine, title):
        self._title = title  # Make it a private attribute
        self.author = author
        self.magazine = magazine

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise ValueError("Title is immutable")

class Author:
    def __init__(self, name):
        self._name = name  # Make it a private attribute

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise ValueError("Name is immutable")
