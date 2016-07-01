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

Below is Carl James' solutions before looking up how the author solved this problem.

"""

import re

roman_map = {
    0: '',
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

#verbose pattern from http://www.diveintopython3.net/regular-expressions.html#romannumerals
pattern = '''
    ^                   # beginning of string
    (M{0,3})            # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    '''

def to_roman(integer):
    '''

    :param integer: an integer between 1 and 3999
    :return: a string
    '''
    if type(integer) != int:
        raise TypeError('Argument must be a whole number.')
    if integer < 1 or integer > 3999:
        raise ValueError('Number must be between 1 and 3999.')
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
    '''

    :param roman: a string formatted as a Roman numeral
    :return: an integer
    '''
    roman = roman.upper()
    process_regex = re.compile(pattern, re.VERBOSE)
    parts = process_regex.match(roman)
    if parts == None:
        raise ValueError('Not a valid Roman Numeral.')
    integer_map = { value: key for key, value in roman_map.items() }
    result = integer_map[parts.group(1)]
    result = result + integer_map[parts.group(2)]
    result = result + integer_map[parts.group(3)]
    result = result + integer_map[parts.group(4)]
    return result