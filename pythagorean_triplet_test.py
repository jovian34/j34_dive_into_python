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
import square_root

def create_possible_triplets(min, max):
    '''

    :return: list of lists
    '''

    possible_triplets = []
    for i in range(min, max -1):
        for j in range(min +1, max):
            if j > i:
                for k in range(min +2, max +1):
                    if k > j and i:
                        triplet = (i,j,k)
                        possible_triplets.append(triplet)
    return possible_triplets

def create_possible_triplets_comp(min, max):
    possible_triplets_comp = [ (i,j,k) for k in range(min + 2,max +1)
                               for j in range(min + 1, max)
                               for i in range(min, max - 1)
                               if j > i if k > j and i]
    return possible_triplets_comp


def triplets_in_range(min, max):
    '''
    :param min: integer
    :param max: integer
    :return: list of lists

    '''

def primative_triplets(b):
    pass

if __name__ == '__main__':
    a = create_possible_triplets(1, 10)
    b = create_possible_triplets_comp(1, 10)
    result = True
    for i in range(len(a)):
        if a[i] not in b:
            result = False
            print(a[i], ' and ', b[i])
        elif a[i] not in b:
            result = False
            print(a[i], ' and ', b[i])
        elif a[i] not in b:
            result = False
            print(a[i], ' and ', b[i])
    if len(a) == len(b):
        print('They are the same length')
    if result == True:
        print('They are the same')
    else:
        print('They are not the same')
    #print(a)
    #print(b)
