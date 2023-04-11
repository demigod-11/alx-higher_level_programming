#!/usr/bin/python3
"""
    Class BaseGeometry
"""


class BaseGeometry:
    """
        A class with public attribute area
    """
    def area(self):
        """
            raises an exception if not implemented
        """
        raise Exception("area() is not implemented")
