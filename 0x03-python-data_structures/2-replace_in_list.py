#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i , j in enumerate(my_list):
        if i == idx and i > 0:
            my_list[i] = element
            return my_list
    else:
        return my_list
