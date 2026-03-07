"""Calculations"""
import math

def add(a: float, b: float) -> float:
    return a + b 

def subtract(a: float, b: float) -> float:
    return a - b 

def multiply(a: float, b: float) -> float:
    return a * b 

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a: float, b: float) -> float:
    return a ** b

def root(a: float, b: float) -> float:
    return a ** (1/b)

def modulus(a: float, b: float) -> float:
    return a % b

def int_divide(a: float, b: float) -> float:
    return a // b

def percent(a: float, b: float) -> float:
    return (a / b)*100 

def abs_diff(a: float, b: float) -> float:
    return abs(a - b)