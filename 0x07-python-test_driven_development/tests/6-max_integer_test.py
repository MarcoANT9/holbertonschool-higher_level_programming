#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        """ Test if the input argument is empty."""

        data = []
        result = max_integer(data)
        self.assertEqual(result, None)

    def test_number_int_data(self):
        """ Test the function for a list of integers."""

        data = [1, 2, 3, 2]

        error_msg = "The list must contain only integers"

        for i in range(len(data)):
            assert type(data[i]) == int, error_msg

        result = max_integer(data)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
