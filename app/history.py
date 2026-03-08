from app.calculation import Calculation

class History:
    """
    Storage and manage user input history for completed operations
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
    