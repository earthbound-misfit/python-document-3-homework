from math import pi

#1) Has a function to calculate the square footage of a house
#Reminder of Formula: Length X Width == Area
def square_footage(length,width):
    area = length * width
    print(f'The square footage of your house is {area}.')


#2) Has a function to calculate the circumference of a circle
def calc_circumference(radius):
    circumference = 2 * pi * radius
    print(circumference)
