"""Test operations.py"""

import pytest
from app.operations import Operation
from app.exceptions import OperationError

def test_add():
    assert Operation.add(1,1) == 2

def test_subtract():
    assert Operation.subtract(1,1) == 0

def test_multiply():
    assert Operation.multiply(1,1) == 1

def test_division():
    assert Operation.divide(4,2) == 2

def test_power():
    assert Operation.power(2,2) == 4

def test_root():
    assert Operation.root(36, 2) == 6 

def test_modulus():
    assert Operation.modulus(13, 3) == 1

def test_int_divide():
    assert Operation.int_divide(10, 3) == 3

def test_percent():
    assert Operation.percent(10, 100) == 10 

def test_abs_diff():
    assert Operation.abs_diff(4, 5) == 1


""" Test Exceptions"""
def test_divide_with_zero():
    with pytest.raises(OperationError, match="Cannot perform division by zero"):
        Operation.divide(1, 0)

def test_root_with_zero():
    with pytest.raises(OperationError, match="Cannot perform root with degree zero"):
        Operation.root(36, 0)

def test_root_with_negative():
    with pytest.raises(OperationError, match="Cannot perform root with negative number"):
        Operation.root(-36, 2)

def test_modulus_with_zero():
    with pytest.raises(OperationError, match="Cannot perform modulus by zero"):
        Operation.modulus(13, 0)

def test_int_divide_with_zero():
    with pytest.raises(OperationError, match="Cannot perform integer division by zero"):
        Operation.int_divide(10, 0)

def test_percent_with_zero():
    with pytest.raises(OperationError, match="Cannot perform division by zero"):
        Operation.percent(10, 0)