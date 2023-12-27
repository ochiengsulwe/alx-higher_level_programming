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
        if isinstance(width, int) and width > 0:
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
        self.validate_integer("width", value)
        self.validate_positive("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for `height` attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value)
        self.validate_positive("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for `x` attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.validate_cordinate("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for `y` attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.validate_cordinate("y", value)
        self.__y = value

    def validate_integer(self, attribute_name, value):
        """Checks for only integer inputs.

        Args:
            attribute_name (str): The attribute name to be checked.
            value (int): The integer value of the attribute to be checked.

        Raises:
            TypeError: If the value is not an integer.

        Example:
            validate_integer('width', 10)
        """

        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")

    def validate_positive(self, attribute_name, value):
        """Validates if the value is positive.

        Args:
            attribute_name (str): The attribute name to be checked.
            value (int): The integer value of the attribute to be checked.

        Raises:
            ValueError: If the value is less than 0.
        """
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")

    def validate_cordinate(self, attribute_name, value):
        """Validates if cordinate is not a negative value.

        Args:
            attribute_name (str): The attribute name to be checked.
            value (int): The integer value of the attribute to be checked.

        Raises:
            ValueError: If the value is less than 0.
        """
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")
