#!/usr/bin/python

'''This module demonstrates the use of parametrized desorators. Parametrized
decorators are nested, i.e. we have outer function, which accepts arguments
and returns actual decorator.

'''

def shifting(shift):
    '''This function constructs decorator, that shift argument of a decorated
    function by shift.
    
    '''
    print "We're inside outer function and will create parametrized decorator now."

    def _inner(func):
        '''This will be actual decorator.

        '''

        print "Creating decorator..."
        def __inner(val):
            print "Function %s will be launched now. It's argument (%s) will be shifted by %s"\
                % (func.func_name, str(val), str(shift))
            return func(shift+val)
        return __inner
    return _inner

def string_func(val):
    print val

@shifting(10)
def number_func(val):
    print str(val)

if __name__ == '__main__':
    string_func("I'm string")
    #This is precisely the same as decorate first_test_func
    string_func = shifting("PREFIX   ")(string_func)
    string_func("I'm string")
    number_func(3)