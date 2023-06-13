#!/usr/bin/python3
"""

This module defines function write_file

"""


def write_file(filename="", text=""):
    """
    This function writes to a file
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
