__author__ = 'Carl James'

from .. import pythagorean_triplet as pythag_trip

def test_all_factors():
    test_input = 30
    result = pythag_trip.all_factors(test_input)
    assert result == (2, 3, 5)

