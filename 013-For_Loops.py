# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 18:22:27 2021

@author: Zsolt
"""

# =============================================================================
# FOR LOOP
# =============================================================================

mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print(num)

print('\nOnly the even numbers:')
for num in mylist:
    # Check for even
    if num % 2 == 0:
        print (num)
print('\nSplitting them:')        
for num in mylist:
    # Check for even
    if num % 2 == 0:
        print (f'{num}. Even number:', num)
    else:
        print (f'{num}. Odd number:', num)

print('\nListing the sum of the numbers:')
list_total = 0
for num in mylist:
    list_total = list_total + num
    
print(f'The total of the numbers is: {list_total}')

word = 'hello'

for wrd in word:
    print(wrd)
    
for wrd in 'hello':
    print(wrd)
    
# If you dont use the for variable
# its a common syntax to write _ as variable name

# =============================================================================
# FOR WITH TUPLES
# =============================================================================
print('FOR WITH TUPLES')
tup = (1,2,3)
for item in tup:
    print(item)

tup_list = [(1,2),(3,4),(5,6),(7,8)]
print('number of items:')
print(len(tup_list))

for item in tup_list:
    print(item)

# =============================================================================
# TUPLE UNPACKING
# =============================================================================
print('a:')
for (a,b) in tup_list:
    print(a)
print('b:')
for (a,b) in tup_list:
    print(b)

print('ab:')
for (a,b) in tup_list:
    print(a)
    print(b)

tup_list2 = [(1,2,3),(4,5,6),(7,8,9)]

for a,b,c in tup_list2:
    print(f'middle item: {b}')

# =============================================================================
# ITERATION OF DICTIONARY
# =============================================================================

d = {'k1' : 1, 'k2' : 2, 'k3' : 3 }

for item in d:
    print(item)

for key,value in d:
    print(value)
    
for key,value in d.items():
    print(value)
    
for value in d.values():
    print(value)

raw_list = 10*[0]
for _ in raw_list:
    print(_)







