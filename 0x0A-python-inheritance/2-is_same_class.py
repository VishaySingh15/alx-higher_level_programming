#!/usr/bin/python3
"""

This module defines is_same_class method

"""


def is_same_class(obj, a_class):
    """
    This function determines if an object is an instance
    of the class
    """

    return type(obj) == a_class
