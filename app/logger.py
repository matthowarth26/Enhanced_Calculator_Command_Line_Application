from abc import ABC, abstractmethod
import pandas as pd 
import logging
import os

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
       pass # pragma: no cover

class LoggingObserver(Observer):
    """
    Observer that logs calculation details.
    """
    def __init__(self, log_file: str | None = None) -> None:
        self.logs: list[str] = []

        if log_file is None:
            log_dir = CalculatorConfig.get_log_dir()
            CalculatorConfig.ensure_directory(log_dir)
            log_file = os.path.join(log_dir, CalculatorConfig.get_log_file())

        self.log_file = log_file

        self.logger = logging.getLogger(f"calculator_logger_{self.log_file}")
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            encoding = CalculatorConfig.get_default_encoding()
            file_handler = logging.FileHandler(self.log_file, encoding=encoding)
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def update(self, calculation: Calculation) -> None:
        """
        Store log message for new calculation.
        """
        log_message = f"Logged calculation: {calculation}"
        self.logs.append(log_message)
        self.logger.info(log_message)

    def get_logs(self) -> list[str]:
        return self.logs


class AutoSaveObserver(Observer):
    """
    Observer that saves history to CSV file.
    """

    def __init__(self, history, file_path: str | None = None) -> None:
        self.history = history

        if file_path is None:
            history_dir = CalculatorConfig.get_history_dir()
            CalculatorConfig.ensure_directory(history_dir)
            file_path = os.path.join(
                history_dir,
                CalculatorConfig.get_history_file(),
            )

        self.file_path = file_path

    def update(self, calculation: Calculation) -> None:
        """
        Save current history to CSV after new calculation is added.
        """
        history_rows = self.history.to_list_of_dicts()
        df = pd.DataFrame(history_rows)

        encoding = CalculatorConfig.get_default_encoding()
        df.to_csv(self.file_path, index=False, encoding=encoding)