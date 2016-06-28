__author__ = 'Carl James'

'''
python -m pytest --assert=plain --cov-report term-missing --cov pythagorean_triplet.py
'''

from .. import pythagorean_triplet

def test_all_factors_with_many_factors():
    test_input = 30
    result = pythagorean_triplet.all_factors(test_input)
    assert result == [2, 3, 5, 6, 10, 15]

def test_all_factors_on_a_prime():
    test_input = 7
    result = pythagorean_triplet.all_factors(test_input)
    assert result == []

def test_validating_proper_inputs():
    min, max, b = ('2','9','16')
    result = pythagorean_triplet.validate_inputs(min,max,b)
    assert result == (2,9,16)

