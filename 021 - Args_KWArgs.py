# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 02:28:57 2021

@author: Zsolt
"""

# =============================================================================
# *args and **kwargs - Arguments and KeyWord Arguments
# =============================================================================

def myfunc (a,b):
    # returns 5% of the sum of a and b
    return sum((a,b)) * 0.05

print(myfunc(40, 60))

# args is just a tuple    
def myfunc2 (*args):
    return sum(args)

print(myfunc2(10,2123,1,212,12,34))
print(myfunc2(20,3,50))
