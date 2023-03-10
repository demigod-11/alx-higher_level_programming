#!/bin/usr/python3
def print_reversed_list_integer(my_list=[]):
    num = len(my_list)
    for i in range(num):
        print("{}".format(my_list[num - 1 - i]))
