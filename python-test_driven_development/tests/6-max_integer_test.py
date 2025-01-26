#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list_case(self):
        self.assertEqual(max_integer([]), None)

    def test_zero_number_case(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_max_at_beginning_case(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_max_operated_integer_case(self):
        self.assertEqual(max_integer([-3, -5 * -5, 12, -1]), 25)

    def test_max_float_numbers(self):
        self.assertEqual(max_integer([50, 51, 50, 49]), 51)

    def test_max_integer_case(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_number_in_repeated_case(self):
        self.assertEqual(max_integer([1000, 1000, 1000]), 1000)

    def test_single_number_case(self):
        self.assertEqual(max_integer([1]), 1)

    def test_negative_numbers_case(self):
        self.assertEqual(max_integer([-10, -5, -2, -1]), -1)

    def test_max_integer_with_negative_mixed_case(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_max_integer_with_mixed_case(self):
        self.assertEqual(max_integer([1, 2, 4, 3, 2]), 4)

    def test_max_integer_with_infinity_case(self):
        self.assertEqual(max_integer([1, -float('inf'), 2]), 2)

    def test_large_number_list_case(self):
        self.assertEqual(max_integer([10000, 20000, 30000]), 30000)

    def test_max_integer_with_float_in_list_case(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_max_integer_with_large_list_case(self):
        self.assertEqual(max_integer([
            901, 902, 903, 904, 905, 906, 907, 908, 909, 910,
            911, 912, 913, 914, 915, 916, 917, 918, 919, 920,
            919, 918, 917, 1000, 915, 914, 913, 912, 911, 910,
            909, 908, 907, 906, 905, 904, 903, 902, 901]), 1000)

    def test_max_float_number_case(self):
        self.assertEqual(max_integer([float('inf'), 1, 2]), float('inf'))

    def test_max_integer_with_loop_case(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 25)

    def test_string_number_in_list_case(self):
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def test_tuple_in_list_case(self):
        with self.assertRaises(TypeError):
            max_integer([10, (20, 30)])

    def test_dictionary_in_list_case(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

    def test_non_iterable_input_case(self):
        with self.assertRaises(TypeError):
            max_integer(1)