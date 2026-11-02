# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
from shapes import Shape

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(position, red)
    def __init__(self, radius):
        if not isinstance(radius, (int,float)):
            raise TypeError("The supplied value should be a number")
        if radius <= 0:
            raise ValueError