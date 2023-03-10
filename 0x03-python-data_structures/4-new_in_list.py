#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    for i, j in enumerate(my_list):
        if i == idx and i > 0:
            new_list.append(element)
        new_list.append(j)
    return new_list
