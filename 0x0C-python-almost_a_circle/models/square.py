#!/usr/bin/python3
"""A square is a special type of a rectangle. Inherits from class Rectangle."""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """Defines a special type of a rectangle with equal sides"""
    def __init__(self, size, x=0, y=0, id=None):
        """The size of the square represents the both opposite sides.

        Args:
            size (int): The lenth of either side.
            x (int): The cordinate representation of the x-axis on a plane.
            y (int): The cordinate representation of the y-axis on a 2-D plane.
            id (int): The special identifier of the instance.

        Attributes:
            __size (int): The dimension of the square.
        """
        super().__init__(size, size, x, y, id)

        @property
        def size(self):
            """Assigns the value for the square instance.

            The value is determined from both the width parse and the height.
            """
            return (self.width)

        @size.setter
        def size(self, value):
            self.width = value
            self.height = value

        def __str__(self):
            return (
                   f" [{self.__class__.__name__}] ({self.id})"
                   f"{self.x}/{self.y} - {self.width}"
                )
