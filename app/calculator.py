"""Calulator REPL"""
from app.operations import add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff
from app.exceptions import OperationError, ValidationError
from app.input_validators import validate_input_is_number, validate_max_input_value, validate_two_valid_inputs

def Calculator():
    print("Welcome to the calculator app!")

    while True: 
        user_input = input("Input the command you would like to perform, or type 'exit' to quit: ").lower().strip()

        if user_input== "exit":
            print("Exiting REPL")
            break 
        
        if user_input in ['add', 'subtract', 'multiply', 'divide', 'power', 'root', 'modulus', 'integer divide', 'percent', 'absolute difference']:
            print("Calculator takes two numbers:")
            a = input("First number: ")
            b = input("Second number: ")

            if a.lower() == "exit" or b.lower() == "exit":
                print("Exiting REPL")
                break 
            
            try: 
                a, b = validate_two_valid_inputs(a, b)
                b = validate_input_is_number(b)  

            except ValidationError as e:
                print(f"Error: {e}")
                continue 
            
            try:
                if user_input == 'add':
                    result = add(a, b)
                
                elif user_input == 'subtract':
                    result = subtract(a, b)
                
                elif user_input == 'multiply':
                    result = multiply(a, b)
                
                elif user_input == 'divide':
                    result = divide(a, b)
                
                elif user_input == 'power':
                    result = power(a, b)      
                
                elif user_input == 'root':
                    result = root(a, b) 
                
                elif user_input == 'modulus':
                    result = modulus(a, b)     
                
                elif user_input == 'integer divide':
                    result = int_divide(a, b)     
                
                elif user_input == 'percent':
                    result = percent(a, b)   
                
                elif user_input == 'absolute difference':
                    result = abs_diff(a, b)       
                
                print(f"Result: {result}")
            
            except OperationError as e:
                print(f"Error: {e}")
        
        else:   
            print("Please choose from the list of available commands: add, subtract, multiply, divide, power, root, modulus, integer divide, percent, absolute difference.")

