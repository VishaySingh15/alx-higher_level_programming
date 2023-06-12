#!/usr/bin/python3
"""

This module defines the base geometry class

"""


class BaseGeometry:
    """
    This class defines the base geometry method
    """

    def area(self):
        """
        This method raises an exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates a value
        """

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
