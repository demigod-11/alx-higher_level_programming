#!/usr/bin/python3
def element_at(my_list, idx):
    for i , j in enumerate(my_list):
        if i == idx and idx > 0:
            return i
    else:
        return None
