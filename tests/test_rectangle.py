import pytest
from src.rectangle import Rectangle



@pytest.mark.parametrize(("side_a", "side_b", "area"),
                         [pytest.param(9,4,36, id='integer'),
                          pytest.param(9.5, 4.5, 42.75, id='float')]
                         )

@pytest.mark.smoke
def test_rectangle_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == area, f'Rectangle area with sides {side_a} and {side_b} must be {area}'


@pytest.mark.parametrize(("side_a", "side_b", "incorrect_area"),
                         [pytest.param(0, 1, 0, id='incorrect area')])

@pytest.mark.fall
def test_rectangle_area_fall(side_a, side_b,incorrect_area):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
        assert r.area == incorrect_area, f'Rectangle sides {side_a} and {side_b} must be greater than zero!'

@pytest.mark.parametrize(("side_a", "side_b", "perimeter"),
                         [pytest.param(9,4,26, id='integer'),
                          pytest.param(9.5, 4.5, 28, id='float')]
                         )
@pytest.mark.smoke
def test_rectangle_perimeter_positive(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.perimeter == perimeter, f'Rectangle perimeter with sides {side_a} and {side_b} must be {perimeter}'

@pytest.mark.parametrize(("side_a", "side_b", "perimeter"),
                         [pytest.param(0, 1, 0, id='integer')]
                         )
@pytest.mark.smoke
def test_rectangle_perimeter_fall(side_a, side_b, perimeter):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
        assert r.perimeter == perimeter, f'Rectangle sides {side_a} and {side_b} must be greater than zero!'

@pytest.mark.parametrize("add_area",
                         [pytest.param(72, id='integer')]
                         )
@pytest.mark.smoke
def test_add_area_integer(rectangle, square, add_area):
    result = rectangle.add_area(square)
    assert result == add_area, f"rectangle.area + square.area must be {add_area}"

@pytest.mark.parametrize("add_area",
                         [pytest.param(85.0, id='float')]
                         )
@pytest.mark.smoke
def test_add_area_float(rectangle_float, square_float, add_area):
    result = rectangle_float.add_area(square_float)
    assert result == add_area, f"rectangle_float.area + square_float.area must be {add_area}"