import pytest

from src.triangle import Triangle


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area"),
                         [pytest.param(4, 9, 8, 15.998046755776157, id='integer'),
                          pytest.param(4.5, 9.5, 8.5, 19.11672615146223, id='float')]
                         )

@pytest.mark.smoke
def test_triangle_area_positive(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.area == area, f'Triangle area with sides {side_a} and {side_b} and {side_c} must be {area}'


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "incorrect_area"),
                         [pytest.param(2, 9, 1, 19.11672615146223, id='incorrect area')])

@pytest.mark.fall
def test_triangle_area_fall(side_a, side_b, side_c, incorrect_area):
    with (pytest.raises(AssertionError)):
        t = Triangle(side_a, side_b, side_c)
        assert t.area == incorrect_area, f'Triangle area with sides {side_a} and {side_b} and {side_c} should be {incorrect_area}'

@pytest.mark.parametrize(("side_a", "side_b", "side_c", "perimeter"),
                         [pytest.param(4, 9, 8, 21, id='integer'),
                          pytest.param(4.5, 9.5, 8.5, 22.5, id='float')]
                         )
@pytest.mark.smoke
def test_triangle_perimeter_positive(side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.perimeter == perimeter, f'Triangle area with sides {side_a} and {side_b} and {side_c} must be {perimeter}'

@pytest.mark.parametrize(("side_a", "side_b", "side_c", "incorrect_perimeter"),
                         [pytest.param(2, 9, 66, 19.582221, id='incorrect perimeter')])

@pytest.mark.fall
def test_triangle_perimeter_fall(side_a, side_b, side_c, incorrect_perimeter):
    with pytest.raises(AssertionError):
        t = Triangle(side_a,side_b, side_c)
        assert t.perimeter == incorrect_perimeter, f'Triangle area with sides {side_a} and {side_b} and {side_c} should be {incorrect_perimeter}'