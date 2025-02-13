#!/usr/bin/python3
"""
This module defines the `Student` class.
The class provides functionality to store student information
and retrieve it as a dictionary representation.
"""


class Student:
    """
    Represents a student with a first name, last name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        If `attrs` is a list of strings, only the attributes
          with names in this list
        will be included in the returned dictionary.
        If `attrs` is not a list of strings, all attributes are returned.

        Args:
            attrs (list, optional): A list of attribute names
            (strings) to include
            in the returned dictionary. Defaults to None.

        Returns:
            dict: A dictionary containing the requested
              attributes of the student.
            If `attrs` is not a valid list of strings,
            all attributes are returned.
        """
        if isinstance(attrs, list) and\
           all(isinstance(attr, str) for attr in attrs):
            return\
               {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        else:
            return self.__dict__
