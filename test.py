import unittest
from main import add

class TestAddition(unittest.TestCase):
    def test_addition(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()
