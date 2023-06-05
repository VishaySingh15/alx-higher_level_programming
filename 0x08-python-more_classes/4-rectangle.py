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

    def area(self):
        """
        Returns area of rectangle
        """

        return self.__height * self.__width

    def perimeter(self):
        """
        Return perimeter of rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns rectangle string
        """

        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            rect += '#' * self.__width + '\n'

        return rect[:-1]

    def __repr__(self):
        """
        Returns a string representation of the object
        """

        return f"Rectangle({self.__width}, {self.__height})"
