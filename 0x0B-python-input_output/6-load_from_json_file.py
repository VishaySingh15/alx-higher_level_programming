#!/usr/bin/python3
"""

This module defines the function load_from_json_file

"""
import json


def load_from_json_file(filename):
    """
    This function loads an object from a text file
    """

    with open(filename, encoding="utf-8") as f:
        return json.load(f)
