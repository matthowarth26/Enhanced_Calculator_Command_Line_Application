from app.calculation import CalculationFactory
from app.logger import LoggingObserver

def test_logging_observer_stores_log_message():
    observer = LoggingObserver()
    calculation = CalculationFactory.create_calculation("add", 1, 1)

    observer.update(calculation)

    logs = observer.get_logs()

    assert len(logs) == 1
    assert "Logged calculation:" in logs[0]
    assert "Addition" in logs[0]
    assert "1" in logs[0]