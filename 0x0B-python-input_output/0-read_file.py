#!/usr/bin/python3
"""

This module defines the read_file method

"""


def read_file(filename=""):
    """
    This method reads a file and outputs to stdout
    """

    with open(filename, encoding="utf-8") as f:
        text = f.read()
        print(text, end="")
