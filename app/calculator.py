"""Calulator REPL"""
from app.calculation import CalculationFactory
from app.exceptions import OperationError, ValidationError
from app.input_validators import validate_two_valid_inputs
from app.history import History

def display_help() -> None:
    """ 
    Display help menu for Calculator REPL
    """
    # List of possible operations 
    operation_list = CalculationFactory.get_supported_operations()

    print("\nAvailable commands:")
    for operation in operation_list:
        print(f" - {operation}")

    print(" - history")
    print(" - clear")
    print(" - help")
    print(" - exit")
    
def Calculator():
    """
    Calculator REPL for user to input operation and 2 numbers
    """
    print("Welcome to the calculator app!")

    # List of possible operations 
    operation_list = CalculationFactory.get_supported_operations()

    # Instantiate history list
    history_list = History()

    # Start Loop 
    while True: 
        user_input = input("Input the operation you would like to perform, type 'help' for operation list, "
        "or type 'exit' to quit: ").lower().strip()

        # Check if user inputs exit 
        if user_input == "exit":
            print("Exiting REPL")
            break 
        
        # Check if user inputs help 
        if user_input == "help":
            display_help()
            continue
        
        if user_input == "history":
            calculator_history = history_list.get_history()

            if not calculator_history:
                print("Calculator history is empty")
            else:
                print("Calculator History:")
                for calculation in calculator_history:
                    print(calculation)
            
            continue 
        
        if user_input == 'clear':
            history_list.clear_history()
            print("Calculator history cleared")
            continue 

        # Check if user inputs an invalid operation 
        if user_input not in operation_list:
            print("Please choose from the list of available commands: " 
                  + ", ".join(operation_list)+", help, or exit.")
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
            history_list.add_calculation(calculation) # Save operation in history list  
            print(f"Result: {result}")
            
        except (ValidationError, OperationError) as e:
            print(f"Error: {e}")