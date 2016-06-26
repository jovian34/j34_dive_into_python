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
    possible_triplets = create_possible_triplets(min, max)
    triplets = [ trip for trip in possible_triplets
                 if trip[0] ** 2 + trip[1] ** 2 == trip[2] ** 2 ]
    return triplets

def primative_triplets(b):
    pass

def get_inputs():
    try:
        min = input('What is the minimum number? ')
        min = int(min)
        max = input(' What is the maximum number? ')
        max = int(max)
    except TypeError:
        print('You must enter a positive whole number.')
        get_inputs()
    if min < 1:
        raise ValueError
        print('Minimum must be a whole number of at least 1.')
        get_inputs()
    if max <= min + 1:
        raise ValueError
        print('Maximum must be at least 2 greater than the minimum.')
        get_inputs()
    return (min, max)

def main():
    min, max = get_inputs()
    print(triplets_in_range(min, max))

if __name__ == '__main__':
    main()