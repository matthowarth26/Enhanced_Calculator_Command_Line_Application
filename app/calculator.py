"""Calulator REPL"""
from app.calculation import add, subtract, multiply, divide

def calculator():
    print("Welcome to the calculator app!")

    while True: 
        user_input = input("Input the command you would like to perform, or type 'exit' to quit: ").lower().strip()

        if user_input== "exit":
            print("Exiting REPL")
            break 
        
        if user_input in ['add', 'subtract', 'multiply', 'divide']:
            print("Calculator takes two numbers:")
            a = input("First number: ")
            b = input("Second number: ")

            if a.lower() == "exit" or b.lower() == "exit":
                print("Exiting REPL")
                break 
            elif user_input == 'add':
                a = float(a)
                b = float(b) 
                result = add(a, b)
            elif user_input == 'subtract':
                a = float(a)
                b = float(b) 
                result = subtract(a, b)
            elif user_input == 'multiply':
                a = float(a)
                b = float(b) 
                result = multiply(a, b)
            elif user_input == 'divide':
                a = float(a)
                b = float(b) 
                try:
                    result = divide(a, b)
                except ValueError as e:
                    print(e)
                    continue
            print(f"Result: {result}")
        else:   
            print("Please choose from the list of available commands: add, subtract, multiply, divide.")

