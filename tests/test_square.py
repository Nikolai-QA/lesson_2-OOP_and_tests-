import pytest
from src.square import Square



@pytest.mark.parametrize(("side_a", "area"),
                         [pytest.param(6, 36, id='integer'),
                          pytest.param(6.5, 42.25, id='float')]
                         )

@pytest.mark.smoke
def test_square_area_positive(side_a, area):
    s = Square(side_a)
    assert s.area == area, f'Square area with side {side_a} must be {area}'


@pytest.mark.parametrize(("side_a", "incorrect_area"),
                         [pytest.param(0, 0, id='incorrect area')])

@pytest.mark.fall
def test_square_area_fall(side_a, incorrect_area):
    with (pytest.raises(ValueError)):
        s = Square(side_a)
        assert s.area == incorrect_area, f'Square area with side {side_a} must be greater than zero.'

@pytest.mark.parametrize(("side_a", "perimeter"),
                         [pytest.param(6, 24, id='integer'),
                          pytest.param(6.5, 26, id='float')]
                         )
@pytest.mark.smoke
def test_square_perimeter_positive(side_a, perimeter):
    s = Square(side_a)
    assert s.perimeter == perimeter, f'Square perimeter with side {side_a} must be {perimeter}'

@pytest.mark.parametrize(("side_a", "incorrect_perimeter"),
                         [pytest.param(-1, -4, id='incorrect perimeter')])

@pytest.mark.fall
def test_square_perimeter_fall(side_a, incorrect_perimeter):
    with pytest.raises(ValueError):
        s = Square(side_a)
        assert s.perimeter == incorrect_perimeter, f'Square area with side {side_a} must be greater than zero.'


@pytest.mark.parametrize("add_area",
                         [pytest.param(72, id='integer')]
                         )
@pytest.mark.smoke
def test_add_area_integer(square, rectangle, add_area):
    result = square.add_area(rectangle)
    assert result == add_area, f"square.area + rectangle.area must be {add_area}"

@pytest.mark.parametrize("add_area",
                         [pytest.param(85.0, id='float')]
                         )
@pytest.mark.smoke
def test_add_area_float(square_float, rectangle_float, add_area):
    result = square_float.add_area(rectangle_float)
    assert result == add_area, f"square_float.area + rectangle_float.area must be {add_area}"
