import pytest
from app.exceptions import ValidationError
from app.input_validators import validate_input_is_number, validate_max_input_value, validate_two_valid_inputs

def test_validate_input_is_number_with_int_string():
    assert validate_input_is_number("5") == 5.0

def test_validate_input_is_number_with_float_string():
    assert validate_input_is_number("5.55") == 5.55

def test_validate_input_is_number_with_int():
    assert validate_input_is_number(5) == 5.0

def test_validate_input_is_number_with_invalid_string():
    with pytest.raises(ValidationError, match="Invalid number: five"):
        validate_input_is_number("five")

def test_validate_max_input_value_valid():
    assert validate_max_input_value(100) == 100

def test_validate_max_input_value_negative_valid():
    assert validate_max_input_value(-100) == -100

def test_validate_max_input_value_invalid():
    with pytest.raises(ValidationError):
        validate_max_input_value(2_000_000_000)

def test_validate_max_input_value_negative_invalid():
    with pytest.raises(ValidationError):
        validate_max_input_value(2_000_000_000)

def test_validate_two_valid_inputs():
    a, b = validate_two_valid_inputs("5", "2")
    assert a == 5.0
    assert b == 2.0

def test_validate_two_valid_inputs_invalid():
    with pytest.raises(ValidationError, match="Invalid number: five"):
        validate_two_valid_inputs("five", "2")

def test_validate_two_valid_inputs_max():
    with pytest.raises(ValidationError):
        validate_two_valid_inputs("2000000000", "2")