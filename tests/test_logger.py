import pandas as pd

from app.calculation import CalculationFactory
from app.logger import LoggingObserver, AutoSaveObserver
from app.history import History

def test_logging_observer_stores_log_message():
    observer = LoggingObserver()
    calculation = CalculationFactory.create_calculation("add", 1, 1)

    observer.update(calculation)

    logs = observer.get_logs()

    assert len(logs) == 1
    assert "Logged calculation:" in logs[0]
    assert "Addition" in logs[0]
    assert "1" in logs[0]

def test_autosave_observer_writes_csv(tmp_path):
    history = History()
    file_path = tmp_path / "history.csv"

    observer = AutoSaveObserver(history, str(file_path))
    history.add_observer(observer)

    calculation = CalculationFactory.create_calculation("add", 1, 1)
    history.add_calculation(calculation)

    assert file_path.exists()

    df = pd.read_csv(file_path)

    assert len(df) == 1
    assert df.loc[0, "operation"] == "Addition"
    assert df.loc[0, "operand1"] == 1
    assert df.loc[0, "operand2"] == 1
    assert df.loc[0, "result"] == 2