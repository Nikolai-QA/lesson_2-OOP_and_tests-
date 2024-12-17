from abc import ABC, abstractmethod


class Figure(ABC):

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise TypeError('The object is not a figure!')
        return self.area + figure.area


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <=0 or side_b <=0 or side_c <=0:
            raise ValueError('side_a or side_b or side_c must be greater than zero!')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        sp = self.perimeter / 2
        return (sp * (sp - self.side_a) * (sp - self.side_b) * (sp - self.side_c)) ** 0.5

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

class Rectangle(Triangle):
    def __init__(self, side_a, side_b):
        side_c = ((side_a ** 2 + side_b ** 2) ** 0.5)
        super().__init__(side_a, side_b, side_c)


    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimeter(self):
        return (self.side_a + self.side_b) * 2


t = Triangle(1,2,3)
r = Rectangle(5,6)


