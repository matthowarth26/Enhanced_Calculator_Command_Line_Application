from abc import ABC, abstractmethod
from app.calculation import Calculation

class Observer(ABC):
    """ 
    Abstract base class for calculation obersver
    """

    @abstractmethod
    def update(self, calculation: Calculation) -> None: 
       pass

class LoggingObserver(Observer):
    """
    Observer that logs calculation details 
    """
    def __init__(self) -> None:
        self.logs: list[str] = []

    def update(self, calculation: Calculation) -> None:
        """
        Store log message for new calculation
        """
        log_message = f"Logged calculation: {calculation}"
        self.logs.append(log_message)

    def get_logs(self) -> list[str]:
        """"
        Return all stores log messages
        """
        return self.logs