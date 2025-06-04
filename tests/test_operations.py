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



#negative tests for add, subtract, multiply and divide functions
def test_add_negative():
    """
    The function will test postive casses for add function.
    Assert statement will validate test conditions. If the codition evaluates to True, the test passes, otherwise it fails. 
    """
    assert add(3.0,-4.0) == -1.0
    assert add(2,-7) == -5.0
    assert add(-1, -5) == -6.0



def test_subtract_negative():
    """
    The function will test postive casses for the subtract function.
    Assert statement will validate test conditions. If the codition evaluates to True, the test passes, otherwise it fails. 
    """
    assert subtract(4, 8) == -4.0
    assert subtract(3, 6.0) == -3.0
    assert subtract(-6, -2) == -4.0   



def test_multiply_negative():
    """
    The function will test postive casses for the multiply function.
    Assert statement will validate test conditions. If the codition evaluates to True, the test passes, otherwise it fails. 
    """
    assert multiply(3, -6) == -18.0
    assert multiply(-5.0, 2.0) == -10.0
    assert multiply(-4, 4) == -16.0   



def test_divide_negative():
    """
    The function will test postive casses for divide function.
    Assert statement will validate test conditions. If the codition evaluates to True, the test passes, otherwise it fails. 
    """
    assert divide(8, -4) == -2.0
    assert divide(9.0, -3.0) == -3.0
    assert divide(-12, 3) == -4.0  


# Test for divide function in the case of division by zero
def test_divide_by_zero():
    """
    Test that the divide function raises a ValueError when attempting 
    to divide by zero.

    This test verifies that dividing by zero correctly triggers a 
    ValueError with the expected error message.
    """
    with pytest.raises(ValueError, match="Division by Zero is not allowed."):
        divide(10, 0)



