#!/usr/bin/python3
"""
    Class Student
"""


class Student:
    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        """ Special method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that returns directory description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            d_list = {}

            for idx in range(len(attrs)):
                for item in obj:
                    if attrs[idx] == item:
                        d_list[item] = obj[item]
            return d_list

        return obj

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for item in json:
            self.__dict__[item] = json[item]
