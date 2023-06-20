#!/usr/bin/python3
"""

This module defines the base class

"""


class Base:
    """
    This class manages the id attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This constructor defines the id attribute
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
