"""
Tests for the calculator application.

This module contains tests for the calculator application,
it will tests for correct operations and error handling scenarios. 
"""
from app.calculator import calculator


#helper funtion
def run_calculator_with_inputs(monkeypatch, inputs, capsys):

    """
    Simulate user input for the calculator REPL and capture its output.

    Parameters:
    - monkeypatch: Pytest fixture to mock input().
    - inputs (list): A list of strings representing user inputs.
    - capsys: Pytest fixture to capture stdout and stderr.

    Returns captured output from the calculator function
    """
    iter_inputs = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(iter_inputs))

    calculator()

    captured = capsys.readouterr()
    return captured.out

#Test addition operation in the calculator REPL.
def test_addition(monkeypatch,capsys):
 
    inputs = ['+', '4', '5', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs, capsys)
    assert "Results: 4.0 + 5.0 = 9.0" in output

#Test subtract operation in the calculator REPL.
def test_substraction(monkeypatch,capsys):
    """Test multiplication operation in REPL."""
    inputs = ['-', '8' , '4', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs,capsys)
    assert "Results: 8.0 - 4.0 = 4.0" in output

#Test multiplication operation in the calculator REPL.
def test_multiplication(monkeypatch,capsys):
    """Test multiplication operation in REPL."""
    inputs = ['*', '4' , '5', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs,capsys)
    assert "Results: 4.0 * 5.0 = 20.0" in output

#Test division operation in the calculator REPL.
def test_division(monkeypatch,capsys):
    """Test division operation in REPL."""
    inputs = ['/', '10' , '2', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs,capsys)
    assert "Results: 10.0 / 2.0 = 5.0" in output


#Test handling of invalid operation in the calculator REPL.
def test_invalid_operation(monkeypatch,capsys):
    """Test invalid operation in REPL."""
    inputs = ['add', '5', '3', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs,capsys)
    assert "Invalid operation. Please choose one of the listed options." in output

#Test handling of non-numeric input for the first number in the calculator REPL.
def test_invalid_num1_format(monkeypatch,capsys):
    """Test invalid input format in REPL."""
    inputs = ['*', 'four' , '5', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs,capsys)
    assert "Invalid input. Please enter a numeric value using digits (e.g., 5 or 3.14)." in output

#Test handling of non-numeric input for the second number in the calculator REPL.
def test_invalid_num2_format(monkeypatch,capsys):
    """Test invalid input format in REPL."""
    inputs = ['*', '4' , 'five', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs,capsys)
    assert "Invalid input. Please enter a numeric value using digits (e.g., 5 or 3.14)." in output

#Test handling of division by zero
def test_division_by_zero(monkeypatch,capsys):
    """Test division by zero in REPL."""
    inputs = ['/', '5', '0', "exit"]
    output = run_calculator_with_inputs(monkeypatch, inputs,capsys)
    assert "Division by Zero is not allowed." in output


