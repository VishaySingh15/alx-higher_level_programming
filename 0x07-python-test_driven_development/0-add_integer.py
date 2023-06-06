#!/usr/bin/python3
"""

Addition module

"""


def add_integer(a, b=98):
    """
    Adds 2 integers and returns result
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
