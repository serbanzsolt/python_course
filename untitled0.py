# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:57:57 2021

@author: Zsolt
"""

class Dog():
    
    species = 'mammal'
    
    
    def __init__(self, breed,name,spots):
        
        self.breed = breed
        self.name = name
        self.spots = spots
        
    #OPERATIONS/ACTIONS ----> METHODS
    def bark(self):
        print("WOOF! My name is {}".format(self.name))
        
        
my_dog = Dog(breed='Lab',name='Sammy',spots=False)
print(my_dog.breed)
print(my_dog.species)
my_dog.bark()


class Circle():
    pi = 3.14
    
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * self.pi
        
    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(30)
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)

    