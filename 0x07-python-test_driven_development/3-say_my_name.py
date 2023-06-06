#!/usr/bin/python3
"""

This modules defines function say_my_name

"""


def say_my_name(first_name, last_name=""):
    """
    This function prints first name and last name
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
