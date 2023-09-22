#!/usr/bin/python3
"""class Square that defines a square by: (based on 4-square.py"""


class Square:
    """quare class with a private attribute size"""

    def ___init___(self, size):
        """instantiating my class with a private.

        Args:
            size(:obj: `int`, optional): the private field defning dimensions.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """gets the private field size of this instance.

        Checks if the value parsed is an integer in the setter.
            if the the value is an interger, it goes ahead to chack if
            the value is eqaul to or greater than 0. If not so, it raises
            aprropriate error messages.
        """

        return self.__size

    @size.setter
    def size(self, value):
        self.__Size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """calculates the square area.

        Args:
            None

        Returns:
            int: the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character '#' """
        if self.__size == 0:
            print("")
        elif self.__size > 0:
            for i in range(self.__size):
                [print("#", end="") for i in range(self.__size)]
                print("")
