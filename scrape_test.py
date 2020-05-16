"""Using unittest to test scrape file"""
import unittest
import scrape

class ScrapeTests(unittest.TestCase):
    """Test if the class return None when there is no headline and remove all the duplicated headline"""

    def test_none(self):
        """Test if the class return None when there is no headline"""
        cnn_headline = scrape.Scraper("https://www.cnn.com/australia", "//img[@class='media__image media__image--responsive']", "//h3[@data-analytics='dummy_class']")
        cnn_headline.scraper()
        self.assertEqual(cnn_headline.print_headline(), "None")

    def test_duplicate(self):
        """Test the remove duplicate function"""
        cnn_headline = scrape.Scraper("https://www.cnn.com/australia", "//img[@class='media__image media__image--responsive']", "//h3[@data-analytics='dummy_class']")
        self.assertEqual(cnn_headline.remove_duplicate(["a", "a", "a"]), {"a"})

if __name__ == '__main__':
    unittest.main()
