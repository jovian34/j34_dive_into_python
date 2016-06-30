__author__ = 'Carl James'

'''
commands needed to execute these tests:
pip install pytest
pip install pytest-cov
python -m pytest --assert=plain --cov-report term-missing --cov roman.py
'''

from .. import roman

def test_to_roman_returns_XXI():
    assert roman.to_roman(21) == 'XXI'


def test_to_roman_returns_MCMXCIV():
    assert roman.to_roman(1994) == 'MCMXCIV'


def test_to_roman_returns_MMMCMXCIX():
    assert roman.to_roman(3999) == 'MMMCMXCIX'


def test_to_roman_returns_CDXLIX():
    assert roman.to_roman(449) == 'CDXLIX'

def test_from_roman_returns_1994():
    assert roman.from_roman('MCMXCIV') == 1994

def test_from_roman_returns_449():
    assert roman.from_roman('CDXLIX') == 449

def test_from_roman_returns_3999():
    assert roman.from_roman('MMMCMXCIX') == 3999

def test_from_roman_returns_21():
    assert roman.from_roman('XXI') == 21
