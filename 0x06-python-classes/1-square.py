#!/usr/bin/python3
"""
    Defines a Class Square
"""


class Square:
    """
        Represents a square
        Attributes:
            __size (int): size of a side of the square
    """

    def __init__(self, size):
        """
            class instantiation
            Args:
                 size : class attribute (private)
            Return: None
        """
        self.__size = size

