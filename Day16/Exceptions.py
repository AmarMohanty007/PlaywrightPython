"""
Day 16 - Exception Handling in Python
Demonstrates how to handle and raise exceptions in Python.
This module covers:
- Common exception types (ZeroDivisionError, ValueError, NameError, TypeError)
- try and except blocks
- Multiple exception handling
- else and finally blocks
- Nested try-except
- Raising custom exceptions
"""

# Example 1: Syntax errors vs Exceptions
# print("welcome"  # This is a syntax error (missing closing parenthesis)


# Example 2: Exception - ZeroDivisionError
# n = 10
# res = n / 0  # ZeroDivisionError: division by zero
# print(res)


# Example 3: Other common exceptions

# x = "10"
# x = int("10")  # This is valid - converts "10" to integer 10
# # x = int("wel")  # ValueError: invalid literal for int() with base 10: 'wel'
# print(x + 5)


# Example 4: Handling exceptions using try & except

# print("started....")
# print(x)  # NameError: name 'x' is not defined
# print("finished....")

# # Better approach with try-except:
# print("started....")
# try:
#     print(x)
# except:
#     print("An exception occurred..")
# print("Finished...")  # This will still execute


# Example 5: Handling multiple specific exceptions

# try:
#     print(x)
# except NameError:
#     print("variable x is not defined.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except:
#     print("Some other exception occurred..")


# Example 6: Using 'else' with try-except
# The else block executes if no exceptions are raised

# try:
#     # print("Hello")
#     100 / 0
# except:
#     print("something went wrong")
# else:
#     print("Nothing went wrong")  # Only executes if no exception


# Example 7: Using 'finally' block
# The finally block ALWAYS executes regardless of whether an exception occurred

# try:
#     # print(x)
#     # print("welcome")
#     pass
# except:
#     print("Something went wrong")
# finally:
#     print("this is finally block...")  # Always executes


# Example 8: Complete try-except-else-finally structure
# User inputs: 0, xyx, 2

# try:
#     n = int(input("Enter a value:"))
#     res = 100 / n
# except ZeroDivisionError:
#     print("You can't divide by Zero..")
# except ValueError:
#     print("Enter a valid number..")
# else:
#     print(res)  # Only executes if no exception
# finally:
#     print("Exceptions completed......")


# Example 9: Nested try-except (try within try)

# try:
#     file = open("C:/Automation/automationFiles/myfile.txt", "r")
#     try:
#         file.write("welcome")
#     except:
#         print("Something went wrong when writing data into file")
#     finally:
#         file.close()
# except:
#     print("Something went wrong when opening the file...")


# Example 10: Raise exceptions
# As a Python developer you can choose to throw an exception if a condition occurs.
# Use the 'raise' keyword to throw an exception.

# x = -1
# if x < 0:
#     raise Exception("Sorry.. no numbers below zero..")


# Example 11: Specify the type of exception to raise

# x = "hello"
# if not type(x) is int:
#     raise TypeError("Only integers are allowed..")


# Example 12: Practical example - raising custom exceptions in functions

def set(age):
    """
    Function to set age with validation.

    Args:
        age: The age value to set

    Raises:
        ValueError: If age is negative
    """
    if age < 0:
        raise ValueError("Age cannot be negative..")
    print("Age is set", age)


# Usage examples:
# set(20)  # Valid - prints "Age is set 20"

try:
    set(-10)  # Invalid - raises ValueError
except ValueError:
    print("invalid data provided....")
