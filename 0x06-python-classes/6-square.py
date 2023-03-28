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

    def __init__(self, size: int = 0, position: tuple = (0, 0)):
        """
            class instantiation
            Args:
                 size : class attribute (private)
            Return: None
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
            __position getter
            Args:
                None
            Return: tuple
        """
        return self.__positon

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) is 2 and \
            type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
            Square Area
            Args:
                None
            Return: int
        """
        return self.__size ** 2

    def my_print(self):
        """
            Prints the square with the # character on stdout
        """
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
