# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:15:45 2021

@author: bfkhuser
"""

# =============================================================================
# TUPLES: Very similar to Lists but they are IMMUTABLE
# =============================================================================

t = (1,2,3)
my_list = [1,2,3]

print(type(t))
print(type(my_list))
print(len(t))

t = ('one' ,2)
print(t[0])
print(t[-1])

t = ('a', 'a', 'b')

print(t.count('a'))
print(t.index('a'))

mylist = [1,2,3]
mylist[0] = 'NEW'
print(mylist)

# Tuples are not mutable
t[0] = 'new'