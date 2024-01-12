#!/usr/bin/python3
roman_numerical = {
    "IV": 4,
    "IX": 9,
    "I": 1,
    "V": 5,
    "X": 10,
    "XL": 40,
    "XC": 90,
    "L": 50,
    "C": 100,
    "CD": 400,
    "CM": 900,
    "D": 500,
    "M": 1000,
}


def roman_to_int(roman_string):
    sum = 0
    if roman_string is not None and isinstance(roman_string, str):
        for key in ["CD", "CM", "XL", "XC", "IV", "IX",
                    "I", "V", "X", "L", "C", "D", "M"]:
            sum += roman_string.count(key)*roman_numerical[key]
            roman_string = roman_string.replace(key, " ")
    return sum
