#!/usr/bin/python

'''This module demonstrates the use of simple desorators. By simple
I mean non-parametrized (i.e. non-nested) functional decorators.

'''

def logging_dec(func):
    '''Logging decorator, which will print the name of a decorated
    function.

    '''
    print "Creating decorator..."
    def inner(*args, **kwargs):
        print "Function %s will be launched now..." % func.func_name
        return func(*args, **kwargs)
    return inner

def first_test_func():
    '''This function does nothing, except printing who she is.

    '''
    print "We're inside first test function."

@logging_dec
def second_test_func():
    '''This function does nothing, except printing who she is.

    '''
    print "We're inside second test function."

if __name__ == "__main__":
    first_test_func()
    #This is precisely the same as decorate first_test_func
    first_test_func = logging_dec(first_test_func)
    #Compare the behavior of first_test_func before and after previous line
    first_test_func()
    second_test_func()