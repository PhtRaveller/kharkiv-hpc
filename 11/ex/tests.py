#!/usr/bin/python

import funcs

def test_square():
    '''Tests ``square`` function from ``funcs`` module.'''
    assert funcs.square([1,2,3])==[1,4,9]
    assert funcs.square([1,2,'1'])==None
    assert funcs.square(1)==None
    assert funcs.square([1,2,0.9e+308])==[1,4,float('inf')]

def test_cumulative():
    '''Tests ``cumulative_sum`` function from ``funcs`` module.'''
    assert funcs.cumulative_sum([1,2,3])==6
    assert funcs.cumulative_sum([1,2,3], 2)==3
    assert funcs.cumulative_sum(1)==None
    assert funcs.cumulative_sum(['w'], 2)==None
    assert funcs.cumulative_sum([1,2,3], 8)==None
    assert funcs.cumulative_sum([1,2,3], -4)==None
    assert funcs.cumulative_sum([1,2,3], 'anystring')==None
    assert funcs.cumulative_sum([0.9e+308,0.9e+308])==float('inf')

#Test for find_max function is for HW.    