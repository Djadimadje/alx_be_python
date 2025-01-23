import math

class Shape:
    def area(self):
        """
        Base method to calculate the area of a shape.
        This method is intended to be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must override this method")


class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Derived class for a rectangle.
        :param length: Length of the rectangle (int or float).
        :param width: Width of the rectangle (int or float).
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the area method to calculate the area of a rectangle.
        :return: Area of the rectangle (length × width).
        """
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """
        Derived class for a circle.
        :param radius: Radius of the circle (int or float).
        """
        self.radius = radius

    def area(self):
        """
        Overrides the area method to calculate the area of a circle.
        :return: Area of the circle (π × radius²).
        """
        return math.pi * (self.radius ** 2)
