"""
Day 2 - Operators in Python
Demonstrates arithmetic, relational, and logical operators.
This module covers:
- Arithmetic operators: +, -, *, /, //, %, **
- Relational operators: >, <, >=, <=, ==, !=
- Logical operators: and, or, not
"""

# Arithmetic operators
# Operations: +  -  *  / //  %  **
# a=5
# b=2
#
# print(a+b)  # 7 - Addition
# print(a-b)  # 3 - Subtraction
# print(a*b)  # 10 - Multiplication
# print(a/b)  # 2.5 - Division (returns float)
# print(a//b)  # 2 - Floor division (returns integer)
# print(a%b)  # 1 - Modulus (returns remainder)
# print(a**b)  # 25 - Exponentiation (5**2 = 5*5 = 25)


# Relational Operators
# Operators: >  <  >=  <=  ==  !=
# Relational operators always return boolean value True/False

# a=5
# b=10
#
# print(a>b)    # False - Is a greater than b?
# print(a<b)    # True - Is a less than b?
#
# print(a==b)   # False - Are a and b equal?
# print(a!=b)   # True - Are a and b not equal?
#
# b=5
# print(a==b)   # True - Now they are equal
# print(a!=b)   # False
#
# print(a<=b)   # True - Is a less than or equal to b?
# print(a>=b)   # True - Is a greater than or equal to b?


# Logical operators
# Operators: and  or  not
# Always returns boolean value True/False

# Truth table for logical operators:
# a      b       a and b     a or b      not a   not b
# -------------------------------------------------------
# T     T       T           T           F       F
# T     F       F           T           F       T
# F     T       F           T           T       F
# F     F       F           F           T       T

# Example 1:
# a=True
# b=False
#
# print(a and b)  # False - Both must be True
# print(a or b)   # True - At least one must be True
#
# print(not a)    # False - Inverts the boolean value
# print(not b)    # True - Inverts the boolean value


# Combination of relational and logical operators
print((1 < 2))  # True
print((1 > 2))  # False

print((1 < 2) and (1 > 2))  # False - Both conditions must be true
print((1 < 2) or (1 > 2))   # True - At least one condition must be true
