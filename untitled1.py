# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 11:35:23 2021

@author: Zsolt
"""

class Animal():
    
    def __init__(self):
        print('An animal crated')
        
    def who_am_i (self):
        print('I am an animal')
        
    def eat(self):
        print('I am eating')

myanimal = Animal()        

class dog (Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print('dog created')
        
    #override
    def who_am_i (self):
        print('i amm a dog')

my_dog = dog()
my_dog.who_am_i()

