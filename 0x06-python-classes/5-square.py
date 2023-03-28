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
        self.size = size

    def area(self):
        """
            Square Area
            Args:
                None
            Return: int
        """
        return self.__size ** 2

    @property
    def size(self):
        """
            __size getter
            Args:
                None
            Return: int
        """
        return self.__size

    @size.setter
    def size(self, value: int):
        """
            __size setter
            Args:
                Value (int)
            Return: None
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size: int = value

    def my_print(self):
        """
            prints # amount of area
            Args:
                None
            Return: Str
        """
        if self.__size == 0:
            print()
            return
        else:
            print("#" * self.__size)
