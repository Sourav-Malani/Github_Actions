import unittest
from main import add

class TestWallet(unittest.TestCase):

    def test_add(self):  # Add `self` as the first parameter
        result = add(2, 3)
        assert result == 5

if __name__ == "__main__":
    unittest.main()
