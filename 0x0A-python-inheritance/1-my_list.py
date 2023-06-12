#!/usr/bin/python3
"""

This module prints a list in ascending order

"""


class MyList(list):
    """
    This class defines print_sorted method
    """

    def print_sorted(self):
        """
        This method prints a list in ascending order
        """

        new_list = self.copy()
        new_list.sort()
        print(new_list)
