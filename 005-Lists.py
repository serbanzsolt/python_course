# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 11:32:32 2021

@author: Zsolt
"""

my_list = [1,2,3]
my_list2 = ['STRING', 100, 32.2]

print(len(my_list2))

my_list3 = ["one", "two", "three"]
# indexing
print(my_list3[0])
my_list4 = ["four", "five"]

concatenated_list = my_list3 + my_list4
print(concatenated_list)
# slicing
print(concatenated_list[1:])

# lists are mutable

concatenated_list[0] = "ONE ALL CAPS"

print(concatenated_list)

# =============================================================================
# APPEND - adding new item to the list
# =============================================================================

concatenated_list.append("six")
print(concatenated_list)

# =============================================================================
# POP - popping item from the list
# =============================================================================

popped_item = concatenated_list.pop()
print(popped_item)
# the list lost the popped item
print(concatenated_list)
concatenated_list.pop(2)
print(concatenated_list)

# =============================================================================
# Sort / Reverse
# =============================================================================

new_list = ["a", "e", "z", "b", "x"]
number_list = [7,1,4,2,3]

print(new_list)
new_list.sort()
print(new_list)

# common error
my_sorted_list = new_list.sort()
print(my_sorted_list)
print(type(my_sorted_list))

print(number_list)
number_list.sort()
print(number_list)
number_list.reverse()
print(number_list)