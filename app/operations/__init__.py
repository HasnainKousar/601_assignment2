#operations.py
#write functions for add, subtract, multiply and divide

def add(n1: float, n2: float) -> float:
    """
    The add function will take two float values n1 and n2, and returns their sum (n1 + n2).
    float values means n1 and n2 are supposed to numbers with decimal points, and the result will also be a number with decimal points

    Example: if we call the function add(2.0, 7.0), it will return 9.0. 
    """
    return (n1+n2) #this is the math part where it will add n1 and n2 and return their sum


def subtract(n1: float, n2: float) -> float:
    """
    The subtract function will take two float values n1 and n2, and returns their difference (n1 - n2).
    float values means n1 and n2 are supposed to numbers with decimal points, and the result will also be a number with decimal points

    Example: if we call the function subtract(7.0, 5.0), it will return 2.0. 
    """
    return (n1-n2) #this is the math part where it will subtract n2 from n1 and return the difference


def multiply(n1: float, n2: float) -> float:
    """
    The multiply function will take two float values n1 and n2, and returns their product (n1 * n2).
    float values means n1 and n2 are supposed to numbers with decimal points, and the result will also be a number with decimal points
    
    Example: if we call the function multiply(4.0, 5.0), it will return 20.0. 
    """
    return (n1*n2) #this is the math part where it will multiply n1 with n2 and return the result


def divide(n1: float, n2: float) -> float:
    """
    The divide function will take two float values n1 and n2, and returns their quotient (n1 / n2).
    float values means n1 and n2 are supposed to numbers with decimal points, and the result will also be a number with decimal points. 

    In the case of division, the denominator cannot be zero so the function first checks if n2 == 0. 
    If n2==0, the function will raise a ValueError, it will send the ValueError messege 'Division by zero is not allowed.' and will end the function.
    else it will return the quotient (n1 / n2).

    Example: if we call the function divide(35.0 / 5.0), it will return 7.0.
    If we call the function divide(10,0), it will it will raise a ValueError and say "Division by zero is not allowed."


    """
    if n2 == 0:
        raise ValueError("Division by Zero is not allowed.")

    return (n1/n2) #this is the math part where it will subtract n2 from n1 and return the difference



