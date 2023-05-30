#!/usr/bin/python3
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
