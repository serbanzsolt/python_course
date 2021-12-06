# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 00:50:32 2021

@author: Zsolt
"""

def even_check (number):
    result = number % 2 == 0
    return result

print( even_check(20) )
print( even_check(21) )

def check_even_list(num_list):
# RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST    
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False
        
print ( check_even_list([1,3,5]) )
print ( check_even_list([1,2,3]) )

def check_even_list2(num_list):
# RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST    
# RETURN ALL THE EVEN NUMBERS
    
    # placeholder variables
    even_numbers = []
    
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers

print ( check_even_list2([1,3,5]) )
print ( check_even_list2([1,2,3]) )

    