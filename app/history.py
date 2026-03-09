from app.calculation import Calculation
from app.exceptions import HistoryError
from app.calculator_memento import CalculatorMemento

class History:
    """
    Store and manage user input history for completed operations
    """

    def __init__(self) -> None:
        """
        Initialize a list to store history of operations
        """
        self._history: list[Calculation] = []
        self._undo_mementos: list[Calculation] = [] 
        self._redo_mementos: list[Calculation] = []

    def save_to_memento(self) -> CalculatorMemento:
        """
        Save current history snapshot to memento
        """
        return CalculatorMemento(self._history)
    
    def restore_from_memento(self, memento: CalculatorMemento) -> None:
        """"
        Restor history snapshot from memento
        """
        self._history = memento.return_saved_state()

    def add_calculation(self, calculation: Calculation) -> None:
        """
        Add an operation object to history list & save current state 
        """
        self._undo_mementos.append(self.save_to_memento())
        self._history.append(calculation)
        self._redo_mementos.clear()
    
    def get_history(self) -> list[Calculation]:
        """
        Return full operation history as list 
        """
        return self._history
    
    def clear_history(self) -> None:
        """
        Clear all operations from history list & save current state 
        """
        self._undo_mementos.append(self.save_to_memento())
        self._history.clear()
        self._redo_mementos.clear()
    
    def is_empty(self) -> bool:
        """
        Check if history list is empty
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
        Remove most recent operation & save current state  
        """
        if self.is_empty():
            raise HistoryError("Calculator history is empty")
        self._undo_mementos.append(self.save_to_memento())
        self._redo_mementos.clear()        
        return self._history.pop()
        
    def undo(self) -> None:
        """"
        Restore previous saved history state from memento snapshots 
        """
        if not self._undo_mementos:
                raise HistoryError("Calculator history is empty - no calculation to undo")
        
        self._redo_mementos.append(self.save_to_memento()) # Move to redo memento 
        previous_state = self._undo_mementos.pop() # Remove from undo memento
        self.restore_from_memento(previous_state)
    
    def redo(self) -> None:
        """"
        Restore next saved history state from memento snapshots
        """
        if not self._redo_mementos:
            raise HistoryError("No calculations to redo")
        
        self._undo_mementos.append(self.save_to_memento()) # Move to undo memento
        next_state = self._redo_mementos.pop() # Remove from redo memento 
        self.restore_from_memento(next_state)
    
    def redo_is_empty(self) -> bool: 
        """
        Check if redo stack is empty
        """
        return len(self._redo_mementos) == 0