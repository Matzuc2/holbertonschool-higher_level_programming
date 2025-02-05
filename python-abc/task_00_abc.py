#!/usr/bin/python3
"""
This module defines an abstract Animal class and its subclasses Dog and Cat.

The Animal class provides a blueprint for defining animals with a sound method
that must be implemented by subclasses.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.

    Methods:
        sound(): Abstract method that must be implemented by subclasses to
        define the sound the animal makes.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to define the sound an animal makes.

        This method must be implemented by subclasses.

        Returns:
            str: A string representing the animal's sound.
        """
        pass


class Dog(Animal):
    """
    Represents a Dog, a subclass of Animal.

    Methods:
        sound(): Returns the sound a dog makes.
    """

    def sound(self):
        """
        Returns the sound a dog makes.

        Returns:
            str: The string "Bark".
        """
        return "Bark"


class Cat(Animal):
    """
    Represents a Cat, a subclass of Animal.

    Methods:
        sound(): Returns the sound a cat makes.
    """

    def sound(self):
        """
        Returns the sound a cat makes.

        Returns:
            str: The string "Meow".
        """
        return "Meow"
