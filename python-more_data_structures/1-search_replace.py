#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Return a new list where all occurrences of search are replaced by replace"""
    # Yeni list comprehension ilə yaratmaq
    new_list = [replace if x == search else x for x in my_list]
    return new_list
