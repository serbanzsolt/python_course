# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:49:39 2021

@author: Zsolt
"""
import string

def is_palindrome (word):
    word = word.replace(' ','')
    if word == word[::-1]:
        return True
    else:
        return False
        

text = 'apple and pear'
print(list(text))

print(is_palindrome('tenet'))


print(set(string.ascii_lowercase))

