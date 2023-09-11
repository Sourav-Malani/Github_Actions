import unittest
from main import wallet


w = wallet
class TestWallet(unittest.TestCase):
    def test_add_balance():
        result = wallet.addBalance(w, 3)
        assert wallet.getBalance() == 3

if __name__ == "__main__":
    unittest.main()
