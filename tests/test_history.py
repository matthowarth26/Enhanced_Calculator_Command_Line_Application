from app.calculation import CalculationFactory
from app.history import History

def test_history_list_is_empty():
    history = History()
    assert history.get_history() == []

def test_history_add_one_operation():
    history = History()
    calculation = CalculationFactory.create_calculation("add", 1, 1)

    history.add_calculation(calculation)

    assert len(history.get_history()) == 1
    assert history.get_history()[0] == calculation

def test_history_add_multiple_operations():
    history = History()
    calculation1 = CalculationFactory.create_calculation("add", 1, 1)
    calculation2 = CalculationFactory.create_calculation("subtract", 1, 1)

    history.add_calculation(calculation1)
    history.add_calculation(calculation2)

    assert len(history.get_history()) == 2
    assert history.get_history()[0] == calculation1
    assert history.get_history()[1] == calculation2

def test_history_clear_list():
    history = History()
    calculation1 = CalculationFactory.create_calculation("add", 1, 1)

    history.add_calculation(calculation1)

    history.clear_history()

    assert history.get_history() == []