#!/usr/bin/python3
"""
This module defines the VerboseList class, which extends
Python's built-in list.

The VerboseList class overrides list methods such as append, extend, remove,
and pop to provide additional console output, describing the performed actions.
"""


class VerboseList(list):
    """
    A subclass of list that provides verbose output for list operations.

    Methods:
        append(object): Adds an item to the list and prints a message.
        extend(iterable): Extends the list with an iterable and prints
        a message.
        remove(value): Removes an item from the list and prints
        a message.
        pop(index): Removes and returns an item at the given
        index with a message.
    """

    def append(self, object):
        """
        Adds an item to the end of the list and prints a message.

        Args:
            object (any): The item to add to the list.
        """
        super().append(object)
        print("Added [{}] to the list".format(object))

    def extend(self, iterable):
        """
        Extends the list by appending elements from the iterable
        and prints a message.

        Args:
            iterable (iterable): An iterable containing
            items to add to the list.
        """
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, value):
        """
        Removes the first occurrence of the specified value
        and prints a message.

        Args:
            value (any): The item to remove from the list.

        Raises:
            ValueError: If the value is not found in the list.
        """
        super().remove(value)
        print("Removed [{}] from the list.".format(value))

    def pop(self, index=-1):
        """
        Removes and returns the item at the given index and prints a message.

        Args:
            index (int, optional): The index of the item to
            remove. Defaults to -1 (last item).

        Returns:
            any: The removed item.

        Raises:
            IndexError: If the list is empty or the index is out of range.
        """
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
