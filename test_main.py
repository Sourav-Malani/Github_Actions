import unittest
from main import add

class TestAddition(unittest.TestCase):
    def test_addition(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

class TestAddition2(unittest.TestCase):
    def test_addition(self):
        result = add(2, 4)
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()
