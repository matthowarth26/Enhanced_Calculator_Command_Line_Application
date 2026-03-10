import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()


class CalculatorConfig:
    """
    Config manager for calculator settings.
    """

    @staticmethod
    def get_max_input_value() -> float:
        """
        Max allowed input value 
        """
        return float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", "1000000000"))

    @staticmethod
    def get_auto_save() -> bool:
        """
        Check autosave observer is enabled 
        """
        return os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true" # pragma: no cover

    @staticmethod
    def get_history_file() -> str:
        """
        File path for autosave history CSV
        """
        return os.getenv("CALCULATOR_HISTORY_DIR", "history.csv")

    @staticmethod
    def get_log_file() -> str:
        """
        File path for calculator logs
        """
        return os.getenv("CALCULATOR_LOG_DIR", "calculator.log")

    @staticmethod
    def get_max_history_size() -> int:
        """
        Max calculations stored in history
        """
        return int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "100"))

    @staticmethod
    def get_precision() -> int:
        """
        Number of decimal places for calculation results
        """
        return int(os.getenv("CALCULATOR_PRECISION", "6"))