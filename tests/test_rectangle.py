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
                         [pytest.param(2, 4, 9, id='incorrect area')])

@pytest.mark.fall
def test_rectangle_area_fall(side_a, side_b,incorrect_area):
    with pytest.raises(AssertionError):
        r = Rectangle(side_a, side_b)
        assert r.area == incorrect_area, f'Rectangle area with sides {side_a} and {side_b} should be {incorrect_area}'

@pytest.mark.parametrize(("side_a", "side_b", "perimeter"),
                         [pytest.param(9,4,26, id='integer'),
                          pytest.param(9.5, 4.5, 28, id='float')]
                         )
@pytest.mark.smoke
def test_rectangle_perimeter_positive(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.perimeter == perimeter, f'Rectangle perimeter with sides {side_a} and {side_b} must be {perimeter}'

@pytest.mark.parametrize(("side_a", "side_b", "incorrect_perimeter"),
                         [pytest.param(2, 4, 9, id='incorrect perimeter')])

@pytest.mark.fall
def test_rectangle_perimeter_fall(side_a, side_b,incorrect_perimeter):
    with pytest.raises(AssertionError):
        r = Rectangle(side_a, side_b)
        assert r.perimeter == incorrect_perimeter, f'Rectangle area with sides {side_a} and {side_b} should be {incorrect_perimeter}'