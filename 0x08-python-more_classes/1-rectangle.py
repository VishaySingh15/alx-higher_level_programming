#!/usr/bin/python3
"""

This module creates the rectangle class.

"""


class Rectangle:
    """
    This defines the Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        This is our constructor that sets our attributes
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter returns width
        """

        return self.__width

    @width.setter
    def width(self, width):
        """
        The setter sets width
        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """
        Getter returns height
        """

        return self.__height

    @height.setter
    def height(self, height):
        """
        The setter sets height
        """

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
