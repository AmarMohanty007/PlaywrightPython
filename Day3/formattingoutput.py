"""
Day 3 - Formatting Output in Python
Demonstrates various approaches to format and output strings with variables.
This module covers:
- Multiple variable assignment
- String concatenation with print()
- String formatting using % operator
- String formatting using .format() method
- Escape sequences (\n, \t)
"""

# Assign multiple variables at once
name, age, sal = "john", 30, 50000.50

# Approach 1: Print multiple values separated by commas
print(name, age, sal)

# Approach 2: Format output by printing strings with variables
# Expected Output:
# Name is: john
# Age is: 30
# Salary is: 50000.50

# String concatenation with + operator (works for strings only)
# print("Name is:"+name)      # valid - concatenate strings
# print("Age is:"+age)        # ERROR - cannot concatenate string and int
# print("Name is:", name)     # Print with comma separation
# print("Age is:", age)
# print("Salary is:", sal)

# Approach 3: % formatting (old style)
# Format specifiers: %s (string), %d (integer), %g (decimal/float)
# print("Name:%s  Age:%d     salary:%g  " % (name, age, sal))
# print("Age:%d  Name:%s     salary:%g  " % (age, name, sal))


# Approach 4: .format() method with positional arguments
# print("Name:{} Age:{}  salary:{}".format(name, age, sal))

# Approach 5: .format() method with indexed positions
# print("Name:{0} Age:{1}  salary:{2}".format(name, age, sal))
# print("salary:{2}  Age:{1} Name:{0}  ".format(name, age, sal))  # Can reorder


# Escape sequences for special characters
print("welcome to \n python")  # \n - newline character (prints on next line)

print("welcome\tto python")    # \t - tab character (prints with tab spacing)
