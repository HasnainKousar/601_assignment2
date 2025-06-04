from app.operations import add, subtract, multiply, divide

def calculator():
    print("Welcome to the calculator app! Type 'exit' to quit.")
    while True:
    
        print("Type '+' to add, '-' to subtract, '*' to multiply, '/' to divide, or 'exit' to quit.")
        operation = input("Pick an operation: ")

        if operation == 'exit':
            print("Exiting the app...")
            return False
        
        if operation not in ["+","-","*","/"]:
            print("Invalid operation. Please choose one of the listed options.\n")
            continue


        try:
            n1 = float(input("Enter the first number (use digits, e.g., 5 or 3.14): "))
            n2 = float(input("Enter the second number (use digits, e.g., 5 or 3.14): "))

   
            if operation =="+":
                result = add(n1,n2)
    
    
            elif operation =="-":
                result = subtract(n1,n2)
    
    
            elif operation =="*":
                result = multiply(n1,n2)
    
    
            else: #operation =="/":
                try:
                    result = divide(n1,n2)
                    #return result
                except ValueError as e:
                    print(e)
                    print('\n')
                    continue
            print(f'Results: {n1} {operation} {n2} = {result}\n')
        except ValueError:
            print("Invalid input. Please enter a numeric value using digits (e.g., 5 or 3.14).\n")
            continue
    


    