#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    length = len(roman_string) - 1
    for i in range(0, len(roman_string)):
        if roman_string[i] not in vals:
            return 0
        elif i < length and vals[roman_string[i]] < vals[roman_string[i + 1]]:
            sum += vals[roman_string[i + 1]] - vals[roman_string[i]]
            i += 1
        else:
            sum += vals[roman_string[i]]
    return sum
