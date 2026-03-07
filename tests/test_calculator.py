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
    inputs = ["integer divide", "10", "3", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Result: 3.0" in output

def test_percent(monkeypatch):
    inputs = ["percent", "10", "100", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Result: 10.0" in output

def test_abs_diff(monkeypatch):
    inputs = ["absolute difference", "4", "5", "exit"]
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
    inputs = ["integer divide", "10", "0", "exit"]
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
    assert "Please choose from the list of available commands: add, subtract, multiply, divide, power, root, modulus, integer divide, percent, absolute difference." in output

def test_invalid_number(monkeypatch):
    inputs = ["add", "five", "3", "exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Please enter two valid numbers" in output

"""Test Exit"""
def test_exit(monkeypatch):
    inputs = ["exit"]
    output = run_calculator_repl_with_inputs(monkeypatch, inputs)
    assert "Exiting REPL" in output
