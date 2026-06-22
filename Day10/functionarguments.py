"""
Day 10 - Function Arguments in Python
Demonstrates different types of function arguments and parameters.
This module covers:
- Arbitrary/Variable-length arguments (*args)
- Positional/Required arguments
- Keyword arguments
- Default arguments
- Mixing positional and keyword arguments
- Returning multiple values
"""

# Types of Function Arguments:
# 1. Arbitrary or Variable-length Arguments (*args)
# 2. Positional or Required Arguments
# 3. Keyword Arguments
# 4. Default Arguments

# Example 1: Function with Arbitrary/Variable-length Arguments
# The *args parameter allows a function to accept any number of arguments

# def sum_function(*numbers):
#     total = 0
#     for i in numbers:
#         total = total + i
#     return total
#
# print(sum_function(10, 20))         # Output: 30
# print(sum_function(10, 20, 30))     # Output: 60
# print(sum_function(100, 200, 300))  # Output: 600
# print(sum_function())               # Output: 0 (empty call)

# Example 2: Positional and Keyword Arguments

# def myfun(i, j):
#     print(i, j)

# myfun(10, 20)  # Positional arguments - passing values by position
# myfun(i=10, j=20)  # Keyword arguments - passing values by name
# myfun(j=10, i=20)  # Keyword arguments - order doesn't matter

# Example 3: Default values can be assigned to positional arguments
# def myfun(i=10, j=20):
#     print(i, j)
#
# myfun(100)   # Output: 100 20 (i is overridden, j uses default)
# myfun()      # Output: 10 20 (both use default values)

# Example 4: Mixing positional and keyword arguments

# def myfun(a, b, c):
#     print(a, b, c)

# myfun(10, 20, 30)      # All positional - Output: 10 20 30
# myfun(a=10, b=20, c=30)  # All keyword - Output: 10 20 30
# myfun(c=10, b=20, a=30)  # Keyword arguments can be in any order - Output: 30 20 10

# myfun(10, 20, c=30)    # Mixed (positional first) - Output: 10 20 30
# myfun(10, b=20, c=30)  # Mixed - Output: 10 20 30

# myfun(10, b=20, 30)    # ERROR - positional args must come before keyword args
# myfun(10, 30, b=20)    # This has logical error (conflicting values for b)

# Example 5: Function can return multiple values
# Functions can return multiple values as a tuple

# def largest(a, b):
#     if a > b:
#         return a, b
#     else:
#         return b, a
#
# print(largest(100, 200))    # Output: (200, 100)
#
# res = largest(100, 200)
# print(res)                   # Output: (200, 100)
# print(type(res))             # Output: <class 'tuple'>
