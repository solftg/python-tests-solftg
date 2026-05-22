import pytest
from math_utils import (
    add,
    subtract,
    multiply,
    divide,
)

@pytest.mark.parametrize("a, b, expected", [
    (1, 3, 4),
    (-3, 3, 0),
    (3.5, 4.5, 8)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b", [
    ("6", 7),
    ([6], 7),
    (True, 7),
    (None, 7),
])
def test_add_type(a, b):
    with pytest.raises(TypeError):
        add(a, b)

@pytest.mark.parametrize("a, b, expected", [
    (2, 1, 1),
    (-3, 3, -6),
    (3.5, 4.5, -1)
])
def test_substract(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a, b", [
    ("6", 7),
    ([6], 7),
    (True, 7),
    (None, 7),
])
def test_subtract_type(a, b):
    with pytest.raises(TypeError):
        subtract(a, b)

@pytest.mark.parametrize("a, b, expected", [
    (6, 7, 42),
    (-3, 4, -12),
    (3.5, 4.5, 15.75)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b", [
    ("6", 7),
    ([6], 7),
    (True, 7),
    (None, 7),
])
def test_multiply_type(a, b):
    with pytest.raises(TypeError):
        multiply(a, b)

@pytest.mark.parametrize("a, b, expected", [
    (42, 6, 7),
    (-36, 6, -6),
    (15.5, 5, 3.1)
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected


@pytest.mark.parametrize("a, b", [
    ("6", 7),
    ([6], 7),
    (True, 7),
    (None, 7),
])
def test_divide_type(a, b):
    with pytest.raises(TypeError):
        divide(a, b)

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)