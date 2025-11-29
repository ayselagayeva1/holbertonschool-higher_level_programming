#!/usr/bin/python3
"""Function that checks inheritance from a class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class thass."""
    obj_type = type(obj)
    return (issubclass(obj_type, a_class)
            and obj_type is not a_class)
