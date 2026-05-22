import unittest
from math_utils import (
    add,
    subtract,
    multiply,
    divide,
)

class TestMathUtils(unittest.TestCase):

    BAD_TYPES = [
        ("6", 7),
        ([6], 7),
        (True, 7),
        (None, 7),
    ]

    def test_add(self):
        cases = [
            (1, 3, 4),
            (-3, 3, 0),
            (3.5, 4.5, 8.0)
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(add(a, b), expected)

    def test_add_type(self):
        for a, b in self.BAD_TYPES:
            with self.subTest(a=a, b=b):
                with self.assertRaises(TypeError):
                    add(a, b)

    def test_subtract(self):
        cases = [
            (2, 1, 1),
            (-3, 3, -6),
            (3.5, 4.5, -1.0)
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(subtract(a, b), expected)

    def test_subtract_type(self):
        for a, b in self.BAD_TYPES:
            with self.subTest(a=a, b=b):
                with self.assertRaises(TypeError):
                    subtract(a, b)

    def test_multiply(self):
        cases = [
            (6, 7, 42),
            (-3, 4, -12),
            (3.5, 4.5, 15.75)
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(multiply(a, b), expected)

    def test_multiply_type(self):
        for a, b in self.BAD_TYPES:
            with self.subTest(a=a, b=b):
                with self.assertRaises(TypeError):
                    multiply(a, b)

    def test_divide(self):
        cases = [
            (42, 6, 7.0),
            (-36, 6, -6.0),
            (15.5, 5, 3.1)
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertAlmostEqual(divide(a, b), expected)

    def test_divide_type(self):
        for a, b in self.BAD_TYPES:
            with self.subTest(a=a, b=b):
                with self.assertRaises(TypeError):
                    divide(a, b)

    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()