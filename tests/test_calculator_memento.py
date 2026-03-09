from app.calculation import CalculationFactory
from app.calculator_memento import CalculatorMemento

def test_memento_stores_history_snapshot():
    calculation1 = CalculationFactory.create_calculation("add", 1, 1)
    calculation2 = CalculationFactory.create_calculation("subtract", 1, 1)

    history_snapshot = [calculation1, calculation2]
    memento = CalculatorMemento(history_snapshot)

    saved_state = memento.return_saved_state()

    assert saved_state == history_snapshot
    assert saved_state is not history_snapshot

def test_memento_returns_copy_of_saved_state():
    calculation1 = CalculationFactory.create_calculation("add", 1, 1)

    history_snapshot = [calculation1]
    memento = CalculatorMemento(history_snapshot)
    
    saved_state = memento.return_saved_state()
    saved_state.append(CalculationFactory.create_calculation("subtract", 1, 1))

    assert len(memento.return_saved_state()) == 1
