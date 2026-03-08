from app.calculation import Calculation
from app.exceptions import HistoryError

class History:
    """
    Store and manage user input history for completed operations
    """

    def __init__(self) -> None:
        """
        Initialize a list to store history of operations
        """
        self._history: list[Calculation] = []

    def add_calculation(self, calculation: Calculation) -> None:
        """
        Add an operation object to history list
        """
        self._history.append(calculation)
    
    def get_history(self) -> list[Calculation]:
        """
        Return full operation history as list 
        """
        return self._history
    
    def clear_history(self) -> None:
        """
        Clear all operations from history list
        """
        self._history.clear()
    
    def is_empty(self) -> bool:
        """
        Check if history list is empty - return true if empty, else false
        """
        return len(self._history) == 0
    
    def return_last_calculation(self) -> Calculation: 
        """
        Return most recent operation 
        """
        if self.is_empty():
            raise HistoryError("Calculator history is empty")
        return self._history[-1]

    def drop_last_calculation(self) -> Calculation:
        if self.is_empty():
            raise HistoryError("Calculator history is empty")
        return self._history.pop()