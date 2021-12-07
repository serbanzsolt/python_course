# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:06:13 2021

@author: Zsolt
"""

# =============================================================================
# MAP
# =============================================================================

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

map(square, my_nums)
for items in map(square, my_nums):
    print(items)
    
def splicer (mystring):
    
    if len(mystring) % 2 ==0:
        return 'EVEN'
    else:
        return mystring[0]
    
names = ['Andy', 'James', 'Sally']

print(list(map(splicer, names)))

# =============================================================================
# FILTER
# =============================================================================

def check_even (num):
    return num%2==0

mynums = [1,2,3,4,5,6]

print(list(filter(check_even, mynums)))


for n in filter(check_even, mynums):
    print(n)
    
# =============================================================================
# LAMBDA
# =============================================================================

def square(num):
    result = num**2
    return result

# def square(num):return num**2
lambda num: num**2

square = lambda num: num**2
