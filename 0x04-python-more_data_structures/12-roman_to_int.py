#!/usr/bin/python3
def roman_value(prmCharacter):
    roman_list = {'I':1, 'V':5, 'X':10,
            'L':50, 'C':100, 'D':500, 'M':1000}
    for key, value in roman_list.items():
        if (prmCharacter is key):
            return value
    return None


def next_value(prmString, prmIndex):
    length = len(prmString)
    if prmIndex + 1 < length:
        return roman_value(prmString[prmIndex + 1])
    else:
        return None


def roman_to_int(roman_string):
    result = 0

    if (not roman_string or not isinstance(roman_string, str)):
        return result

    for idx, char in enumerate(roman_string):
        current_value = roman_value(char)
        value = next_value(roman_string, idx)
        if value is None or current_value >= value:
            result += current_value
        else:
            result += (value - current_value)
    return result
