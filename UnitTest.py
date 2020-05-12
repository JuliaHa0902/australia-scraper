import unittest
from unittest.mock import patch
import cnn

class Test_CNN(unittest.TestCase):

    def test_print(self):
        headline = ["a", "a", "a"]
        result = cnn.print_australia_latest(headline)
        self.assertEqual (result, {"a"})

        headline = []
        result = cnn.print_australia_latest(headline)
        self.assertEqual (result, 'None')
        

if __name__ == '__main__':
    unittest.main()
