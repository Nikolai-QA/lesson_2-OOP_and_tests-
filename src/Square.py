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
            raise TypeError ('The object is not a figure!')
        return self.area + figure.area

class Square(Figure):
    def __init__(self, side_a):
        self.side_a = side_a

    @property
    def area(self):
        return self.side_a ** 2

    @property
    def perimeter(self):
        return self.side_a * 4

class Triangle(Square):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError ('side_a must be greater than zero!')
        super().__init__(side_a)
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        sp = self.perimeter / 2
        return (sp * (sp - self.side_a) * (sp - self.side_b) * (sp - self.side_c)) ** 0.5

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

s = Square(6)
t = Triangle(2,3,4)



















