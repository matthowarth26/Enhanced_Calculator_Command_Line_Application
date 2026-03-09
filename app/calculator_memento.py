"""
Calculator Memento
"""
from app.calculation import Calculation

class CalculatorMemento():
    """
    Store a snapshot of calculator history
    """

    def __init__(self, history_state: list[Calculation]) -> None:
        """"
        Save a copy of the history state
        """
        self._history_state = history_state.copy()
    
    def return_saved_state(self) -> list[Calculation]:
        """
        Return the saved history state
        """
        return self._history_state.copy()