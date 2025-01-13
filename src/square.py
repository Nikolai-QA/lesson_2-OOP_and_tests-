from figure import Figure


class Square(Figure):
    def __init__(self, side_a):
        self.side_a = side_a

    @property
    def area(self):
        return self.side_a ** 2

    @property
    def perimeter(self):
        return self.side_a * 4

s = Square(6)
print(s.perimeter)



















