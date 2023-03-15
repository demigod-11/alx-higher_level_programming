#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_to_int_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                         'C': 100, 'D': 500, 'M': 1000}
    prev_value = 0
    total_value = 0

    for c in roman_string:
        curr_value = roman_to_int_dict.get(c, 0)

        if curr_value == 0:
            return 0  # Invalid Roman numeral

        if curr_value > prev_value:
            total_value += curr_value - 2 * prev_value
        else:
            total_value += curr_value

        prev_value = curr_value

    return total_value
