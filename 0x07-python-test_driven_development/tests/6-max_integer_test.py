#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    This class defines unit tests for max_integer
    """

    def test_maxInt(self):
        """
        Test for the max integer
        """

        self.assertAlmostEqual(max_integer([5, 2, 9]), 9)
        self.assertAlmostEqual(max_integer([]), None)
