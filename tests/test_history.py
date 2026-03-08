import pytest
from app.calculation import CalculationFactory
from app.history import History
from app.exceptions import HistoryError

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

def test_history_is_empty_true():
    history = History()
    assert history.is_empty() is True

def test_history_is_empty_fale():
    history = History()
    calculation = CalculationFactory.create_calculation("add", 1, 1)

    history.add_calculation(calculation)

    assert history.is_empty() is False

def test_return_last_calculation():
    history = History()
    calculation1 = CalculationFactory.create_calculation("add", 1, 1)
    calculation2 = CalculationFactory.create_calculation("subtract", 1, 1)

    history.add_calculation(calculation1)
    history.add_calculation(calculation2)

    assert history.return_last_calculation() == calculation2

def test_return_last_calculation_when_empty_error():
    history = History()

    with pytest.raises(HistoryError, match="Calculator history is empty"):
        history.return_last_calculation()

def test_drop_last_calculation():
    history = History()
    calculation1 = CalculationFactory.create_calculation("add", 1, 1)
    calculation2 = CalculationFactory.create_calculation("subtract", 1, 1)

    history.add_calculation(calculation1)
    history.add_calculation(calculation2)

    dropped = history.drop_last_calculation()

    assert dropped == calculation2
    assert len(history.get_history()) == 1
    assert history.return_last_calculation() == calculation1

def test_drop_last_calculation_when_empty_error():
    history = History()

    with pytest.raises(HistoryError, match="Calculator history is empty"):
        history.drop_last_calculation()

def test_undo_operation_move_to_redo_stack():
    history = History()
    calculation1 = CalculationFactory.create_calculation("add", 1, 1)
    calculation2 = CalculationFactory.create_calculation("subtract", 1, 1)

    history.add_calculation(calculation1)
    history.add_calculation(calculation2)

    undone = history.undo()

    assert undone == calculation2
    assert len(history.get_history()) == 1
    assert history.return_last_calculation() == calculation1
    assert history.redo_is_empty() is False

def test_undo_operation_with_empty_history_error():
    history = History()

    with pytest.raises(HistoryError, match="Calculator history is empty - no calculation to undo"):
        history.undo()

def test_redo_returns_last_undone_calculation():
    history = History()
    calculation1 = CalculationFactory.create_calculation("add", 1, 1)

    history.add_calculation(calculation1)
    history.undo()
    redone = history.redo()

    assert redone == calculation1
    assert len(history.get_history()) == 1
    assert history.return_last_calculation() == calculation1

def test_redo_operation_with_empty_redo_stack():
    history = History()

    with pytest.raises(HistoryError, match="No calculations to redo"):
        history.redo()

def test_clear_redo_history_after_new_operation():
    history = History()
    calculation1 = CalculationFactory.create_calculation("add", 1, 1)
    calculation2 = CalculationFactory.create_calculation("subtract", 1, 1)

    history.add_calculation(calculation1)
    history.undo()

    assert history.redo_is_empty() is False

    history.add_calculation(calculation2)

    assert history.redo_is_empty() is True