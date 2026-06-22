"""
Day 2 - Taking Input From User
Demonstrates how to accept user input and handle type conversions.
This module covers:
- Using input() function to get user input (returns string)
- Type conversion using int() and float()
- String concatenation vs numeric addition with inputs
"""

# ISSUE: Without type conversion, input concatenates as strings
# num1=input("Enter first number:")
# num2=input("Enter second number:")
#
# print(type(num1))  # <class 'str'>
# print(type(num2))  # <class 'str'>
#
# print(num1+num2)   # "100200" - concatenates strings, not adds numbers


# Approach 1: Convert input to int before storing
# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
#
# print(type(num1))  # <class 'int'>
# print(type(num2))  # <class 'int'>
#
# print(num1+num2)   # 300 - performs addition


# Approach 2: Convert input during addition
# num1=input("Enter first number:")
# num2=input("Enter second number:")
#
# print(int(num1)+int(num2))  # Converts and adds in one line


# Example for decimal (float) input
# Taking decimal input from user and converting to float for proper addition
num1 = input("Enter first decimal number:")
num2 = input("Enter second decimal number:")

# Without conversion - concatenates as strings
print(num1 + num2)  # "10.520.0" - string concatenation

# With conversion - performs floating point addition
print(float(num1) + float(num2))  # 30.5 - proper float addition
