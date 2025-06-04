import pytest
from app.operations import add


#postive tests for add, subtract, multiple and divide
def test_add_positive():
    """
    The function will test postive casses for add function.
    Assert statement will validate test conditions. If the codition evaluates to True, the test passes, otherwise it fails. 
    """
    assert add(3.0,4.0) == 7.0
    assert add(2,3) == 5.0
    assert add(-1, 2) == 1


