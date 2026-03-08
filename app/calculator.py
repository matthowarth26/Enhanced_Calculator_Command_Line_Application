"""Calulator REPL"""
from app.calculation import CalculationFactory
from app.exceptions import OperationError, ValidationError
from app.input_validators import validate_two_valid_inputs

def Calculator():
    """
    Calculator REPL for user to input operation and 2 numbers
    """
    print("Welcome to the calculator app!")

    # List of possible operations 
    operation_list = CalculationFactory.get_supported_operations()

    # Start Loop 
    while True: 
        user_input = input("Input the operation you would like to perform, or type 'exit' to quit: ").lower().strip()

        # Check if user inputs exit 
        if user_input== "exit":
            print("Exiting REPL")
            break 
        
        # Check if user inputs one of the possible operations 
        if user_input not in operation_list:
            print("Please choose from the list of available commands: " + ", ".join(operation_list)+".")
            continue 
        
        print("Calculator takes two numbers:")
            
        # Prompt user to input both numbers 
        a = input("First number: ")
        b = input("Second number: ")

        # Check if user tries to exit 
        if a.lower() == "exit" or b.lower() == "exit":
            print("Exiting REPL")
            break 
            
        # Validate that both inputs are valid numbers and do not exceed max limit 
        try: 
            a, b = validate_two_valid_inputs(a, b)
            calculation = CalculationFactory.create_calculation(user_input, a, b) # Use CalculationFactory method for inputted operation  
            result = calculation.compute()
            print(f"Result: {result}")
            
        except (ValidationError, OperationError) as e:
            print(f"Error: {e}")