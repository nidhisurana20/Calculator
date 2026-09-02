import math
import unittest

from calculator import add, subtract, multiply, divide, power, sqrt, CalculatorError


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(CalculatorError):
            divide(1, 0)

    def test_power(self):
        self.assertEqual(power(2, 5), 32)

    def test_sqrt(self):
        self.assertEqual(sqrt(9), 3)
        with self.assertRaises(CalculatorError):
            sqrt(-1)


if __name__ == "__main__":
    unittest.main()
