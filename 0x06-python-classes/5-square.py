#!/usr/bin/python3
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
        """ Returns Area
        """
        return self.__size**2

    @property
    def size(self):
        """ Defines attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets size
        """
        if type(value) == int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
    def my_print(self):
        """ Prints square
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#'*self.__size)
