"""Exceptions for Calculator"""

class CalculatorError(Exception):
    """Base exceptions for calculator errors"""
    pass

class OperationError(CalculatorError):
    """ExcpExceptionetion raised when calculation operation failure"""
    pass

class ValidationError(CalculatorError):
    """Exception raised when user input is invalid """
    pass