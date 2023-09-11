import unittest
from main import add

w = wallet

class TestWallet(unittest.TestCase):

    def test_add(self):  # Add `self` as the first parameter
        result = add(2, 3)
        assert result == 3

if __name__ == "__main__":
    unittest.main()
