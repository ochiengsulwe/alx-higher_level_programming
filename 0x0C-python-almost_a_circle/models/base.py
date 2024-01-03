#!/usr/bin/python3
""" The base class which defines the other classes in this project

    The goal of it is to manage the `id` in all the future classes
    and to prevent duplication of some code and by estension, some bugs.
"""
import json


class Base(object):
    """The base class managing the `id` attribute in the project

    Attributes:
        __nb_objects (int): Private class attribute use to track `id`.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """The class is instatited with one optional public attribute `id`.

        Args:
            id (:obj:`int`, optional): A public attribute to be tracked.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Describess the JSON string representation of `list_dictionaries`.

        Args:
            list_dictionaries (:obj:`list` of :obj:`dict`):
                A list of instance attributes.

        Returns:
            str: JSON representation of `list_dictionaries`.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of `list_objs` to a file.

        Args:
            list_objs (list): A list of class instances who inherits of `Base`.

        Returns:
            None.
        """
        if list_objs is None:
            list_objs = []
        json_file = f"{cls.__name__}.json"
        json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
            )

        with open(json_file, "w") as jfile:
            jfile.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string.
        """
        if not json_string:
            return []
        return json.loads(json_string)
