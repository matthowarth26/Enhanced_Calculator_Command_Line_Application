import pandas as pd 
from datetime import datetime 

from app.calculation import CalculationFactory, Calculation
from app.exceptions import HistoryError
from app.calculator_memento import CalculatorMemento
from app.logger import Observer
from app.calculator_config import CalculatorConfig

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
        self._observers = []

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

        # Enforce max calculations stored in history 
        max_history_size = CalculatorConfig.get_max_history_size()
        if len(self._history) > max_history_size:
                self._history.pop(0)

        self.notify_observers(calculation)
    
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
    
    def add_observer(self, observer) -> None: 
        """
        Add an observer
        """
        self._observers.append(observer)
    
    def notify_observers(self, calculation: Calculation) -> None:
        """
        Notify observers about new calculation
        """
        for observer in self._observers:
            observer.update(calculation)
    
    def to_list_of_dicts(self) -> list[dict]:
        """
        Convert history into a list of dictionaries for saving
        """
        return [calculation.to_dict() for calculation in self._history]
    
    def save_to_csv(self, file_path: str) -> None:
        """
        Save current hsitory to CSV file
        """
        history_rows = self.to_list_of_dicts()
        df = pd.DataFrame(history_rows)
        df.to_csv(file_path, index=False)

    def load_from_csv(self, file_path: str) -> None:
        """
        Load history from CSV file and rebuild calculation objects
        """
        try:
            df = pd.read_csv(file_path)
        except FileNotFoundError as e:
            raise HistoryError(f"History file not found: {file_path}") from e
        except Exception as e:
            raise HistoryError(f"Failed to load history from file: {file_path}") from e

        required_columns = {"operation", "operand1", "operand2"}
        if not required_columns.issubset(df.columns):
            raise HistoryError("CSV file is missing required columns")

        loaded_history = []

        for _, row in df.iterrows():
            operation_name = str(row["operation"]).strip()

            # Convert class-style names back into factory command names
            operation_map = {
                "Addition": "add",
                "Subtraction": "subtract",
                "Multiplication": "multiply",
                "Division": "divide",
                "Power": "power",
                "Root": "root",
                "Modulus": "modulus",
                "IntegerDivision": "int_divide",
                "Percentage": "percent",
                "AbsoluteDifference": "abs_diff",
            }

            if operation_name not in operation_map:
                raise HistoryError(f"Unsupported operation in CSV: {operation_name}")

            timestamp = None 

            if "timestamp" in row and not pd.isna(row["timestamp"]):
                timestamp = datetime.fromisoformat(str(row["timestamp"]))

            calculation = CalculationFactory.create_calculation(
                operation_map[operation_name],
                float(row["operand1"]),
                float(row["operand2"]),
            )
            
            calculation.timestamp = timestamp or datetime.now()
            
            loaded_history.append(calculation)

        self._undo_mementos.append(self.save_to_memento())
        self._history = loaded_history
        self._redo_mementos.clear()        