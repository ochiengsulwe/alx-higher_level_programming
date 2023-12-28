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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for `width` attribute.

        The setter checks if the value inputed is a valid integer,
        i.e. the value is greater than zero.
        The setter also doesn't allow values below 1 as dimensions.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for `height` attribute

        The setter validates if the value parsed is a valid integer.
        It doesn't allow for values below 1 as well as negative values.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for `x` attribute.

        The setter validate if the corsinate value parsed in a valid integer.
        Being that values here are a representation of cordinates,
            value 0 is allowed.
        """
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
        """Getter for `y` attribute.

        The setter validates if the value parsed in a valid integer.
        Being  that the value represents a point cordinate, value 0 isallowed.
        Only negative numbers are flagged.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Claculates the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Prints to the stdout a rectangle using `#`"""
        rec = [
                ['#' for shape in range(self.__width)]
                for shape in range(self.__height)
        ]
        for row in rec:
            print(''.join(row))

    def __str__(self):
        return (
                f"[{self.__class__.__name__}] ({self.id})"
                f"{self.__x}/{self.__y} - {self.__width}/{self.__height}"
            )
