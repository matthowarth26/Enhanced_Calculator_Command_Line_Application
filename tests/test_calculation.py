import pytest

from app.calculation import Calculation, Addition, Subtraction, Multiplication, Division, Power, Root, Modulus, IntegerDivision, Percentage, AbsoluteDifference
from app.exceptions import OperationError

def test_addition_compute():
    calculation = Addition(1, 1)
    assert calculation.compute() == 2

def test_subtraction_compute():
    calculation = Subtraction(1, 1)
    assert calculation.compute() == 0

def test_multiplication_compute():
    calculation = Multiplication(1, 1)
    assert calculation.compute() == 1

def test_division_compute():
    calculation = Division(4, 2)
    assert calculation.compute() == 2

def test_power_compute():
    calculation = Power(2, 2)
    assert calculation.compute() == 4

def test_root_compute():
    calculation = Root(36, 2)
    assert calculation.compute() == 6

def test_modulus_compute():
    calculation = Modulus(13, 3)
    assert calculation.compute() == 1

def test_int_divide():
    calculation = IntegerDivision(10, 3)
    assert calculation.compute() == 3

def test_percent():
    calculation = Percentage(10, 100)
    assert calculation.compute() == 10

def test_absolute_difference_compute():
    calculation = AbsoluteDifference(4, 5)
    assert calculation.compute() == 1

def test_division_by_zero_compute():
    calculation = Division(4, 0)
    with pytest.raises(OperationError, match="Cannot perform division by zero"):
        calculation.compute()

def test_str():
    calculation = Addition(1, 1)
    assert str(calculation) == "Addition(1, 1)"

def test_repr():
    calculation = Addition(1, 1)
    assert repr(calculation) == "Addition(a=1, b=1)"