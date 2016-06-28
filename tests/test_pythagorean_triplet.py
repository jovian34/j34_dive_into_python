__author__ = 'Carl James'

'''
commands needed to execute these tests:
pip install pytest
pip install pytest-cov
python -m pytest --assert=plain --cov-report term-missing --cov pythagorean_triplet.py
'''

from .. import pythagorean_triplet

def test_create_triplets_yields_triplets_start():
    trip_gen = pythagorean_triplet.create_possible_triplets(2,10)
    result = next(trip_gen)
    assert result == (2,3,4)

def test_create_triplets_yields_triplets_end():
    trip_gen = pythagorean_triplet.create_possible_triplets(2,103)
    result = []
    for trip in trip_gen:
        result.append(trip)
    assert result[-1] == (101,102,103)

def test_create_triplets_yields_more_than_range():
    trip_gen = pythagorean_triplet.create_possible_triplets(2, 103)
    result = []
    for trip in trip_gen:
        result.append(trip)
    assert len(result) > 100

def test_triplet_filtered_out():
    trip_gen = pythagorean_triplet.triplets_in_range(2, 103)
    result = []
    for trip in trip_gen:
        result.append(trip)
    assert (3,4,6) not in result

def test_triplet_filtered_in():
    trip_gen = pythagorean_triplet.triplets_in_range(2, 103)
    result = []
    for trip in trip_gen:
        result.append(trip)
    assert (3,4,5) in result

def test_is_primative_triplet_true():
    triplet = (3,4,5)
    assert pythagorean_triplet.is_primative_triplet(triplet)

def test_is_primative_triplet_false():
    triplet = (6,8,10)
    assert not pythagorean_triplet.is_primative_triplet(triplet)



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

