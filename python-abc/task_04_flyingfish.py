#!/usr/bin/python3
"""
This module defines classes representing different animals: Fish, Bird,
and FlyingFish, demonstrating multiple inheritance.
"""


class Fish:
    """
    A class representing a fish.

    Methods:
        swim(): Prints a message indicating the fish is swimming.
        habitat(): Prints a message about the fish's habitat.
    """

    def swim(self):
        """
        Prints a message indicating that the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints a message indicating that the fish lives in water.
        """
        print("The fish lives in water")


class Bird:
    """
    A class representing a bird.

    Methods:
        fly(): Prints a message indicating the bird is flying.
        habitat(): Prints a message about the bird's habitat.
    """

    def fly(self):
        """
        Prints a message indicating that the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints a message indicating that the bird lives in the sky.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish, inheriting from both Fish and Bird.

    Methods:
        swim(): Prints a message indicating the flying fish is swimming.
        fly(): Prints a message indicating the flying fish is soaring.
        habitat(): Prints a message about the flying fish's unique habitat.
    """

    def fly(self):
        """
        Prints a message indicating that the flying fish is soaring.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Prints a message indicating that the flying fish is swimming.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Prints a message indicating that the flying fish lives
        both in water and in the sky.
        """
        print("The flying fish lives both in water and the sky!")
