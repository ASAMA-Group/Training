import unittest
from unittest_module import operations


class TestOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(operations.add(6,4), 10)
        self.assertEqual(operations.add(-2,1), -1)

    def test_subtract(self):
        self.assertEqual(operations.subtract(5,2), 3)
        self.assertEqual(operations.subtract(8,0), 8)

    def test_multiplay(self):
        self.assertEqual(operations.multiplay(6,2), 12)
        self.assertEqual(operations.multiplay(4,0), 0)

    def test_division(self):
        self.assertEqual(operations.division(8,2), 4)
        self.assertRaises(ZeroDivisionError, operations.division, 6, 0)


if __name__ == "__main__":
    unittest.main