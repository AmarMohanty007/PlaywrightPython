"""
Day 2 - Deleting Variables in Python
Demonstrates how to delete variables using the del keyword.
This module shows:
- Variable deletion
- Accessing deleted variables (raises NameError)
"""

# Create variables
a = 100
b = 200

# Print variables before deletion
print(a)  # 100
print(b)  # 200

# Delete variable 'a' using the del keyword
del a

# Attempting to access deleted variable 'a' will raise NameError
# print(a)  # NameError: name 'a' is not defined

# Variable 'b' still exists and can be accessed
print(b)  # 200
