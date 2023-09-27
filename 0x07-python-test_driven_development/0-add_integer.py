#!/usr/bin/python3
"""Defines a function for adding two integers or floats."""


def add_integer(a, b=98):
    """The function adds to integers.

    Args:
        a(int): the first argument to the function. Should never be left empty.
        b(:obj, `int', optional): the second argument of the function.
            will always default to 98 if left empty.

    Returns:
        int: the sum of the parsed values.
    """

    if not isinstance(a, (int, float)):
        raise TypeError(a must be an integer)
    if not isinstance(b, (int, float)):
        raise TypeError(b must be an integer)

    result = int(a) + int(b)

    return result
