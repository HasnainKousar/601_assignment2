"""
File for the 'app/calulator.py. 
A simple calculator application that performs basic arithmetic operations:
addition, subtraction, multiplication, and division. It uses functions
from the 'app/operations.py' module to execute these operations based on
user input.

"""

# first we need to import the add, subtract, multiply and divide function from app.operations. 
# The calculator function will use these to do math such as adding, subtracting, multiplying and dividing numbers based on user input
from app.operations import add, subtract, multiply, divide

def calculator():
    """Basic REPL calculator that performs addition, subtraction,
    multiplication, and division based on user input."""

    # Welcome message and instructions for exiting the application
    print("Welcome to the calculator app! Type 'exit' to quit.")


    # Continuously prompt the user for input until 'exit' is entered
    while True:
    
        # Display available operations to the user
        print("Type '+' to add, '-' to subtract, '*' to multiply, '/' to divide, or 'exit' to quit.")

        # prompt user to select an operation
        operation = input("Pick an operation: ")

        # Exit the application if user types 'exit'
        if operation == 'exit':
            print("Exiting the app...")
            return False
        
        # check if user selected the correct operation
        if operation not in ["+","-","*","/"]:

            # print an error message if user types an incorrect operation
            print("Invalid operation. Please choose one of the listed options.\n")
            continue


        try:

            # Prompt the user to enter the first number
            n1 = float(input("Enter the first number (use digits, e.g., 5 or 3.14): "))

            # Prompt the user to enter the second number
            n2 = float(input("Enter the second number (use digits, e.g., 5 or 3.14): "))

            # Perform the selected operation (add, subtract, multiply or divide)
            if operation =="+":
                result = add(n1,n2)
    
            elif operation =="-":
                result = subtract(n1,n2)
    
            elif operation =="*":
                result = multiply(n1,n2)
    
            else: #operation =="/":
                try:
                    result = divide(n1,n2)

                # handle division error by zero
                except ValueError as e:
                    print(e)
                    print('\n')
                    continue
            #display the results of the operation. 
            print(f'Results: {n1} {operation} {n2} = {result}\n')

        # Handle invalid input for first and second number. (example if user types 'five' instead '5') 
        except ValueError:
            # If the user doesn't type something correctly, like typing letters where numbers should be, we show an 'invalid input 'error.
            print("Invalid input. Please enter a numeric value using digits (e.g., 5 or 3.14).\n")
            continue
    


