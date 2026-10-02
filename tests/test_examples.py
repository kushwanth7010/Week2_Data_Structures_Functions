"""Regression checks for the introductory data-structures exercises."""
import unittest

from data_cleaning import filter_data, remove_duplicates
from functions_examples import factorial, filter_even, sum_of_squares


class DataStructuresTests(unittest.TestCase):
    def test_unique_values_keep_their_original_order(self):
        self.assertEqual(remove_duplicates([10, 20, 10, 30, 20]), [10, 20, 30])
        self.assertEqual(remove_duplicates([]), [])

    def test_filter_data_includes_threshold(self):
        self.assertEqual(filter_data([1, 3, 5, 3], 3), [3, 5, 3])

    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squares([1, -2, 3]), 14)
        self.assertEqual(sum_of_squares([]), 0)

    def test_filter_even(self):
        self.assertEqual(filter_even([1, 2, 3, 4, -6]), [2, 4, -6])

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)

    def test_factorial_rejects_invalid_inputs(self):
        with self.assertRaises(ValueError):
            factorial(-1)
        for invalid in (2.5, "5", True):
            with self.subTest(invalid=invalid):
                with self.assertRaises(TypeError):
                    factorial(invalid)


if __name__ == "__main__":
    unittest.main()
