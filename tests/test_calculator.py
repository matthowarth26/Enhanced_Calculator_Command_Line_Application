"""Test calculator.py"""

import sys
from io import StringIO
from app.calculator import Calculator  
from app.exceptions import OperationError
 
def run_calculator_repl_with_inputs(monkeypatch, inputs):
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    captured_output = StringIO()
    original_stdout = sys.stdout
    sys.stdout = captured_output
    
    try:
        Calculator()
    finally:
        sys.stdout = original_stdout

    return captured_output.getvalue()

def test_add(monkeypatch):
    inputs = ["add", "2", "3", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Result: 5.0" in output

def test_subtract(monkeypatch):
    inputs = ["subtract", "3", "2", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Result: 1.0" in output

def test_multiply(monkeypatch):
    inputs = ["multiply", "3", "2", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Result: 6.0" in output

def test_divide(monkeypatch):
    inputs = ["divide", "9", "3", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Result: 3.0" in output

def test_power(monkeypatch):
    inputs = ["power", "3", "2", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Result: 9.0" in output

def test_root(monkeypatch):
    inputs = ["root", "36", "2", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Result: 6.0" in output

def test_modulus(monkeypatch):
    inputs = ["modulus", "13", "3", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Result: 1.0" in output

def test_int_divide(monkeypatch):
    inputs = ["int_divide", "10", "3", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Result: 3.0" in output

def test_percent(monkeypatch):
    inputs = ["percent", "10", "100", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Result: 10.0" in output

def test_abs_diff(monkeypatch):
    inputs = ["abs_diff", "4", "5", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Result: 1.0" in output

"""Test Exceptions"""
def test_divide_by_zero(monkeypatch):
    inputs = ["divide", "10", "0", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Error: Cannot perform division by zero" in output

def test_root_with_zero(monkeypatch):
    inputs = ["root", "36", "0", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Error: Cannot perform root with degree zero" in output

def test_modulus_with_zero(monkeypatch):
    inputs = ["modulus", "13", "0", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Error: Cannot perform modulus by zero" in output

def test_int_divide_with_zero(monkeypatch):
    inputs = ["int_divide", "10", "0", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Error: Cannot perform integer division by zero" in output

def test_percent_with_zero(monkeypatch):
    inputs = ["percent", "10", "0", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Error: Cannot perform division by zero" in output

"""Test Input Errors"""
def test_invalid_command(monkeypatch):
    inputs = ["square", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Please choose from the list of available commands: add, subtract, multiply, divide, power, root, "
    "modulus, int_divide, percent, abs_diff, history, clear, undo, redo, help, or exit." in output

def test_invalid_number(monkeypatch):
    inputs = ["add", "five", "3", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Error: Invalid number: five" in output

def test_invalid_max_number(monkeypatch):
    inputs = ["add", "2000000000", "3", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Error: 2000000000.0 exceeds maximum allowed value: 1000000000" in output

"""Test Exit"""
def test_exit(monkeypatch):
    inputs = ["exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Exiting REPL" in output

"""Test Help Message"""
def test_help_message(monkeypatch):
    inputs = ["help", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Available commands:" in output
    assert "add" in output
    assert "subtract" in output
    assert "multiply" in output
    assert "divide" in output
    assert "power" in output
    assert "root" in output
    assert "modulus" in output
    assert "int_divide" in output
    assert "percent" in output
    assert "abs_diff" in output 
    assert "history" in output
    assert "clear" in output
    assert "save" in output
    assert "load" in output
    assert "exit" in output
    assert "help" in output

"""Test History"""
def test_history_list_repl_is_empty(monkeypatch):
    inputs = ["history", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Calculator history is empty" in output

def test_history_repl_add_one_operation(monkeypatch):
    inputs = ["add", "1", "1", "history", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Result: 2.0" in output
    assert "Calculator History:" in output
    assert "Addition(1.0, 1.0) = 2.0" in output

def test_history_repl_clear_list(monkeypatch):
    inputs = ["add", "1", "1", "clear", "history", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Calculator history cleared" in output
    assert "Calculator history is empty" in output 

"""Test Undo/Redo Functionality"""
def test_undo_calculation_repl(monkeypatch):
    inputs = ["add", "1", "1", "undo", "history", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Result: 2.0" in output
    assert "Undo" in output
    assert "Calculator history is empty" in output

def test_redo_calculation_repl(monkeypatch):
    inputs = ["add", "1", "1", "undo", "redo", "history", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Undo" in output
    assert "Redo" in output
    assert "Addition(1.0, 1.0) = 2.0" in output

def test_undo_calculation_empty_history_repl(monkeypatch):
    inputs = ["undo", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Error: Calculator history is empty - no calculation to undo" in output

def test_redo_calculation_empty_history_repl(monkeypatch):
    inputs = ["redo", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Error: No calculations to redo" in output

"""Test Save/Load Functionality"""
def test_save_command(monkeypatch, tmp_path):
    test_file = tmp_path / "history.csv"

    from app import calculator_config
    monkeypatch.setattr(
        calculator_config.CalculatorConfig,
        "get_history_file",
        staticmethod(lambda: str(test_file))
    )

    inputs = ["add", "1", "1", "save", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)

    assert f"History saved to {test_file}" in output
    assert test_file.exists()


def test_load_command(monkeypatch, tmp_path):
    test_file = tmp_path / "history.csv"

    from app.history import History
    from app.calculation import CalculationFactory
    from app import calculator_config

    seeded_history = History()
    seeded_history.add_calculation(CalculationFactory.create_calculation("add", 1, 1))
    seeded_history.save_to_csv(str(test_file))

    monkeypatch.setattr(
        calculator_config.CalculatorConfig,
        "get_history_file",
        staticmethod(lambda: str(test_file))
    )

    inputs = ["load", "history", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)

    assert f"History loaded from {test_file}" in output
    assert "Addition(1.0, 1.0) = 2.0" in output