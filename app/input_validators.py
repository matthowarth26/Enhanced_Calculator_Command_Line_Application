from app.exceptions import ValidationError

def validate_input_is_number(value):
    """
    Convert user input to float
    Raise ValidationError exception if input cannot be converted
    """
    try:
        return float(value)
    except (TypeError, ValueError) as e:
        raise ValidationError(f"Invalid number: {value}") from e

def validate_max_input_value(value, max_value=1_000_000_000):
    """
    Validate that user input does not exceed max value
    """
    if abs(value) > max_value:
        raise ValidationError(f"{value} exceeds maximum allowed value: {max_value}")
    
    return value

def validate_two_valid_inputs(a, b):
    """
    Validate that both inputs can be converted to numbers and do not exceed max value
    """
    a = validate_input_is_number(a)
    b = validate_input_is_number(b)

    a = validate_max_input_value(a)
    b = validate_max_input_value(b)

    return a, b