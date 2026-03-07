import pytest
from app.exceptions import ValidationError
from app.input_validators import validate_input_is_number

def test_validate_input_is_number_with_int_string():
    assert validate_input_is_number("5") == 5.0

def test_validate_input_is_number_with_float_string():
    assert validate_input_is_number("5.55") == 5.55

def test_validate_input_is_number_with_int():
    assert validate_input_is_number(5) == 5.0

def test_validate_input_is_number_with_invalid_string():
    with pytest.raises(ValidationError, match="Invalid number: five"):
        validate_input_is_number("five")