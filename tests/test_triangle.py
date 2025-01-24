import pytest

from src.triangle import Triangle


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area"),
                         [pytest.param(4, 9, 8, 16.0, id='integer'),
                          pytest.param(4.5, 9.5, 8.5, 19.1, id='float')]
                         )

@pytest.mark.smoke
def test_triangle_area_positive(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert round(t.area, 1) == area, f'Triangle area with sides {side_a} and {side_b} and {side_c} must be {area}'


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "incorrect_area"),
                         [pytest.param(0, 0, 0, 0, id='incorrect area')])

@pytest.mark.fall
def test_triangle_area_fall(side_a, side_b, side_c, incorrect_area):
    with (pytest.raises(ValueError)):
        t = Triangle(side_a, side_b, side_c)
        assert t.area == incorrect_area, f'Triangle area with sides {side_a} and {side_b} and {side_c} must be greater than zero.'

@pytest.mark.parametrize(("side_a", "side_b", "side_c", "perimeter"),
                         [pytest.param(4, 9, 8, 21, id='integer'),
                          pytest.param(4.5, 9.5, 8.5, 22.5, id='float')]
                         )
@pytest.mark.smoke
def test_triangle_perimeter_positive(side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.perimeter == perimeter, f'Triangle area with sides {side_a} and {side_b} and {side_c} must be {perimeter}'

@pytest.mark.parametrize(("side_a", "side_b", "side_c", "incorrect_perimeter"),
                         [pytest.param(-1, -3, -2, -6, id='incorrect perimeter')])

@pytest.mark.fall
def test_triangle_perimeter_fall(side_a, side_b, side_c, incorrect_perimeter):
    with pytest.raises(ValueError):
        t = Triangle(side_a,side_b, side_c)
        assert t.perimeter == incorrect_perimeter, f'Triangle area with sides {side_a} and {side_b} and {side_c} must be greater than zero.'

@pytest.mark.parametrize("add_area",
                         [pytest.param(52.0, id='integer')]
                         )
@pytest.mark.smoke
def test_add_area_integer(triangle, square, add_area):
    result = triangle.add_area(square)
    assert round(result, 1) == add_area, f"triangle.area + square.area must be {add_area}"

@pytest.mark.parametrize("add_area",
                         [pytest.param(61.4, id='float')]
                         )
@pytest.mark.smoke
def test_add_area_float(triangle_float, square_float, add_area):
    result = triangle_float.add_area(square_float)
    assert round(result, 1) == add_area, f"triangle_float.area + square_float.area must be {add_area}"