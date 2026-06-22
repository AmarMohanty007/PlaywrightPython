"""
Day 4 - Range Function in Python
Demonstrates the range() function used with loops.
This module covers:
- range(stop) - single parameter
- range(start, stop) - start and stop parameters
- range(start, stop, step) - start, stop, and step parameters
- Using range with negative values
"""

# Syntax:
# range(stop)              # if you provide a single number, that becomes the stopping point
#                          # in this case 0 is the starting point
# range(start, stop)       # specify both start and stop
# range(start, stop, step) # specify start, stop, and increment/decrement


# Example 1: Only stopping value (start defaults to 0)
# print(list(range(10)))   # Equivalent to: list(range(0, 10))
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Example 2: Start & Stop values
# print(list(range(5, 10)))
# Output: [5, 6, 7, 8, 9]


# Example 3: Print even numbers between 1 to 10
# print(list(range(0, 10, 2)))
# Output: [0, 2, 4, 6, 8]


# Example 4: Print odd numbers between 1 to 10
# print(list(range(1, 10, 2)))
# Output: [1, 3, 5, 7, 9]


# Example 5: Reverse sequence (10, 9, 8, 7, 6, 5, 4, 3, 2)
# print(list(range(10, 1, -1)))
# Output: [10, 9, 8, 7, 6, 5, 4, 3, 2]


# Example 6: Range with negative numbers
# -11 -10 -9  -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7
# print(list(range(-10, -5)))
# Output: [-10, -9, -8, -7, -6]


# Example 7: Range with negative numbers and step
print(list(range(-10, -5, 2)))
# Output: [-10, -8, -6]
