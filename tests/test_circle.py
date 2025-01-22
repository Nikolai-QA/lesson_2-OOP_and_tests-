import pytest

from src.circle import Circle


@pytest.mark.parametrize(("radius", "area"),
                         [pytest.param(5, 78.5, id='integer'),
                          pytest.param(5.5, 95.0, id='float')]
                         )

@pytest.mark.smoke
def test_circle_area_positive(radius, area):
    c = Circle(radius)
    assert round(c.area, 1) == area, f'Circle area with radius {radius} must be {area}'



@pytest.mark.parametrize(("radius", "incorrect_area"),
                         [pytest.param(0, 0, id='incorrect area')])

@pytest.mark.fall
def test_circle_area_fall(radius, incorrect_area):
    with (pytest.raises(ValueError)):
        c = Circle(radius)
        assert c.area == incorrect_area, f'Circle area with radius {radius} must be greater than zero.'

@pytest.mark.parametrize(("radius", "perimeter"),
                         [pytest.param(5, 31.4, id='integer'),
                          pytest.param(5.5, 34.6, id='float')]
                         )
@pytest.mark.smoke
def test_circle_perimeter_positive(radius, perimeter):
    c = Circle(radius)
    assert round(c.perimeter, 1) == perimeter, f'Circle perimeter with side {radius} must be {perimeter}'

@pytest.mark.parametrize(("radius", "incorrect_perimeter"),
                         [pytest.param(-1, -6.3, id='incorrect perimeter')])

@pytest.mark.fall
def test_circle_perimeter_fall(radius, incorrect_perimeter):
    with pytest.raises(ValueError):
        c = Circle(radius)
        assert round(c.perimeter, 1) == incorrect_perimeter, f'Circle area with radius {radius} must be greater than zero.'

@pytest.mark.parametrize("add_area",
                         [pytest.param(114.5, id='integer')]
                         )
@pytest.mark.smoke
def test_add_area_integer(circle, rectangle, add_area):
    result = circle.add_area(rectangle)
    assert round(result, 1) == add_area, f"circle.area + rectangle.area must be {add_area}"

@pytest.mark.parametrize("add_area",
                         [pytest.param(137.8, id='float')]
                         )
@pytest.mark.smoke
def test_add_area_float(circle_float, rectangle_float, add_area):
    result = circle_float.add_area(rectangle_float)
    assert round(result, 1) == add_area, f"circle_float.area + rectangle_float.area must be {add_area}"