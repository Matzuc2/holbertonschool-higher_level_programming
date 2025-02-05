#!/usr/bin/python3
"""
This module defines mixin classes for swimming and flying abilities,
as well as a Dragon class that inherits both.
"""


class SwimMixin:
    """
    A mixin class that provides swimming capability.

    Methods:
        swim(): Prints a message indicating that the creature swims.
    """

    def swim(self):
        """
        Prints a message indicating that the creature is swimming.
        """
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class that provides flying capability.

    Methods:
        fly(): Prints a message indicating that the creature flies.
    """

    def fly(self):
        """
        Prints a message indicating that the creature is flying.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a dragon, capable of both swimming and flying.

    Methods:
        roar(): Prints a message indicating that the dragon roars.
    """

    def roar(self):
        """
        Prints a message indicating that the dragon is roaring.
        """
        print("The dragon roars!")
