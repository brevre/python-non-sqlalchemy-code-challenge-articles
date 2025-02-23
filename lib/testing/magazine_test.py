import pytest
from classes.many_to_many import Author, Magazine, Article

def test_article_titles():
    author = Author("Carry Bradshaw")
    magazine = Magazine("Vogue", "Fashion")

    Article(author, magazine, "How to wear a tutu with style")
    
    assert magazine.article_titles() == ["How to wear a tutu with style"]

def test_contributing_authors():
    author_1 = Author("Carry Bradshaw")
    author_2 = Author("Nathaniel Hawthorne")
    magazine = Magazine("Vogue", "Fashion")

    Article(author_1, magazine, "How to wear a tutu with style")
    Article(author_1, magazine, "Dating life in NYC")
    Article(author_1, magazine, "Fashion Secrets")
    Article(author_2, magazine, "Architecture Insights")

    assert author_1 in magazine.contributing_authors()
    assert author_2 not in magazine.contributing_authors()

    # Check that a magazine with no contributors returns an empty list, not None
    empty_magazine = Magazine("New Mag", "Tech")
    assert empty_magazine.contributing_authors() == []
