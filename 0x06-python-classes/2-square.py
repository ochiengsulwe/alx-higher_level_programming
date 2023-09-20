#!/usr/bin/python3
"""Describing a square"""


class Square:
    """A square definition"""

    def __init__(self, size=0):
        """instantiating my class with size of default value 0.

        Args:
            __size(int): an integer value to represents the square size.
        """

        self.__size = size
        if not isinstance(size, int):
            raise TypeError(size must be an integer)
        elif size < 0:
            raise ValueError(size must be >= 0)
