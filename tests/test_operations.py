import pytest
from app.operations import add, subtract, multiply, divide


#postive tests for add, subtract, multiple and divide
def test_add_positive():
    """
    The function will test postive casses for add function.
    Assert statement will validate test conditions. If the codition evaluates to True, the test passes, otherwise it fails. 
    """
    assert add(3.0,4.0) == 7.0
    assert add(2,3) == 5.0
    assert add(-1, 2) == 1


def test_subtract_positive():
    """
    The function will test postive casses for the subtract function.
    Assert statement will validate test conditions. If the codition evaluates to True, the test passes, otherwise it fails. 
    """
    assert subtract(8, 4) == 4.0
    assert subtract(9.0, 3.0) == 6.0
    assert subtract(2, -6) == 8.0   



def test_multiply_positive():
    """
    The function will test postive casses for the multiply function.
    Assert statement will validate test conditions. If the codition evaluates to True, the test passes, otherwise it fails. 
    """
    assert multiply(3, 4) == 12.0
    assert multiply(5.0, 3.0) == 15.0
    assert multiply(-4, -3) == 12.0   



def test_divide_positive():
    """
    The function will test postive casses for divide function.
    Assert statement will validate test conditions. If the codition evaluates to True, the test passes, otherwise it fails. 
    """
    assert divide(8, 4) == 2.0
    assert divide(9.0, 3.0) == 3.0
    assert divide(-12, -3) == 4.0  


