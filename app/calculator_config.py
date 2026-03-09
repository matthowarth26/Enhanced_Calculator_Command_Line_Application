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
        return os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"

    @staticmethod
    def get_history_file() -> str:
        """
        File path for autosave history CSV
        """
        return os.getenv("CALCULATOR_HISTORY_FILE", "history.csv")

    @staticmethod
    def get_log_file() -> str:
        """
        File path for calculator logs.
        """
        return os.getenv("CALCULATOR_LOG_FILE", "calculator.log")