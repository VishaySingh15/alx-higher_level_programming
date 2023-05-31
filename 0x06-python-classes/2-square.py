#!/usr/bin/python3
""" This module creates a simple Square class
    and initialises it and checks for errors
"""


class Square:
    """ Class defines a square by size
    """
    def __init__(self, size=0):
        """ Initilises square anf checks for errors
        """
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
