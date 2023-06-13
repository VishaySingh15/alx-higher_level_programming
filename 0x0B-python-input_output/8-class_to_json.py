#!/usr/bin/python3
"""

This module defines the class_to_json function

"""


def class_to_json(obj):
    """
    Function that retuns the dictionary description of an obj
    """

    dic = {}
    if hasattr(obj, "__dict__"):
        dic = obj.__dict__.copy()
    return dic
