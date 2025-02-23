class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        raise AttributeError("Author name cannot be changed")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        magazine_list = list(set(article.magazine for article in self.articles()))
        return magazine_list if magazine_list else []

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = list(set(magazine.category for magazine in self.magazines()))
        return topics if topics else None


class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not 2 <= len(name) <= 16:
            raise ValueError("Name must be between 2 and 16 characters")
        if not isinstance(category, str):
            raise TypeError("Category must be a string")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")

        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        if not 2 <= len(new_name) <= 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise TypeError("Category must be a string")
        if len(new_category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        authors = list(set(article.author for article in self.articles()))
        return authors if authors else []

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1

        top_authors = [author for author, count in author_counts.items() if count > 2]
        return top_authors if top_authors else []  # ✅ FIXED: Now returns [] instead of None


class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be a Magazine instance")
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not 5 <= len(title) <= 50:
            raise ValueError("Title must be between 5 and 50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        raise AttributeError("Title cannot be modified after initialization")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise TypeError("Author must be an Author instance")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise TypeError("Magazine must be a Magazine instance")
        self._magazine = new_magazine
