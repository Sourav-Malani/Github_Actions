import unittest
from main import wallet

w = wallet

class TestWallet(unittest.TestCase):

    def test_add_balance(self):  # Add `self` as the first parameter
        result = w.addBalance(2, 3)
        assert w.getBalance() == 3

if __name__ == "__main__":
    unittest.main()
