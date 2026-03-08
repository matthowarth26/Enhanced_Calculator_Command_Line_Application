from abc import ABC, abstractmethod
from app.operations import Operation
from app.exceptions import OperationError


class Calculation(ABC):
    """Abstract base class for calculation operations"""

    def __init__(self, a: float, b: float) -> None:
        self.a = a 
        self.b = b

    @abstractmethod
    def compute(self) -> float:
        pass 

    def __str__(self):
        return f"{self.__class__.__name__}({self.a}, {self.b})"

    def __repr__(self):
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"

# Calculation Factory 
class Addition(Calculation):
    def compute(self) -> float:
        return Operation.add(self.a, self.b)

class Subtraction(Calculation):
    def compute(self) -> float:
        return Operation.subtract(self.a, self.b)

class Multiplication(Calculation):
    def compute(self) -> float:
        return Operation.multiply(self.a, self.b)
    
class Division(Calculation):
    def compute(self) -> float:
        return Operation.divide(self.a, self.b)

class Power(Calculation):
    def compute(self) -> float:
        return Operation.power(self.a, self.b)
    
class Root(Calculation):
    def compute(self) -> float:
        return Operation.root(self.a, self.b)
    
class Modulus(Calculation):
    def compute(self) -> float:
        return Operation.modulus(self.a, self.b)
        
class IntegerDivision(Calculation):
    def compute(self) -> float:
        return Operation.int_divide(self.a, self.b)
    
class Percentage(Calculation):
    def compute(self) -> float:
        return Operation.percent(self.a, self.b)
    
class AbsoluteDifference(Calculation):
    def compute(self) -> float:
        return Operation.abs_diff(self.a, self.b)
    
class CalculationFactory:
    """
    Factory class for creating calculation instances
    """
    _calculations = {
        "add": Addition,
        "subtract": Subtraction,
        "multiply": Multiplication,
        "divide": Division,
        "power": Power,
        "root": Root,
        "modulus": Modulus,
        "integer divide": IntegerDivision,
        "percent": Percentage,
        "absolute difference": AbsoluteDifference,
    }

    @classmethod
    def create_calculation(cls, operation_type: str, a: float, b: float) -> Calculation:
        operation_type = operation_type.lower().strip()

        if operation_type not in cls._calculations:
            raise OperationError(f"Invalid operation: {operation_type}")

        return cls._calculations[operation_type](a, b)

    @classmethod
    def get_supported_operations(cls) -> list[str]:
        return list(cls._calculations.keys())