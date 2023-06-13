#!/usr/bin/python3
"""

This module defines the function save_to_json_file

"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an object to a text file
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
