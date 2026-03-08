"""Operations"""
from app.exceptions import OperationError

class Operation:

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b 

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b 

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b 

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot perform division by zero")
        return a / b

    @staticmethod
    def power(a: float, b: float) -> float:
        return a ** b

    @staticmethod
    def root(a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot perform root with degree zero")
        if a < 0:
            raise OperationError("Cannot perform root with negative number")
        return a ** (1/b)

    @staticmethod
    def modulus(a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot perform modulus by zero")
        return a % b

    @staticmethod
    def int_divide(a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot perform integer division by zero")
        return a // b

    @staticmethod
    def percent(a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot perform division by zero")    
        return (a / b)*100 

    @staticmethod
    def abs_diff(a: float, b: float) -> float:
        return abs(a - b)