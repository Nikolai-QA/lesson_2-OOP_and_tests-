from figure import Figure


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

t = Triangle(4,9,8)
print(t.perimeter)


