#!/usr/bin/python3
""" This module creates a simple Square class
    and initialises it and checks for errors
    Contains function for area of square and
    setter
"""


class Square:
    """ Defines square
    """
    def __init__(self, size=0):
        """ Initialises square
        """
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Returns area
        """
        return self.__size**2

    @property
    def size(self):
        """ Creates attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """defines setter
        """
        if type(value) == int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
