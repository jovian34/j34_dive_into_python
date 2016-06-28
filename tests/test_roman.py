__author__ = 'Carl James'

'''
commands needed to execute these tests:
pip install pytest
pip install pytest-cov
python -m pytest --assert=plain --cov-report term-missing --cov roman.py
'''

from .. import roman

def test_to_roman_returns_integer():
    assert roman.to_roman(21) == 'XXI'