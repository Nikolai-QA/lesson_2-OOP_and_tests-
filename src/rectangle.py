from figure import Figure



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

r = Rectangle(9, 4)
print(r.add_area(r))
