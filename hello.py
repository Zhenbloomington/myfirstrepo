# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:04:30 2020

@author: Zhen.Li
"""
def world():
    print("Hello, World!")

# Define a variable
shark = "Sammy"

# define a class
class Octopus:
     def __init__(self, name, color):
         self.color = color
         self.name = name
         
     def tell_me_about_the_octopus(self):
         print("This octopus is " + self.color + "." )
         print(self.name + " is the octopus's name.")
