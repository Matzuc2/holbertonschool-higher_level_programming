#!/usr/bin/python3
"""
This module defines the `Student` class.
The class provides functionality to store student information,
retrieve it as a dictionary, and update attributes from a JSON object.
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

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
          based on a JSON dictionary.

        Args:
            json (dict): A dictionary where keys are attribute
            names and values
            are the new values for those attributes.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)


""" On parcourt le dictionnaire json et si ce dernier
possède un même nom d'attribut que celui dans le dictionnaire de
base, on échange la valeur de l'attribut de l'objet par celui
de l'attribut du dictionnaire json. C'est ce à quoi sert setattr.
avant on effectue une vérification et on compare chaque attribut
du dict json à ceux de l'objet avec hasattr,
si le même nom d'attribut est trouvé,
on échange la valeur de l'attribut de l'objet avec celui du dict
json de par setattr   """

"""Je m'efforce d'écrire cela ici car cet tâche
a été réussie par l'IA malgré moi, je n'ai pas réussi à
trouver la réponse seul.. Cependant je suis bien
content d'avoir découvert ces méthodes, donc sans regret."""
