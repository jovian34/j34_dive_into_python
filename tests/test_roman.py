__author__ = 'Carl James'

'''
commands needed to execute these tests:
pip install pytest
pip install pytest-cov
python -m pytest --assert=plain --cov-report term-missing --cov roman.py
'''
import pytest

from .. import roman

def test_to_roman_returns_XXI():
    assert roman.to_roman(21) == 'XXI'

def test_to_roman_returns_MCMXCIV():
    assert roman.to_roman(1994) == 'MCMXCIV'

def test_to_roman_returns_MMMCMXCIX():
    assert roman.to_roman(3999) == 'MMMCMXCIX'

def test_to_roman_returns_MMMDCCCLXXXVIII():
    assert roman.to_roman(3888) == 'MMMDCCCLXXXVIII'

def test_to_roman_returns_CDXLIX():
    assert roman.to_roman(449) == 'CDXLIX'

def test_to_roman_type_error_on_string():
    with pytest.raises(TypeError):
        roman.to_roman('345')

def test_to_roman_type_error_on_float():
    with pytest.raises(TypeError):
        roman.to_roman(2398.453)

def test_to_roman_value_error_negative_number():
    with pytest.raises(ValueError):
        roman.to_roman(-23)

def test_to_roman_value_error_high_number():
    with pytest.raises(ValueError):
        roman.to_roman(4000)

def test_from_roman_returns_1994():
    assert roman.from_roman('MCMXCIV') == 1994

def test_from_roman_returns_449():
    assert roman.from_roman('CDXLIX') == 449

def test_from_roman_returns_3999():
    assert roman.from_roman('MMMCMXCIX') == 3999

def test_from_roman_returns_21():
    assert roman.from_roman('XXI') == 21

def test_from_roman_returns_3888():
    assert roman.from_roman('MMMDCCCLXXXVIII') == 3888

def test_from_roman_value_error_4000():
    with pytest.raises(ValueError):
        roman.from_roman('MMMM')

def test_from_roman_value_error_bad_roman_format():
    with pytest.raises(ValueError):
        roman.from_roman('CCCCLVIII')

def test_from_roman_type_error_int():
    '''
    if not a string when roman.upper() method is applied
    AttributeError is raised, ending the program
    :return:
    '''
    with pytest.raises(AttributeError):
        roman.from_roman(3526)

def test_from_roman_valid_lowercase():
    assert roman.from_roman('mcmxcviii') == 1998

def test_from_roman_valid_mixedcase():
    assert roman.from_roman('MmxcVi') == 2096