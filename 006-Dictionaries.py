# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 14:20:11 2021

@author: Zsolt
"""

# =============================================================================
# Dictionaries {'key1':'value1', 'key2':'value2' } KEY - VALUE PAIRS
# Unordered
# =============================================================================

my_dict = {'key1':'value1', 'key2':'value2' }
print(my_dict)

print(my_dict['key1'])

prices_lookup = {'apple' : 2.99 , 'oranges' : 3.99 , 'milk' : 0.80}
print(prices_lookup['oranges'])

# Dictionaries are flexible with type values

d = { 'k1' : 123, 'k2' : [0,1,2], 'k3' : {'insidekey':100} }

# It is the same declaration
# d = {
#      'k1' : 123,
#      'k2' : [0,1,2],
#      'k3' : {'insidekey':100}     
#      }

print(d['k2'])

print(d['k3'])
print(d['k3']['insidekey'])
print( d['k2'][2] )

c = {'key1' : [1,2,3,'a','b','c']}

my_new_list = c['key1']
print(my_new_list)

letter = my_new_list[3]
print(letter.upper())

d['key1'][2].upper()













