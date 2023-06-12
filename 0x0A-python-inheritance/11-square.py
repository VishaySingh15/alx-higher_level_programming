#!/usr/bin/python3
"""

This module defines the Square class

"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    This class defines a square object
    """

    def __init__(self, size):
        """
        This method instatiates the object
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Calculates area of square
        """

        return super().area()

    def __str__(self):
        """
        This method returns square details
        """

        return f"[Square] {self.__size}/{self.__size}"
