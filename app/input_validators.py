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
