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
        self._redo_stack: list[Calculation] = []

    def add_calculation(self, calculation: Calculation) -> None:
        """
        Add an operation object to history list
        """
        self._history.append(calculation)
        self._redo_stack.clear()
    
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
        self._redo_stack.clear()
    
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
        """
        Remove most recent operation 
        """
        if self.is_empty():
            raise HistoryError("Calculator history is empty")
        return self._history.pop()
    
    def undo(self) -> Calculation:
        """"
        Undo most recent operation by moving it to the redo stack 
        """
        if self.is_empty():
            raise HistoryError("Calculator history is empty - no calculation to undo")
        
        calculation = self._history.pop()
        self._redo_stack.append(calculation)
        return calculation
    
    def redo(self) -> Calculation:
        """"
        Redo the most recently undone operation by moving it back to the history list
        """
        if not self._redo_stack:
            raise HistoryError("No calculations to redo")
        
        calculation = self._redo_stack.pop()
        self._history.append(calculation)
        return calculation
    
    def redo_is_empty(self) -> bool: 
        """
        Check if redo stack is empty
        """
        return len(self._redo_stack) == 0