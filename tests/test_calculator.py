from app.calculator import calculator


#helper funtion

def run_calculator_with_inputs(monkeypatch, inputs, capsys):
    iter_inputs = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(iter_inputs))

    calculator()

    captured = capsys.readouterr()
    return captured.out


def test_addition(monkeypatch,capsys):

    inputs = ['+', '4', '5', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs, capsys)
    assert "Results: 4.0 + 5.0 = 9.0" in output


def test_substraction(monkeypatch,capsys):
    """Test multiplication operation in REPL."""
    inputs = ['-', '8' , '4', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs,capsys)
    assert "Results: 8.0 - 4.0 = 4.0" in output


def test_multiplication(monkeypatch,capsys):
    """Test multiplication operation in REPL."""
    inputs = ['*', '4' , '5', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs,capsys)
    assert "Results: 4.0 * 5.0 = 20.0" in output


def test_division(monkeypatch,capsys):
    """Test division operation in REPL."""
    inputs = ['/', '10' , '2', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs,capsys)
    assert "Results: 10.0 / 2.0 = 5.0" in output


# Negative Tests
def test_invalid_operation(monkeypatch,capsys):
    """Test invalid operation in REPL."""
    inputs = ['add', '5', '3', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs,capsys)
    assert "Invalid operation. Please choose one of the listed options." in output

def test_invalid_num1_format(monkeypatch,capsys):
    """Test invalid input format in REPL."""
    inputs = ['*', 'four' , '5', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs,capsys)
    assert "Invalid input. Please enter a numeric value using digits (e.g., 5 or 3.14)." in output

def test_invalid_num2_format(monkeypatch,capsys):
    """Test invalid input format in REPL."""
    inputs = ['*', '4' , 'five', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs,capsys)
    assert "Invalid input. Please enter a numeric value using digits (e.g., 5 or 3.14)." in output


def test_division_by_zero(monkeypatch,capsys):
    """Test division by zero in REPL."""
    inputs = ['/', '5', '0', "exit"]
    output = run_calculator_with_inputs(monkeypatch, inputs,capsys)
    assert "Division by Zero is not allowed." in output


