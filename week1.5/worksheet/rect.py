# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        if not isinstance(width, int):
            raise TypeError("The width must be a number")
        if not isinstance(height, int):
            raise TypeError("The height must be a number")
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be greater than 0")


        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
    def is_square(self):
        """
        Returns True if the rectangle is actually square, False otherwise.
        """
        return self.width == self.height

    def area(self):
        """
        Calculates the area of the rectangle and returns the result.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle and returns the result.
        """
        return (2 * self.width) + (2 * self.height)

r= Rectangle(2, 2)
print(r.width, r.height)
print(r.area())
print(r.perimeter())
print(r.is_square())