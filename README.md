# Calculator Application

## Overview

This is a simple command-line calculator application implemented in Python. It performs basic arithmetic operations: addition, subtraction, multiplication, division, and modulo. The application uses a `Calculator` class to handle these operations and provides an interactive menu for users to select the desired operation.

## Features

- **Addition**: Adds two numbers.
- **Subtraction**: Subtracts the second number from the first number.
- **Multiplication**: Multiplies two numbers.
- **Division**: Divides the first number by the second number, with error handling for division by zero.
- **Modulo**: Computes the remainder of the division of the first number by the second number, with error handling for division by zero.

## Usage

1. **Run the application**:
   ```bash
   python calculator.py
   Select an operation:

2. **Select an operation**:
    ```bash
    Enter `1` for addition.
    Enter `2` for subtraction.
    Enter `3` for multiplication.
    Enter `4` for division.
    Enter `5` for modulo.
    Enter `6` to exit the application.
    Input numbers:

3. **Input numbers**:
After selecting an operation, input the first and second numbers as prompted.
Receive result:

4. **Receive result**:
The application will display the result of the selected operation.

## Ejemplo
    --> Enter 1 to add 
    --> Enter 2 to subtract 
    --> Enter 3 to multiply 
    --> Enter 4 to divide 
    --> Enter 5 to mod 
    --> Enter 6 to exit 
    1
    Enter the first number: 10
    Enter the second number: 5
    The addition between 10.0 and 5.0 is 15.0

## Error Handling

Division by Zero: The application raises an exception if a division or modulo operation is attempted with zero as the divisor. The error message displayed is "Oops! Divide by zero."

## Code Structure
*`Calculator` class*: Contains methods for addition, subtraction, multiplication, division, and modulo operations. It also includes error handling for division by zero.

- **`__init__(self, num1, num2)`**: Initializes the calculator with two numbers.
- **`add(self)`**: Returns the sum of `num1` and `num2`.
- **`substract(self)`**: Returns the difference between `num1` and `num2`.
- **`multiply(self)`**: Returns the product of `num1` and `num2`.
- **`divide(self)`**: Returns the quotient of `num1` divided by `num2`, or raises an exception if `num2` is zero.
- **`mod(self)`**: Returns the remainder of `num1` divided by `num2`, or raises an exception if `num2` is zero.