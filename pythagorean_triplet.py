'''

from STDIG Python Meeting 2 on YouTube
https://youtu.be/LN-kUWW_9wM

The test case below assumes that two functions are defined

triplets_in_range(min, max)
    compute all pythagorean triplets (a, b, c) with min <= a, b, c => max

primative_triples(b)
    Find all primitive pythagorean triplets having b as one of their components

    Args:
        b - an integer divisible by 4 (see explanation below)

Note that in the latter function the components other than the arguement can
be quite large

a ** 2 + b ** 2 = c ** 2

A primative pythagorean triplet has its three components coprime. So (3,4,5) is
a primative pythagorean triplet since 3,4, and 5 don't have a common factor.
On the other hand, (6, 8, 10), although a pythagorean triplet, is not primative
since 2 divides all three components.

'''

def create_possible_triplets(min, max):
    '''

    :param min: integer
    :param max: integer at least 2 greater than min
    :return: a list of tuples each with 3 integers in ascending value
    '''

    possible_triplets = [ (i,j,k) for k in range(min + 2,max +1)
                               for j in range(min + 1, max)
                               for i in range(min, max - 1)
                               if j > i if k > j and i]
    return possible_triplets


def triplets_in_range(min, max):
    '''

    :param min: integer
    :param max: integer at least 2 greater than min
    :return: a list of tuples each with 3 integers in ascending value
        these tuples are all pythagorean triplets
    '''

    possible_triplets = create_possible_triplets(min, max)
    triplets = [ trip for trip in possible_triplets
                 if trip[0] ** 2 + trip[1] ** 2 == trip[2] ** 2 ]
    return triplets

def all_factors(x):
    '''

    :param x: integer
    :return: list of all possible factors
    '''

    return [factor for factor in range(2, int(x / 2) + 1) if x % factor == 0]

def is_primative_triplet(triplet):
    '''

    :param triplet: tuple of ascending integers that is a pythagorean triplet
    :return: Boolean
    '''

    result = True
    factors = [ all_factors(triplet[i]) for i in range(3)]
    for factor in factors[0]:
        if factor in factors[1] and factors[2]:
            result = False
    return result

def my_primative_triplets(triplets):
    '''

    :param triplets: a list of tuples each with 3 integers in ascending value
        these tuples are all pythagorean triplets
    :return: a list of tuples each with 3 integers in ascending value
        these tuples are all primative pythagorean triplets
    '''

    return [ trip for trip in triplets if is_primative_triplet(trip)]

def primative_triplets(triplets, b):
    '''

    :param triplets: a list of tuples each with 3 integers in ascending value
        these tuples are all pythagorean triplets
    :param b: an integer divisible by 4
    :return: list of tuples
    '''
    return [trip for trip in triplets if b in trip]


def get_min_input():
    return input('What is the minimum number? ')

def get_max_input():
    return input('What is the maximum number? ')

def get_b():
    return input('Please enter a whole number divisible by 4: ')



def validate_inputs(min, max, b):
    '''

    :param min: string of a number
    :param max: string of a number
    :param b: string of a number
    :return: tuple of integers
    '''
    try:
        min = int(min)
    except ValueError:
        print('You must enter a positive whole number.')
        main()

    if min < 1:
        print("Minimum must be a whole number of at least 1.")
        main()

    try:
        max = int(max)
    except ValueError:
        print('You must enter a positive whole number.')
        main()

    if max <= min + 1:
        print('Maximum must be at least 2 greater than the minimum.')
        main()

    try:
        b = int(b)
    except ValueError:
        print('You must enter a positive whole number.')
        main()

    if b % 4 != 0:
        print('The third input must be divisible by 4 (example: 16).')
        main()
    return (min, max, b)

def main():
    '''

    :return: None

    This is the main program
    '''
    min, max, b = get_min_input(), get_max_input(), get_b()
    min, max, b = validate_inputs(min, max, b)
    triplets = triplets_in_range(min, max)
    prim_triplets = primative_triplets(triplets, b)
    my_prim_triplets = my_primative_triplets(triplets)
    print(triplets)
    print('***********************')
    print(prim_triplets)
    print('***********************')
    print(my_prim_triplets)

if __name__ == '__main__':
    main()