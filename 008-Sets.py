# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:06:19 2021

@author: bfkhuser
"""

# =============================================================================
# Sets UNORDERED collection of unique elements
# =============================================================================

myset = set()
print (myset)

myset.add(1)
print (myset)

myset.add(2)
print (myset)
# Adding 2 again
myset.add(2)
print (myset)

# Casting set on a list

my_list = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,3]
my_set = set(my_list)

print (my_set)

my_list2 = [4,4,4,1,1,1,1,1,2,2,2,2,3,3,3,3,3,3]
my_set2 = set(my_list2)

print (my_set2)