#!/usr/bin/python

"""This module demonstrates how to use decorator to measure
function running time. As a side effect, you can compare performance
of different approaches to contructing a list from another list.

Follow decorator pattern carefully to better understand the hierarchy
of returned decorators.

"""

RUNS = 1000
LIST_SIZE = 10000

def timing(runs):
    """Returns wrapper function, which performs multiple runs
    and measures average time elapsed per run. Returned function is used as decorator.

    """
    def _timing(func):
        def __timing(*args, **kwargs):
            import time
            stime = time.clock()
            for i in xrange(runs):
                res = func(*args, **kwargs)
            etime = time.clock() - stime
            print "%fs elapsed." % (etime/runs)
            return res
        return __timing
    return _timing

@timing(RUNS)
def list_loop(*args, **kwargs):
    """Loops over args[0], multiplies each element by two and append
    to resulting list.

    """
    result = []
    for i in args[0]:
        result.append(2*i)
    return result

@timing(RUNS)
def list_map(*args, **kwargs):
    """Applies lambda function, which doubles its argument, to args[0].

    """
    return map(lambda x: x*2, args[0])

@timing(RUNS)
def list_comprehension(*args, **kwargs):
    """Contructs resulting list with doubled elements from args[0] via
    list comprehension.

    """
    return [2*x for x in args[0]]

def double_generator(somelist):
    for i in somelist:
        yield i*2

@timing(RUNS)
def list_generator(*args, **kwargs):
    """Contructs resulting list with doubled elements from args[0] via
    generator function double_generator.

    """
    return list(double_generator(args[0]))

@timing(RUNS)
def list_filter_straight(*args, **kwargs):
    """Filters initial list (args[0]) according to element < args[1]
    using loop.

    """
    result = []
    for i in args[0]:
        if i<args[1]:
            result.append(i)
    return result

@timing(RUNS)
def list_filter_functional(*args, **kwargs):
    """Filters initial list (args[0]) according to element < args[1]
    using built-in filter function.

    """
    return filter(lambda x: x<args[1], args[0])

@timing(RUNS)
def list_filter_comprehension(*args, **kwargs):
    """Filters initial list (args[0]) according to element < args[1]
    using extended syntax of list comprehensions.

    """
    return [x for x in args[0] if x<args[1]]

if __name__ == "__main__":
    testlist = range(LIST_SIZE)
    print "Profiling for-loop:"
    res = list_loop(testlist)
    print "Profiling map on list:"
    res = list_map(testlist)
    print "Profiling list comprehension:"
    res = list_comprehension(testlist)
    print "Profiling generator:"
    res = list_generator(testlist)
    print "Profiling filtering with for-loop:"
    res = list_filter_straight(testlist, 10)
    print "Profiling filtering with built-in filter function:"
    res = list_filter_functional(testlist, 10)
    print "Profiling filtering with list-comprehension:"
    res = list_filter_comprehension(testlist, 10)