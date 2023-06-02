#!/usr/bin/python3
"""

This module defines text_indentation function

"""


def text_indentation(text):
    """
    This function prints 2 lines after ., ?, :
    """

    if type(text) != str:
        raise TypeError("text must be a string")
    text = text.strip()
    letter = 0
    while (letter in range(len(text))):
        if text[letter] in ['.', '?', ':']:
            print(text[letter], end="")
            print("\n")
            letter += 1
        else:
            print(text[letter], end="")
        letter += 1
