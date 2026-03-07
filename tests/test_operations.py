import pytest
from app.operations import add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff
from app.exceptions import OperationError

def test_add():
    assert add(1,1) == 2

def test_subtract():
    assert subtract(1,1) == 0

def test_multiply():
    assert multiply(1,1) == 1

def test_division():
    assert divide(4,2) == 2

def test_power():
    assert power(2,2) == 4

def test_root():
    assert root(36, 2) == 6 

def test_modulus():
    assert modulus(13, 3) == 1

def test_int_divide():
    assert int_divide(10, 3) == 3

def test_percent():
    assert percent(10, 100) == 10 

def test_abs_diff():
    assert abs_diff(4, 5) == 1


""" Test Exceptions"""
def test_divide_with_zero():
    with pytest.raises(OperationError, match="Cannot perform division by zero"):
        divide(1, 0)

def test_root_with_zero():
    with pytest.raises(OperationError, match="Cannot perform root with degree zero"):
        root(36, 0)

def test_modulus_with_zero():
    with pytest.raises(OperationError, match="Cannot perform modulus by zero"):
        modulus(13, 0)

def test_int_divide_with_zero():
    with pytest.raises(OperationError, match="Cannot perform integer division by zero"):
        int_divide(10, 0)

def test_percent_with_zero():
    with pytest.raises(OperationError, match="Cannot perform division by zero"):
        percent(10, 0)