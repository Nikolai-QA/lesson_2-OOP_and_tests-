import pytest

from src.circle import Circle


@pytest.mark.parametrize(("radius", "area"),
                         [pytest.param(5, 78.53981633974483, id='integer'),
                          pytest.param(5.5, 95.03317777109125, id='float')]
                         )

@pytest.mark.smoke
def test_circle_area_positive(radius, area):
    c = Circle(radius)
    assert c.area == area, f'Circle area with radius {radius} must be {area}'


@pytest.mark.parametrize(("radius", "incorrect_area"),
                         [pytest.param(1, 3.151592653589793, id='incorrect area')])

@pytest.mark.fall
def test_circle_area_fall(radius, incorrect_area):
    with (pytest.raises(AssertionError)):
        c = Circle(radius)
        assert c.area == incorrect_area, f'Circle area with radius {radius} should be {incorrect_area}'

@pytest.mark.parametrize(("radius", "perimeter"),
                         [pytest.param(5, 31.41592653589793, id='integer'),
                          pytest.param(5.5, 34.55751918948772, id='float')]
                         )
@pytest.mark.smoke
def test_circle_perimeter_positive(radius, perimeter):
    c = Circle(radius)
    assert c.perimeter == perimeter, f'Circle perimeter with side {radius} must be {perimeter}'

@pytest.mark.parametrize(("radius", "incorrect_perimeter"),
                         [pytest.param(1, 6.273185307179586, id='incorrect perimeter')])

@pytest.mark.fall
def test_circle_perimeter_fall(radius, incorrect_perimeter):
    with pytest.raises(AssertionError):
        c = Circle(radius)
        assert c.perimeter == incorrect_perimeter, f'Circle area with radius {radius} should be {incorrect_perimeter}'