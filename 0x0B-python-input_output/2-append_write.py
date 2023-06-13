#!/usr/bin/python
"""

This module defines function append_write

"""


def append_write(filename="", text=""):
    """
    This function appends to a text file
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
