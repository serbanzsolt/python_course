# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 19:18:19 2021

@author: Zsolt
"""

# =============================================================================
# WHILE LOOPS
# =============================================================================

x = 0
# x = 50
while x < 5:
    print(f'The Current value of x is : {x}')
    x = x + 1
    # x += 1
else:
    print('X is not less than 5')
    
# =============================================================================
# BREAK, CONTINUE, PASS
# =============================================================================

# PASS keyword = means do nothing
x = [1,2,3]
for item in x:
    #comment
    pass

print('end of my script')

# CONTINUE keyword = go back to the top of the closest enclosing loop
mystring = 'sammy'
for letter in mystring:
    print(letter)

for letter in mystring:
    if letter == 'a':
        continue
    print(letter)
    
# BREAK keyword = Breaks the current closest enclosing loop

for letter in mystring:
    if letter == 'a':
        break
    print(letter)

