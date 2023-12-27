#!/usr/bin/python3
"""The class `Rectangle` inherits from `Base` class."""
from models.base import Base


class Rectangle(Base):
    """`Rectangle` defines a four sided shape with two equal opposite sides."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """The instance class inherits the `id` attriibute from `Base` Class.

        Args:
            width (int): Describes the longest length of the object `Rectangle`
            height (int): Describe the shortest length of the object Recatangle
            x (int): Describes the coordinates of the object on a 2-D Plane.
            y (int): Describes the y axis of object on the 2-D plane.
            id (:obj: `int`, optional): class attribute.

        Attributes:
            __width (int): private instant attribute.
            __height (int): private instance attribute.
            __x (int: private instance attribute.
            __y (int): private instance attribute.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for `width` attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for `height` attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for `x` attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
         if value < 0:
             raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for `y` attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
