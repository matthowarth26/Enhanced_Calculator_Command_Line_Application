import pytest
from app.calculation import addition, subtraction, multiplcation, division

def test_addition():
    assert addition(1,1) == 2

def test_subtraction():
    assert subtraction(1,1) == 0

def test_multiplcation():
    assert multiplcation(1,1) == 1

def test_division():
    assert division(4,2) == 2

def test_division_with_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        division(1, 0)