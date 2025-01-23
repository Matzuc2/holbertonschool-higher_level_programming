#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    result = 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        if roman_string[i] in d:
            if i > 0 and d[roman_string[i]] > d[roman_string[i - 1]]:
                result += (d[roman_string[i]] - (d[roman_string[i - 1]] * 2))
            else:
                result += d[roman_string[i]]
    return (result)
