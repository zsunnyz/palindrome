import unittest
from palindrome import check_palindrome

class test_palindrome(unittest.TestCase):
    def test_even(self):
        self.assertTrue(check_palindrome("ww"))

if __name__ == "__main__":
    unittest.main()