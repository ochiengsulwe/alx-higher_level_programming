#!/usr/bin/python3
""" The base class which defines the other classes in this project

    The goal of it is to manage the `id` in all the future classes
    and to prevent duplication of some code and by estension, some bugs.
"""


class Base(object):
    """The base class managing the `id` attribute in the project

    Attributes:
        __nb_objects (int): Private class attribute use to track `id`.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """The class is instatited with one optional public attribute `id`.

        Args:
            id (:obj: `int`, optional): A public attribute to be tracked.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
