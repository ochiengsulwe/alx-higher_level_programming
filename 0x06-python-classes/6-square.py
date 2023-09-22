#!/usr/bin/python3
"""Writes a class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """instantiates the square instance with two optional fields.

        Args:
            size(:obj: `int`, optional): the size of the square.
            position(:obj: `tuple` of `int`, optional): the square position.
            """
        self.__size = size
        self.__position = position

    def area(self):
        """calculates the sqaure area.

        Args:
            None
        Returns:
            int: area of the sqaure of dimension size * size.
        """
        return self.__size ** 2

    @property
    def size(self):
        """retrives the square dimensions.

        checks if size is is an integer and also greater than zero
            before allowing computations. If otherwise, it rasies error
            messages accordingly.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints in stdout the square with the character '#' """
        if self.__size > 0:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")

    @property
    def position(self):
        """sets up the private field position accordingly."""

        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(val, int) and val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
