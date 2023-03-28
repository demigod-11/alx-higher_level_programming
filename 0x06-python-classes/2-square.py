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

    def __init__(self, size=0):
        """
            class instantiation
            Args:
                 size : class attribute (private)
            Return: None
        """
        self.__size:int = size

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
