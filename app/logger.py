from abc import ABC, abstractmethod
import pandas as pd 
import logging

from app.calculation import Calculation
from app.calculator_config import CalculatorConfig

class Observer(ABC):
    """ 
    Abstract base class for calculation obersver
    """

    @abstractmethod
    def update(self, calculation: Calculation) -> None: 
       """"
       Respond to a new calculation event
       """
       pass

class LoggingObserver(Observer):
    """
    Observer that logs calculation details 
    """
    def __init__(self, log_file: str | None = None) -> None:
        self.log_file = log_file or CalculatorConfig.get_log_file()
        self.logs: list[str] = []

        self.logger = logging.getLogger(f"calculator_logger_{self.log_file}")
        self.logger.setLevel(logging.INFO)

        self.logger = logging.getLogger(f"calculator_logger_{self.log_file}")
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            file_handler = logging.FileHandler(self.log_file)
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def update(self, calculation: Calculation) -> None:
        """
        Store log message for new calculation
        """
        log_message = f"Logged calculation: {calculation}"
        self.logs.append(log_message)
        self.logger.info(log_message)

    def get_logs(self) -> list[str]:
        return self.logs
       
class AutoSaveObserver(Observer):
    """
    Observer that saves history to CSV file
    """

    def __init__(self, history, file_path: str | None = None):
        self.history = history
        self.file_path = file_path or CalculatorConfig.get_history_file()

    def update(self, calculation: Calculation) -> None:
        """
        Save current history to CSV after new calculation is added
        """
        history_rows = self.history.to_list_of_dicts()
        df = pd.DataFrame(history_rows)
        df.to_csv(self.file_path, index=False)