# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 17:42:36 2021

@author: Zsolt
"""
score = ((5 ** 2) / 100) + (50+75-25)
print(score)

s = 'hello'
print(s[1])
print(s[-4])
print(s[4:])
print(s[-1])

mylist = [0]
mylist.append(0)
mylist.append(0)
print(mylist)

list3 = [1,2,[3,4,'hello']]

list3[2][2] = 'goodbye'
print ( list3)

d = {'simple_key':'hello'}
# Grab 'hello'
print(d['simple_key'])

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello
print ( d['k1'][0]['nest_key'][1]) 

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2])