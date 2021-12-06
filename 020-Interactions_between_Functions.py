# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 01:42:07 2021

@author: Zsolt
"""

# =============================================================================
#  INTERACTIONS BETWEEN FUNCTIONS
# =============================================================================

example = [1,2,3,4,5,6,7]

from random import shuffle

shuffle(example)

print(example)
result = shuffle(example)
print(result)

def shuffle_list (mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
print(result)

mygame = [' ', 'O', ' ']

shuffle_list(mygame)

def player_guess ():
    
    guess = ''
    
    while guess not in ['0','1','2']:
        guess = input ("Pick a number: 0,1 or 2: ")
    
    return int(guess)

# 1my_index = player_guess()

def check_guess (gamelist,guess):
    if gamelist[guess] == 'O':
        print('CORRECT!')
    else:
        print('WRONG GUESS!')
        print(gamelist)
    
    
# =============================================================================
#     THE GAME
# =============================================================================
    
# INITIAL LIST
mygame = [' ', 'O', ' ']
# SHUFFLE LIST
mixedup_list = shuffle_list(mygame)
# USER GUESS
guess = player_guess()
# CHECK GUESS
check_guess(mixedup_list, guess)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
