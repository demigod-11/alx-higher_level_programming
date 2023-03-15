#!/usr/bin/python3
def weight_average(my_list=[]):
    avg= 0
    total_weight = 0
    total_score = 0
    if not my_list:
        return (0)
    for item in my_list:
        score, weight = item
        total_weight += weight
        total_score += score * weight
    return total_score / total_weight
