from author import Author
from article import Article
from magazine import Magazine

# Create authors
author1 = Author("Carry Bradshaw")
author2 = Author("John Doe")
author3 = Author("Jane Doe")

# Create magazines
mag1 = Magazine("Vogue", "Fashion")
mag2 = Magazine("Architectural Digest", "Architecture")

# Create articles
article1 = Article(author1, mag1, "How to wear a tutu with style")
article2 = Article(author2, mag1, "The power of bold accessories")
article3 = Article(author1, mag2, "Modern architecture and style")
article4 = Article(author1, mag1, "10 fashion tips for winter")
article5 = Article(author3, mag1, "Vintage fashion resurgence")

# Debug relationships
print(author1.articles())
print(author1.magazines())
print(author1.topic_areas())

print(mag1.articles())
print(mag1.contributors())
print(mag1.article_titles())
print(Magazine.top_publisher())
