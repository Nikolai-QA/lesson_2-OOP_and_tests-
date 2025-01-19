import pytest

from src.square import Square


@pytest.mark.parametrize(("side_a", "area"),
                         [pytest.param(6,36, id='integer'),
                          pytest.param(6.5,42.25, id='float')]
                         )

@pytest.mark.smoke
def test_square_area_positive(side_a, area):
    s = Square(side_a)
    assert s.area == area, f'Square area with side {side_a} must be {area}'


@pytest.mark.parametrize(("side_a", "incorrect_area"),
                         [pytest.param(2, 9, id='incorrect area')])

@pytest.mark.fall
def test_square_area_fall(side_a, incorrect_area):
    with (pytest.raises(AssertionError)):
        s = Square(side_a)
        assert s.area == incorrect_area, f'Square area with side {side_a} should be {incorrect_area}'

@pytest.mark.parametrize(("side_a", "perimeter"),
                         [pytest.param(6,24, id='integer'),
                          pytest.param(6.5, 26, id='float')]
                         )
@pytest.mark.smoke
def test_square_perimeter_positive(side_a, perimeter):
    s = Square(side_a)
    assert s.perimeter == perimeter, f'Square perimeter with side {side_a} must be {perimeter}'

@pytest.mark.parametrize(("side_a", "incorrect_perimeter"),
                         [pytest.param(2, 9, id='incorrect perimeter')])

@pytest.mark.fall
def test_square_perimeter_fall(side_a, incorrect_perimeter):
    with pytest.raises(AssertionError):
        s = Square(side_a)
        assert s.perimeter == incorrect_perimeter, f'Square area with side {side_a} should be {incorrect_perimeter}'