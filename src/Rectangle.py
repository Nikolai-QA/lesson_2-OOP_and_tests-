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


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        if side_a <=0 or side_b <=0:
            raise ValueError('side_a and side_b must be greater than zero!')
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self):
        return self.side_b * self.side_a

    @property
    def perimeter(self):
        return (self.side_a + self.side_b) * 2


class Square(Rectangle):
    def __init__(self, side_a):
        super().__init__(side_a, side_a)

r = Rectangle(9, 4)
s = Square(6)
