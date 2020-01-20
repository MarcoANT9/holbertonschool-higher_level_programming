#!/usr/bin/python3
"""
This is the "My_list" class, usage:
>>> my_list([1, 4, 2, 3, 8])
[1, 2, 3, 4, 8]
"""


class MyList(list):
    """
    This is a child class inheriting properties from the
    "list" class.
    """
    def print_sorted(self):
        """
        This method prints the sorted list without modifying
        the original.
        """
        print(sorted(self))
