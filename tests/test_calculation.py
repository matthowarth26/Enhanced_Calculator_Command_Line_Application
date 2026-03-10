import pytest

from app.calculation import Calculation, Addition, Subtraction, Multiplication, Division, Power, Root, Modulus, IntegerDivision, Percentage, AbsoluteDifference, CalculationFactory
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
    assert str(calculation) == "Addition(1, 1) = 2"

def test_repr():
    calculation = Addition(1, 1)
    assert repr(calculation) == "Addition(a=1, b=1)"

def test_calculation_factory_addition():
    calculation = CalculationFactory.create_calculation("add", 1, 1)
    assert calculation.compute() == 2

def test_calculation_factory_subtraction():
    calculation = CalculationFactory.create_calculation("subtract", 1, 1)
    assert calculation.compute() == 0

def test_calculation_factory_multiplication():
    calculation = CalculationFactory.create_calculation("multiply", 1, 1)
    assert calculation.compute() == 1

def test_calculation_factory_division():
    calculation = CalculationFactory.create_calculation("divide", 4, 2)
    assert calculation.compute() == 2

def test_calculation_factory_power():
    calculation = CalculationFactory.create_calculation("power", 2, 2)
    assert calculation.compute() == 4

def test_calculation_factory_root():
    calculation = CalculationFactory.create_calculation("root", 36, 2)
    assert calculation.compute() == 6

def test_calculation_factory_modulus():
    calculation = CalculationFactory.create_calculation("modulus", 13, 3)
    assert calculation.compute() == 1

def test_calculation_factory_int_divide():
    calculation = CalculationFactory.create_calculation("int_divide", 10, 3)
    assert calculation.compute() == 3

def test_calculation_factory_percent():
    calculation = CalculationFactory.create_calculation("percent", 10, 100)
    assert calculation.compute() == 10

def test_calculation_factory_abs_diff():
    calculation = CalculationFactory.create_calculation("abs_diff", 4, 5)
    assert calculation.compute() == 1

def test_calculation_to_dict():
    calculation = CalculationFactory.create_calculation("add", 1, 1)
    result = calculation.to_dict()

    assert result["operation"] == "Addition"
    assert result["operand1"] == 1
    assert result["operand2"] == 1
    assert result["result"] == 2

def test_get_rounded_result(monkeypatch):
    from app import calculator_config

    monkeypatch.setattr(
        calculator_config.CalculatorConfig,
        "get_precision",
        staticmethod(lambda: 2),
    )

    calculation = Division(10, 3)
    assert calculation.get_rounded_result() == 3.33

def test_to_dict_uses_configured_precision(monkeypatch):
    from app import calculator_config

    monkeypatch.setattr(
        calculator_config.CalculatorConfig,
        "get_precision",
        staticmethod(lambda: 2),
    )

    calculation = Division(10, 3)
    result = calculation.to_dict()

    assert result["result"] == 3.33

def test_str_uses_configured_precision(monkeypatch):
    from app import calculator_config

    monkeypatch.setattr(
        calculator_config.CalculatorConfig,
        "get_precision",
        staticmethod(lambda: 2),
    )

    calculation = Division(10, 3)
    assert str(calculation) == "Division(10, 3) = 3.33"