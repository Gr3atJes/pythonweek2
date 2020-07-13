import unittest
from app.models import Article

class TestArticle(unittest.TestCase):
    """
    Test class to test the behaviour of the movie class

    
    """
    self.new_article = Article("Bob","Random Title", "Short","random.com","random.jpg","12/12/12","None")

def test_instance(self):
    """
    Tests if instance of the Article class
    """
    self.assertTrue(isinstance(self.new_article,Article))

def test_init(self):
    """
    Tests for proper instantiation
    """
    self.assertEqual(self.new_article.author,"Bob")
