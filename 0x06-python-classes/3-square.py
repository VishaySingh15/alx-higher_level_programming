#!/usr/bin/python3
""" This module creates a simple Square class
    and initialises it and checks for errors
    Contains function for area of square
"""


class Square:
    """ Class defines a square
    """
    def __init__(self, size=0):
        """ Initialises a square and check for errors
        """
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Returns Areas of square
        """
        return self.__size**2
