# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 22:48:47 2021

@author: Zsolt
"""
# =============================================================================
# 1
# =============================================================================

st = 'Print only the words that start with s in this sentence'
starting_with_s = []
puffer_list = st.split(' ')

print(puffer_list)
print(puffer_list[0][0])

for word in puffer_list:
    if (word[0] == 's' or word[0] =='S'):
        starting_with_s.append(word)
    
print(starting_with_s)

# =============================================================================
# 2
# =============================================================================

for x in range(0,11,2):
    print(x)
    
# =============================================================================
# 3
# =============================================================================
result = [ x for x in range(1,51) if x%3==0 ]
print (result)

# =============================================================================
# 4
# =============================================================================

st = 'Print every word in this sentence that has an even number of letters'

puff = st.split(' ')
print(puff)
list_of_even = []

for word in puff:
    if (len(word))%2 == 0:
        list_of_even.append(word)
        print(f'Word with the number of even letters({(len(word))}): {word}')
    
print(list_of_even)

# =============================================================================
# 5
# =============================================================================
 
for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print('FIZZBUZZ')
    elif x % 3 == 0:
        print('FIZZ')
    elif x % 5 == 0:
        print('BUZZ')
    else:
        print(x)

# =============================================================================
# 6
# =============================================================================

st = 'Create a list of the first letters of every word in this string'

result2 = [ word[0] for word in st.split(' ') ]
print(result2)

   
    
    
