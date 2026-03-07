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