# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 02:28:57 2021

@author: Zsolt
"""

# =============================================================================
# *args and **kwargs - Arguments and KeyWord Arguments
# =============================================================================

# *args
def myfunc (a,b):
    # returns 5% of the sum of a and b
    return sum((a,b)) * 0.05

print(myfunc(40, 60))

# args is just a tuple    
def myfunc2 (*args):
    return sum(args)

print(myfunc2(10,2123,1,212,12,34))
print(myfunc2(20,3,50))

# **kwargs is just a dictionary

def myfunc3(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('MY fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
        
myfunc3(fruit='apple', veggie='lettuce')

# combine these

def myfunc4 (*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))
    
myfunc4(10,20,30,fruit='orange',food='eggs',animal='dog')