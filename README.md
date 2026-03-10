# Calculator Repl 

This project implements a modular calculation application that users can interact with via a command-line interface (REPL). The calculator supports a defined set of arithmetic operations, while providing robust error handling. It also includes features such as logging, undo/redo functionality, and auto-saving history and loading from a CSV. 


# Key Features

- REPL Interface
- Design Patterns Integration
   - Observer Pattern
   - Memento Pattern
   - Factory Pattern
- Persistent data management 
- History management utilizing pandas dataframes
- Autosaving and loading history to CSV files 
- User commands - help, history, exit, clear, undo, redo, save and load 
- Comprehensive Error handling to manage invalid inputs and exceptions 
- Test automation with GitHub Actions 


# Featured Arithemtic Operations 

Prompt the command-line interface with one of the supported arithmetic operations below. When prompted, input the first number followed by the second number to perform the operation. 
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

For additional support or history operations, prompt the command-line interface with one of the following commands:
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

# Configuration Setup

Python-dotenv is used to load configuration values from a .env file. 

Sample .env file:
```
CALCULATOR_MAX_INPUT_VALUE=1000000000
CALCULATOR_AUTO_SAVE=true
CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_PRECISION=2
CALCULATOR_DEFAULT_ENCODING=utf-8
CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=data
CALCULATOR_HISTORY_FILE=history.csv
CALCULATOR_LOG_FILE=calculator.log
```

# Running Unit and Coverage Tests

Run unit tests with pytest:
```
pytest
```

Run coverage tests with pytest: 
```
pytest --cov=app
```

# CI/CD Information:

GitHub actions is configured to automatically run unit and coverage tests on all push and pull requests. 

GitHub Actions Workflow:
 - Checkout code using `actions/checkout`
 - Set up Python environment using `actions/setup-python`
 - Install dependencies from `requirements.txt`
 - Run tests by executing `pytest`
 - Measure test coverage using `pytest-cov`
 - Ensure CI pipeline fails if test coverage falls below (90%)

Configuration File:
```
.github/workflows/python-app.yml
```