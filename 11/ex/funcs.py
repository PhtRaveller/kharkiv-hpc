#!/usr/bin/python

'''This module contains simple functions for number list processing.'''

def square(numbers):
    '''This function constructs a list with elements from ``number`` squared.

    In case ``numbers`` is not iterable or any elements of ``numbers`` cannot be treated
    as numbers, it returns ``None``. Non-numeric types are not casted. Types of elements
    in resulted list are the same, as in initial one. In case of overflow corresponding
    elements are ``inf`` as they should be.
    
    Examples:
    >>> square([1,2,3])
    [1, 4, 9]
    >>> square(4)
    None
    >>> square([5,1,'e'])
    None
    >>> square([1,0.9e+308])
    [1, inf]

    Note, that ``doctest`` doesn't capture stderr, only stdout.
    '''
    try:
        return [x*x for x in numbers]
    except TypeError as err:
        import sys
        print sys.stderr.write('{0} is either non-iterable, or contains non-numeric elements.\n'.format(numbers))
        return None

def cumulative_sum(numbers, part=None):
    '''This function constructs cumulative sum of a list. ``part`` argument tells
    how many items to gather, i.e. result is ``sum from 0 to part-1 of numbers``.

    Works the same as ``square`` for non-numeric elements or non-iterable ``numbers``.
    If part is invalid (either <0, >len(numbers)-1, or non-numeric) should return None,
    even though we can actually use such indices in slicing.

    Examples:
    >>> cumulative_sum([1,2,3])
    6
    >>> cumulative_sum([1,2,3], 2)
    3
    >>> cumulative_sum(1)
    None
    >>> cumulative_sum(['w'], 2)
    None
    >>> cumulative_sum([1,2,3], 8)
    None
    >>> cumulative_sum([1,2,3], -4)
    None
    >>> cumulative_sum([1,2,3], 'anystring')
    None
    >>> cumulative_sum([0.9e+308,0.9e+308])
    inf'''
    #This code fails most of the doctests
    #We'll fix this during the lecture
    if part is not None:
        return sum(numbers[:part])
    else:
        return sum(numbers)

def find_max(numbers, part=None):
    if part is not None:
        return max(numbers[:part])
    else:
        return max(numbers)

if __name__ == '__main__':
    import doctest
    doctest.testmod()