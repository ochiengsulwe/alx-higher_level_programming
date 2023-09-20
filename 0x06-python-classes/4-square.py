#!/usr/bin/python3
"""Class Square that defines a square by: (based on 4-square.py)."""


class Square:
    """a class definning a shape of equal foursides.

    This class illustrates a shape of same size.
    """

    def __init__(self, size=0)
    """instantiating the classs with optional field size.

    Args:
        size(:obj: `int`, optional): the shape dimension
    """
    self.__size = size
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    @property
    def size(self):
        """int: retrives the value of private field size"""

        return (self.__size)

    @size.setter
    def size(self, value):
        self.__size = size

    def area(self):
        """computes the square's area.

        Args:
            None

        Returns:
            int: the area in sq units
        """
        return (self.__size ** 2)
