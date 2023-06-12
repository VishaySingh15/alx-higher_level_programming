#!/usr/bin/python3
"""

This module defines the Rectangle class

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class defines the instantiation method
    """

    def __init__(self, width, height):
        """
        This method instatiates the object
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
