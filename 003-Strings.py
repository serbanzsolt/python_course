# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 00:36:51 2021

@author: Zsolt
"""

print("HEllo")
print('World')
print('this is also a string')
print(" and this is too")

# =============================================================================
# escape sequence
# =============================================================================

print("hello \n world")

print(len('how much character is this word'))

# =============================================================================
# String Indexing and Slicing
# =============================================================================

mystring = "Hello World"

print(mystring)

# indexing

print(mystring[0])
print(mystring[8])
print(mystring[-3])

# slicing

newstring = 'abcdefghijk'
print(newstring[2:])
print(newstring[:3])
print(newstring[3:6])

# stepsize

print(newstring[::2])
print(newstring[2:7:2])

# =============================================================================
# String Properties and Methods
# =============================================================================

# Immutability

name = "Sam"

#name[0] = "p" #CANNOT DO IT

print(name[1:])
last_letters = name[1:]
print("P" + last_letters)

# =============================================================================
# String Concatenation
# =============================================================================

x = "Hello world"
x = x + " it's beautifull outside"
print(x)

letter = "z"
print(letter * 10)

print(1+3)
print("1"+"3")

#Methods

y = "Hello World"
# IMPORTANT!!!
y = y.upper()
# or
print(y.upper())

z = "this is a string method"
z = z.split()
print(z)

z = "this is a string method"
z = z.split("i")
print(z)

