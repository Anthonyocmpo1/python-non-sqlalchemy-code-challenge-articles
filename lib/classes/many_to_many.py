class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            print("Error: Author must be of type Author.")
        elif not isinstance(magazine, Magazine):
            print("Error: Magazine must be of type Magazine.")
        elif not isinstance(title, str) or not (5 <= len(title) <= 50):
            print("Error: Title must be a string between 5 and 50 characters.")
        else:
            self._title = title
            self.author = author
            self.magazine = magazine
            Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            print("Error: Title is immutable once set.")
        elif not isinstance(value, str) or not (5 <= len(value) <= 50):
            print("Error: Title must be a string between 5 and 50 characters.")
        else:
            self._title = value

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            print("Error: Name must be a non-empty string.")
        else:
            self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        print("Error: Author name is immutable once set.")

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def topic_areas(self):
        if not self.magazines():
            return None
        return list({magazine.category for magazine in self.magazines()})

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            print("Error: Name must be a string between 2 and 16 characters.")
        elif not isinstance(category, str) or len(category) == 0:
            print("Error: Category must be a non-empty string.")
        else:
            self._name = name
            self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            print("Error: Name must be a string between 2 and 16 characters.")
        else:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            print("Error: Category must be a non-empty string.")
        else:
            self._category = value

    def contributors(self):
        return list({article.author for article in self.articles()})

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        contributors = [author for author, count in author_counts.items() if count > 2]
        return contributors if contributors else None


# Create instances and produce output

magazine1 = Magazine("Tech Monthly", "Technology")
magazine2 = Magazine("Science Weekly", "Science")

author1 = Author("Alice Smith")
author2 = Author("Bob Johnson")

# Add articles
article1 = author1.add_article(magazine1, "The Future of AI")
article2 = author1.add_article(magazine1, "Quantum Computing: An Overview")
article3 = author2.add_article(magazine2, "Exploring the Depths of the Ocean")

# Print articles by author
print(f"Articles by {author1.name}:")
for article in author1.articles():
    print(f"- {article.title} in {article.magazine.name}")

# Print articles in magazine
print(f"\nArticles in {magazine1.name}:")
for article in magazine1.articles():
    print(f"- {article.title} by {article.author.name}")

# Print contributing authors
print(f"\nContributing authors in {magazine1.name}:")
for author in magazine1.contributors():
    print(f"- {author.name}")

# Print topics
print(f"\nTopics for {author1.name}:")
for topic in author1.topic_areas() or []:
    print(f"- {topic}")
