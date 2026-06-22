"""
Day 10 - Variable Scope in Python
Demonstrates the difference between global and local variables.
This module covers:
- Global variables (defined outside functions)
- Local variables (defined inside functions)
- Accessing variables in different scopes
- Using the 'global' keyword to modify global variables
"""

# Global and Local Variables
# Variables created outside of functions are called Global variables
# Variables created inside functions are called Local variables

# Example 1: Accessing global variable within a function
#
# x = 20  # Global variable
#
# def myfun():
#     y = 10  # Local variable
#     print(x)  # Can access global variable within function - Output: 20
#     print(y)  # Can access local variable within function - Output: 10
#
# myfun()
#
# print(x)   # Can access global variable outside function - Output: 20
# print(y)   # TypeError - cannot access local variable outside function


# Example 2: Same variable name for global and local
#
# x = 100  # Global variable
#
# def myfun():
#     x = 200  # Local variable with same name
#     print(x)  # Prints local value - Output: 200
#
# myfun()
# print(x)   # Prints global value - Output: 100


# Example 3: Using 'global' keyword to modify global variable
# x = 100  # Global variable
#
# def myfun():
#     global x  # Declare that we're using the global x
#     x = 200   # Modify the global variable
#     print(x)  # Output: 200
#
# myfun()
# print(x)  # Output: 200 (global variable was modified)


# Example 4: Declare global variable inside a function
# There is no need to declare global variables outside the function.
# You can declare them inside the function using the 'global' keyword

def myfun():
    # global x = 100  # Syntax error - not valid
    global x  # Declare x as global
    x = 100   # Assign value to global x
    print(x)  # Output: 100


# Call the function to create/modify the global variable
myfun()

# Access the global variable outside the function
print(x)  # Output: 100 - able to access x because it's global
