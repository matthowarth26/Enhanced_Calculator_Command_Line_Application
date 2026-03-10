# Calculator Repl 

This project implements a modular calculation application that users can interact with via a command-line interface (REPL). The calculator supports a defined set of arithmetic operations, while providing robust error handling. It also includes features such as logging, undo/redo functionality, and auto-saving history and loading from a CSV. 


# Key Features

- REPL Interface
- Design Patterns Integration
   - Observer Pattern
   - Memento Pattern
   - Factory Pattern
- Persistent data management 
- History Management utilizing pandas dataframes
- Auto-Saving and Loading history to CSV files 
- User Commands - help, history, exit, clear, undo, redo, save and load 
- Comprehensive Error handling to manage invalid inputs and exceptions 
- Test automation with GitHub Actions 


# Featured Arithemtic Operations 

- add
- subtract
- multiply
- divide 
- power
- root 
- modulus
- int_divide
- percent 
- abs_diff


# Additional Supported Commands

- history - Show calculation history
- clear - Clear calculation history
- undo - Undo the last calculation
- redo - Redo the last undone calculation
- save - Save calculation history to file
- load - Load calculation history from file
- help - Show help message 
- exit - Exit the calculator


# Project Installation 

Clone the repository 

```git clone <repository-url>
cd <repository-directory>
```

Create and Activate a Virtual Environment 
```python3 -m venv venv
source venv/bin/activate
```

Install Required Packages
```
pip install -r requirements.txt
```

Running the Project
```
python main.py
```
