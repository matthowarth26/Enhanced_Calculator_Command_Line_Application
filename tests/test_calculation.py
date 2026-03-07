import pytest
from app.calculation import add, subtract, multiply, divide

def test_add():
    assert add(1,1) == 2

def test_subtract():
    assert subtract(1,1) == 0

def test_multiply():
    assert multiply(1,1) == 1

def test_division():
    assert divide(4,2) == 2

def test_divide_with_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)