"""
Day 1 - Variables and Data Types
Demonstrates variable assignment and type checking in Python.
This module includes examples of:
- Variable assignment with different data types
- Multiple variable assignment patterns
- Variable swapping
- Dynamic type changing
"""

# Example 1: Check the type of variables
# a=10
# b=20
# s="welcome"
# grade='A'
#
# print(type(a))
# print(type(b))
# print(type(s))
# print(type(grade))

# Example 2: Print multiple values using a single print() function
# a=10
# b=10.5
# print(type(a))
# print(type(b))
#
# #print(a)
# #print(b)
#
# print(a,b)

# Example 3: Assigning Multiple Values at Once
# a,b,c=10,20,"welcome"
# print(a,b,c)


# Example 4: Assigning Same Value to Multiple Variables
# a=100
# b=100
# c=100

# #a,b,c=100,100,100
# a=b=c=100
# print(a,b,c)

# Example 5: Variable Swapping
#   a=10   b=20            a=20   b=10

# a=10
# b=20
# print(a,b)  # before swapping a=10, b=20
#
# b,a=a,b  # swapping
# print(a,b)  # after swapping b=10, a=20


# Example 6: Dynamic Type Changing
# Demonstrates that Python allows variables to change types dynamically

# Variable 'a' is assigned an integer value (100)
a = 100
print(a)
print(type(a))  # Output: <class 'int'>

# Reassign 'a' to another integer value (200)
a = 200
print(a)
print(type(a))  # Output: <class 'int'>

# Reassign 'a' to a string value - type changes dynamically
a = "welcome"
print(a)
print(type(a))  # Output: <class 'str'>
