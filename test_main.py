import unittest
from main import wallet

# class test_TestAddition(unittest.TestCase):
#     def test_addition(self):
#         result = add(2, 3)
#         self.assertEqual(result, 5)

#create class intsance
w = wallet
def test_add_balance():
    result = wallet.addBalance(w, 3)
    assert wallet.getBalance() == 3

if __name__ == "__main__":
    unittest.main()
