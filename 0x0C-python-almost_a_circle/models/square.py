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
                f"[{self.__class__.__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.size}"
            )

    def update(self, *args, **kwargs):
        """Dynamically sets instance attributes.

        Args:
            *args (int): Accepts varible number or arguments as ordered:
                1. id: the class attribute.
                2. size: the size of the square.
                3. x: x-axis represenation on the plane.
                4. y: y-axis represantation on a plane.
            **kwargs (int): key word arguments of a variable number.
                 Each should represent the instance attribute.
            """
        if args:
            attributes = ["id", "size", "x", "y"]
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif kwargs:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """Returns a dictionary of class `Square`.

        The Key of the dictionary is the attribute name,
            while the value is the assigned value of the attribute.
        """
        class_name_prefix = "_Rectangle__"
        dict_rep = {
                key.replace(class_name_prefix, ''): value
                for key, value in self.__dict__.items()
                if key.startswith(class_name_prefix)
                and key != "_Rectangle__height" and key != "_Rectangle__width"
            }
        dict_rep['id'] = self.id
        dict_rep['size'] = self.size
        return dict_rep
