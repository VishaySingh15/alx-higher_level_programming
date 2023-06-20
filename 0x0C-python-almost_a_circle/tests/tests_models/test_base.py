#!/usr/bin/python3
"""

This module defines the test class for the base class

"""
import unittest
from models.base import Base


class TestBaseCases(unittest.TestCase):
    """
    This test suite tests the methods of the Base class
    """

    def setUp(self):
        """
        Sets nb_objects to 0 for each test
        """

        Base._Base__nb_objects = 0

    def test_id_int(self):
        """
        Passes an int value
        """

        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_id_none(self):
        """
        No value passed
        """

        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_nb_objects(self):
        """
        Checks if nb_objects increments
        """

        obj = Base()
        obj2 = Base(5)
        obj3 = Base()
        self.assertEqual(obj3.id, 2)
