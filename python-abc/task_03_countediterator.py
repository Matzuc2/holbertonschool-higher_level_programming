#!/usr/bin/python3
"""
This module defines the CountedIterator class.

The CountedIterator class wraps an iterable and keeps track
of the number of times the iterator has been accessed.
"""


class CountedIterator:
    """
    An iterator that counts the number of times it has been accessed.

    Attributes:
        __data (iterator): An iterator over the provided data.
        __count (int): The number of times the iterator has been accessed.

    Methods:
        __next__(): Advances the iterator and increments the count.
        get_count(): Returns the number of times the iterator
        has been accessed.
    """

    def __init__(self, data, count=0):
        """
        Initializes the CountedIterator with an iterable and an optional count.

        Args:
            data (iterable): The data to be iterated over.
            count (int, optional): Initial count value (default is 0).
        """
        self.__data = iter(data)
        self.__count = count

    def __next__(self):
        """
        Advances the iterator by one step and increments the access count.

        Returns:
            any: The next item from the iterable.

        Raises:
            StopIteration: If the iterator is exhausted.
        """
        next1 = next(self.__data)
        if next1 is None:
            raise StopIteration("No more items")
        else:
            self.__count += 1
            return next1

    def get_count(self):
        """
        Returns the number of times the iterator has been accessed.

        Returns:
            int: The access count.
        """
        return self.__count
