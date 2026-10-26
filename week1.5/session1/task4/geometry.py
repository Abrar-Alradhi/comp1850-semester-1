# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math
class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y # Add constructor here

    # Add distance() method here
    def distance(self):
        return math.hypot(self.x, self.y)
    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self, point):
        """
        return distance from this point to the specified point.
        """
        return math.hypot(self.x - point.x, self.y - point.y)
# Copy Point class definition here

# Add a definition for a Circle class here, giving it
class Circle:
    def __init__(self, radius, centre=Point(0.0, 0.0)):
        """
        returns a circle object, with the given radius $ centre coordinates.

        centre coordinates default to origin.
        """
        self.radius = radius
        self.centre = centre

    def area(self):
        """
        returns the area of the circle.
        """
        return math.pi * self.radius * self.radius
    def perimeter(self):
        """
        returns the perimeter of the circle
        """
        return 2* math.pi * self.radius

#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!
