#import this to another file usually for larger projects

from random import randint

Die:

#first parameter always has to be self
def __init__(self, sides):
    # below is instance variable
    self.sides = sides
    self.value = 1
    #this is used to create an object

def get_value(self):
    return self.value
    # self will be die 1 on the function in program die, find the value

def roll(self):
    rand_num = randint(1, self.sides)
    self.value = rand_num

def set_value(self, value):
    self.value = value
    #for whatever function is calling self, set it equal to value