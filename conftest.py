import pytest

from src.square import Square
from src.rectangle import Rectangle
from src.circle import Circle
from src.triangle import Triangle


@pytest.fixture
def rectangle():
    return Rectangle(9, 4)

@pytest.fixture
def square():
    return Square(6)

@pytest.fixture
def rectangle_float():
    return Rectangle(9.5, 4.5)

@pytest.fixture
def square_float():
    return Square(6.5)

@pytest.fixture
def circle():
    return Circle(5)

@pytest.fixture
def circle_float():
    return Circle(5.5)

@pytest.fixture
def triangle():
    return Triangle(4, 9, 8)

@pytest.fixture
def triangle_float():
    return Triangle(4.5, 9.5, 8.5)