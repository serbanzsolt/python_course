# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 17:58:20 2021

@author: Zsolt
"""

# =============================================================================
# Statements
# IF, ELIF, ELSE
# =============================================================================
a = 100
if (a==1):
    print('1')
elif (a==2):
    print('2')
else:
    print('3')
    
if True:
    print('Its TRUE')
    
if 3>2:
    print('Its TRUE')
    
hungry = False

if hungry:
    print('FEED ME!')
else:
    print('not hungry')
    
loc = 'Bank'

if loc =='Auto Shop':
    print('Cars are cool!')
elif loc == 'Bank':
    print('Money is Cool!')
else:
    print('I do not know much')
    
name = 'Sammy'

if name == 'Franky':
    print('Hello Franky')
elif name == 'Sammy':
    print('Hello Sammy')
else:
    print('What is your name?')