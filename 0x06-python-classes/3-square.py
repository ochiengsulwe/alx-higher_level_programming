#!/usr/bin/python3
"""class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """Defines a shape of forur equal sides"""

    def __init__(self, size=0):
        """instantiating my class with an optional field.

        Args:
            size(:obj: `int`, optional): defines the square dimensions.

        Returns:
            int: the area of the square.
        """

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """calculates the area of the square.

        Args:
            None

        Returns:
            int: the value of the areaof the square.
        """
        return (self.__size ** 2)
