class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Invalid name")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Invalid name")
        self._name = value

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("Input must be a valid Magazine instance")
        article = Article(self, magazine, title)
        if article not in self._articles:
            self._articles.append(article)
            magazine._articles.append(article)
        return article

    def topic_areas(self):
        return list({article.magazine.category for article in self._articles})


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters")
        if not isinstance(category, str) or len(category.strip()) == 0:
            raise ValueError("Category must be a valid non-empty string")
        self._name = name
        self._category = category
        self._articles = []
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Category must be a valid non-empty string")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        return [author for author, count in author_counts.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        return max(cls.all_magazines, key=lambda mag: len(mag._articles), default=None)


class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be a valid Author instance")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be a valid Magazine instance")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title

        Article.all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise ValueError("New author must be a valid Author instance")
        self._author._articles.remove(self)
        new_author._articles.append(self)
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("New magazine must be a valid Magazine instance")
        self._magazine._articles.remove(self)
        new_magazine._articles.append(self)
        self._magazine = new_magazine
