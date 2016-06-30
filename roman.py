__author__ = 'Carl James'

"""
mapping program to translate between integers and Roman numerals

Roman numberals only exist between 1 and 3999

from http://www.diveintopython3.net/unit-testing.html

The rules for Roman numerals lead to a number of interesting observations:

There is only one correct way to represent a particular number as a Roman numeral.
The converse is also true: if a string of characters is a valid Roman numeral,
    it represents only one number (that is, it can only be interpreted one way).
There is a limited range of numbers that can be expressed as Roman numerals,
    specifically 1 through 3999. The Romans did have several ways of expressing
    larger numbers, for instance by having a bar over a numeral to represent
    that its normal value should be multiplied by 1000. For the purposes
    of this chapter, let’s stipulate that Roman numerals go from 1 to 3999.
There is no way to represent 0 in Roman numerals.
There is no way to represent negative numbers in Roman numerals.
There is no way to represent fractions or non-integer numbers in Roman numerals.

"""

roman_map = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X',
    20: 'XX',
    30: 'XXX',
    40: 'XL',
    50: 'L',
    60: 'LX',
    70: 'LXX',
    80: 'LXXX',
    90: 'XC',
    100: 'C',
    200: 'CC',
    300: 'CCC',
    400: 'CD',
    500: 'D',
    600: 'DC',
    700: 'DCC',
    800: 'DCCC',
    900: 'CM',
    1000: 'M',
    2000: 'MM',
    3000: 'MMM'}

def to_roman(integer):
    if type(integer) != int:
        raise TypeError
    if integer < 1 or integer > 3999:
        raise ValueError
    else:
        chars = str(integer)
        chars = [ char for char in chars ]
        result = ''
        if len(chars) > 3:
            mill = int(chars[-4]) * 1000
            result = result + roman_map[mill]
        if len(chars) > 2:
            cent = int(chars[-3]) * 100
            result = result + roman_map[cent]
        if len(chars) > 1:
            tens = int(chars[-2]) * 10
            result = result + roman_map[tens]
        ones = int(chars[-1])
        return result + roman_map[ones]

def from_roman(roman):
    pass