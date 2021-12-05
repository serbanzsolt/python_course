# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 21:07:13 2021

@author: Zsolt
"""

# =============================================================================
# LIST COMPREHENSIONS - unique way to create a list
# =============================================================================

# =============================================================================
# FLATTENED FOR-LOOPS
# =============================================================================

mystring = 'hello'
mylist = []

for letter in mystring:
    mylist.append(letter)
    
print(mylist)

# FLATTENED:
    
mylist2 = [letter for letter in mystring]
print(mylist2)

mylist3 = [x for x in 'word']
print(mylist3)

mylist4 = [asdasd for asdasd in 'word']
print(mylist4)

mylist5 = [x for x in range(0,11)]
print(mylist5)

mylist6 = [num**2 for num in range(0,11)]
print(mylist6)

mylist7 = [num**2 for num in range(0,11) if num%2==0]
print(mylist7)

celsius = [0,10,20,34.5]

fahrenheit = [( (9/5) *temp + 32) for temp in celsius] 
print(fahrenheit)

fahrenheit2 = []
for temp in celsius:
    fahrenheit2.append( ((9/5) * temp + 32) )

print (fahrenheit2)


# Readability key when programming, 
# if I come back after a month and check this I wont understand it :)

results = [x if x%2==0 else 'odd' for x in range(0,11)]
print(results)

# =============================================================================
# NESTED LOOPS
# =============================================================================

mylist8 = []

for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist8.append(x*y)
        
print(mylist8)

mylist9 = [x*y for x in [2,4,6] for y in [1,10,1000]]

