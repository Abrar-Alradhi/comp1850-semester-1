# Week 1.5, Session 1: Task 3
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



# Finally, add code here to demonstrate use of Point
p = Point(4, 8)
q = Point(2, 7)
print(p.distance_to(q))
