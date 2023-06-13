#!/usr/bin/python3
"""

This module defines the Student class

"""


class Student():
    """
    This class instantiates a student object
    """

    def __init__(self, first_name, last_name, age):
        """
        This method initialises the attributes
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This method returns a dictionary representation of a student
        """

        return self.__dict__.copy()
