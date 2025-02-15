#!/usr/bin/python3
import pickle

"""
This module defines a class `CustomObject` that represents an object
with attributes such as `name`, `age`, and `is_student`. It includes
methods for serializing the object to a file and deserializing it back
from a file using the `pickle` module.
"""


class CustomObject:
    """
    A class to represent a custom object with attributes such as
    name, age, and is_student, and provides methods for serialization
    and deserialization of the object.

    Attributes:
        name (str): The name of the person or object.
        age (int): The age of the person or object.
        is_student (bool): A flag indicating if the person is a student.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance with the given attributes.

        Args:
            name (str): The name of the person or object.
            age (int): The age of the person or object.
            is_student (bool): A flag indicating if the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the attributes of the CustomObject instance.

        This method is used to display the object's name, age, and whether
        the object is a student.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the CustomObject instance and saves it to a file.

        Args:
            filename (str): The name of the file where the
            serialized object will be saved.
        """
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes a CustomObject from a file and returns the instance.

        Args:
            filename (str): The name of the file from which the object
              will be loaded.

        Returns:
            CustomObject: A CustomObject instance loaded from the file.
        """
        with open(filename, "rb") as file:
            loaded_data = pickle.load(file)
        return loaded_data
