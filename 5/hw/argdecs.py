#!/usr/bin/python

'''This is actual homework. You need to write a decorator, which checks
argument's type and either return None if function is called with
incorrect argument, or return result of a function itself.

'''

def guard_type(guarded_type):
    '''This function constructs decorator, that checks argument's
    type before calling decorated function. If type of arguments
    is guarded_type, then function is called and their result is returned.
    Else None is returned.
    
    '''
    def _inner(func):
        def __inner(val):
            #TODO: check type here
            #isinstance(obj, neededtype) allows to check whether obj's
            #type is neededtype

            #Say, you can do isinstance([1,2,3], list), which is True

            #if isinstance(val, guarded_type):
            #    return func(val)
            #else:
            #    print "Function %s doesn't accept argument of type %s"\
            #        % (func.func_name, type(val))
            return None
        return __inner
    return _inner

@guard_type(list)
def list_func(val):
    '''Capitalizes each element of val and concatenets them with scape.

    '''
    return " ".join([str(x).upper() for x in val])

@guard_type(float)
def float_func(val):
    '''Raises val to the third power.

    '''
    return val**3

if __name__ == '__main__':
    print list_func(['some', 'string', 'here']) or "We've got None!"
    print list_func(3.4) or "We've got None!"
    print float_func(3.4) or "We've got None!"
    print float_func(['some', 'string', 'here']) or "We've got None!"    