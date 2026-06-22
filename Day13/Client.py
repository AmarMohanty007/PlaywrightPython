"""
Day 13 - Modules: Client Module
Demonstrates basic module functions that perform arithmetic operations.
This module serves as a utility module that can be imported by other Python files.
This module covers:
- Creating reusable functions
- Module composition and imports
- Function organization in separate files
- Using modules to organize code
"""

# Helper function that adds adata driven.
def add(a, b):
    """
    Add two numbers and print the result.

    Args:
        a: First number
        b: Second number

    Output:
        Prints the sum of a and b
    """
    print(a + b)


# Helper function that multiplies mul.
def mul(a, b):
    """
    Multiply two numbers and print the result.

    Args:
        a: First number
        b: Second number

    Output:
        Prints the product of a and b
    """
    print(a * b)


# Helper function that subtracts sub.
def sub(a, b):
    """
    Subtract two numbers and print the result.

    Args:
        a: First number (minuend)
        b: Second number (subtrahend)

    Output:
        Prints the difference (a - b)
    """
    print(a - b)

# This module is designed to be imported by other files:
# Example usage in another file:
#   from Client import add, mul, sub
#   add(5, 3)   # Output: 8
#   mul(4, 2)   # Output: 8
#   sub(10, 3)  # Output: 7
