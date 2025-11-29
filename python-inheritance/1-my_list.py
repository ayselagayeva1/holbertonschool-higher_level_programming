#!/usr/bin/python3
"""
1-my_list module
"""


class MyList(list):
    """MyList class inherits from list"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
