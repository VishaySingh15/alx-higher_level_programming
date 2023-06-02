#!/usr/bin/python3
"""

This module defines print_square

"""


def print_square(size):
    """
    This function prints a square of size
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print(size * '#')
