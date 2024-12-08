class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []  # Store articles as a list

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def articles(self):
        return self._articles  # Return the list of articles

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []  # Store articles as a list

    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        return self._articles  # Return the list of articles
