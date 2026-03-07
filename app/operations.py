"""Calculations"""
from app.exceptions import OperationError

def add(a: float, b: float) -> float:
    return a + b 

def subtract(a: float, b: float) -> float:
    return a - b 

def multiply(a: float, b: float) -> float:
    return a * b 

def divide(a: float, b: float) -> float:
    if b == 0:
        raise OperationError("Cannot perform division by zero")
    return a / b

def power(a: float, b: float) -> float:
    return a ** b

def root(a: float, b: float) -> float:
    if b == 0:
        raise OperationError("Cannot perform root with degree zero")
    return a ** (1/b)

def modulus(a: float, b: float) -> float:
    if b == 0:
        raise OperationError("Cannot perform modulus by zero")
    return a % b

def int_divide(a: float, b: float) -> float:
    if b == 0:
        raise OperationError("Cannot perform integer division by zero")
    return a // b

def percent(a: float, b: float) -> float:
    if b == 0:
        raise OperationError("Cannot perform division by zero")    
    return (a / b)*100 

def abs_diff(a: float, b: float) -> float:
    return abs(a - b)