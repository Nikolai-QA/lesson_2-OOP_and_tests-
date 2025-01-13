from figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be greater than zero!")
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return math.pi * self.radius * 2

c = Circle(5)