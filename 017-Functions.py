# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 00:12:28 2021

@author: Zsolt
"""

# =============================================================================
# FUNCTIONS
# starts with the def keyword, stands for DEFINITION
# functions use SNAKE CASING: all lowercase and underscore between words
# def name_of_the_function():
# =============================================================================

def greet (name):
    print('Hello ' + name)
    
greet('Zsolt')

def add_function (number1,number2):
    return number1+number2

print(add_function(5, 32))

# =============================================================================
# FUNCTIONS
# =============================================================================

def say_hello():
    print('hello')
    print('hello')
    print('hello')
    
say_hello()

def say_hello(name='Default'):
    print(f'Hello {name}')
    
say_hello()
say_hello('jelly')

def add_num(num1,num2):
    return num1+num2

result = add_num(55, 66)
print(result)







    