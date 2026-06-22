"""
Day 2 - String Concatenation
Demonstrates the concatenation operator (+) behavior with different data types.
This module covers:
- Numeric concatenation (addition)
- String concatenation
- Boolean-numeric concatenation
- Type mixing restrictions
"""

# Concatenation with numbers - performs addition
# When + is used between two numeric values, it performs addition operation
print(10 + 10)      # 20 - valid addition
print(10.5 + 12.0)  # 22.5 - valid addition (float)
print(10 + 10.5)    # 20.5 - valid addition (mixed int and float)


# Concatenation with strings - performs string concatenation
# When + is used between strings, it joins them together
print("welcome" + " python")  # "welcome python" - string concatenation


# Concatenation with booleans and numbers - performs addition
# True equals 1 and False equals 0 in arithmetic operations
print(True + 5)      # 6 - True is treated as 1, so 1 + 5 = 6
print(False + 5)     # 5 - False is treated as 0, so 0 + 5 = 5
print(True + True)   # 2 - 1 + 1 = 2


# Type mixing - cannot concatenate different types
# These operations will raise TypeError because types don't match

# print(10 + "welcome")     # TypeError - cannot add int and str
# print(10.5 + 'welcome')   # TypeError - cannot add float and str
# print(True + "welcome")   # TypeError - cannot add bool and str
