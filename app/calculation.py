from abc import ABC, abstractmethod
from app.operations import Operation
from app.exceptions import OperationError

# Abstract Class Method for calculations 
class Calculation(ABC):
    
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
    def compute(self):
        return Operation.add(self.a, self.b)

class Subtraction(Calculation):
    def compute(self):
        return Operation.subtract(self.a, self.b)

class Multiplication(Calculation):
    def compute(self):
        return Operation.multiply(self.a, self.b)
    
class Division(Calculation):
    def compute(self):
        return Operation.divide(self.a, self.b)

class Power(Calculation):
    def compute(self):
        return Operation.power(self.a, self.b)
    
class Root(Calculation):
    def compute(self):
        return Operation.root(self.a, self.b)
    
class Modulus(Calculation):
    def compute(self):
        return Operation.modulus(self.a, self.b)
        
class IntegerDivision(Calculation):
    def compute(self):
        return Operation.int_divide(self.a, self.b)
    
class Percentage(Calculation):
    def compute(self):
        return Operation.percent(self.a, self.b)
    
class AbsoluteDifference(Calculation):
    def compute(self):
        return Operation.abs_diff(self.a, self.b)
    
class CalculationFactory:
    """
    Factory class for creating calculation instances
    """

    @staticmethod
    def create_calculation(operation_type: str, a: float, b: float) -> Calculation:
        calculations = {
            "add": Addition,
            "subtract": Subtraction,
            "multiply": Multiplication,
            "divide": Division,
            "power": Power, 
            "root": Root,
            "modulus": Modulus,
            "integer divide": IntegerDivision,
            "percent": Percentage,
            "absolute difference": AbsoluteDifference
        }

        if operation_type not in calculations:
            raise OperationError(f"Invalid operation: {operation_type}")
        
        return calculations[operation_type](a,b)