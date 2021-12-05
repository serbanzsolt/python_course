# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 19:35:42 2021

@author: Zsolt
"""
# =============================================================================
# RANGE
# =============================================================================

mylist = [1,2,3,4,5]

for num in range(10):
    print(num)
    
for num in range(3,10):
    print(num)
    
for num in range(0,10,2):
    print(num)
    
for _ in range(100):
    print(_)
    
# range as a generator

print(type(range(0,10,2)))

# Casting a list using range as generator

new_list = list(range(0,10,2))              
print(new_list)

# =============================================================================
# ENUMERATE
# =============================================================================

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1

# ENUMERATE
for item in enumerate(word):
    print(item)

# ENUMERATE GIVES BACK TUPLES

# Using tuples unpacking:

for a,b in  enumerate(word):
    print(a)
    print(b)
    print('\n')

# =============================================================================
# ZIP - opposite of unpacking tuples, will only zip the many as the smallest list
# =============================================================================

mylist1 = [1,2,3,4,5]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]

for item in zip(mylist1,mylist2,mylist3):
    print (item)
    
# Casting zip to a list

zipped_list = list(zip(mylist1,mylist2,mylist3))
print(zipped_list)

# =============================================================================
# IN operator
# =============================================================================

print('x' in [1,2,3])
print('x' in ['x','y','z'])
print('X' in ['x','y','z'])

print('mykey' in {'mykey':123})
d = {'mykey':123}
print(123 in d.values())

# =============================================================================
# MATHEMATICAL - MIN, MAX
# =============================================================================

mylist4 = [10,20,30,40,50]
print(min(mylist4))
print(max(mylist4))

# =============================================================================
# MATHEMATICAL - RANDOM
# =============================================================================

from random import shuffle

mylist5 = [1,2,3,4,5,6,7,8,9,10]
print(mylist5)
shuffle(mylist5)
print(mylist5)

from random import randint

x = randint(0, 10)

print(f'Here is a random number 0-10: {x}')

for _ in range(0,11):
    print(randint(0, 100))

# =============================================================================
# INPUT using for user input functions
# =============================================================================

input('Enter a number here: ')
result = input('Enter a number here: ')

print(f'your entered: {result} above')
print(type(result))

print(f'your entered: {result} above and its type is(CAST): ', type(int(result)))

result = int(input('Enter a number(INT) here: '))
print(f'your entered: {result} above and its type is(NO CAST): ', type(result))

