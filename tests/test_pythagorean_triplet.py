__author__ = 'Carl James'

'''
commands needed to execute these tests:
pip install pytest
pip install pytest-cov
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
    min, max, b = (2,9,16)
    result = pythagorean_triplet.validate_inputs(min,max,b)
    assert result == (True,2,9,16)

def test_validate_negative_min_input_false():
    min,max,b = (-3,4,32)
    result = pythagorean_triplet.validate_inputs(min,max,b)
    assert result[0] == False

def test_validate_lower_max_input_false():
    min,max,b = (23,22,32)
    result = pythagorean_triplet.validate_inputs(min,max,b)
    assert result[0] == False

def test_validate_b_not_divisible_by_four_is_false():
    min,max,b = (2, 13, 29)
    result = pythagorean_triplet.validate_inputs(min,max,b)
    assert result[0] == False

