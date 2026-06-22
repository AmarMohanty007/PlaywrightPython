"""
Day 5 - Strings in Python
Demonstrates string creation, manipulation, slicing, and formatting.
This module covers:
- Creating strings using different approaches
- String operators (+ and *)
- String slicing with positive and negative indices
- F-string formatting
- Membership operators (in, not in)
"""

# Creating strings in 3 approaches

# Approach 1: Using double quotes
# name = "John"
# grade = "B"

# Approach 2: Using single quotes
# name = 'John'
# grade = 'B'

# Approach 3: Using str() constructor
# name = str()       # empty string
# grade = str()      # empty string
# print(name, grade)
#
# name = str("John")
# grade = str("B")
# print(name, grade)
# print(type(name))  # <class 'str'>
# print(type(grade)) # <class 'str'>


# + and * operators with strings
# str = "welcome"
# print(str + " Programming")  # Concatenation: "welcome Programming"
# print(str * 3)              # Repetition: "welcomewelcomewelcome"


# Slicing strings
# Starting index count from 0, ending index count from 1
# mystr = "welcome"
#
# print(mystr[1:3])   # "el" - characters at indices 1 and 2
# print(mystr[:6])    # "welcom" - from start to index 6 (0 default)
# print(mystr[2:])    # "lcome" - from index 2 to end
#
# mystr = "welcome"
# print(mystr[1:-1])  # "elcom" - from index 1 to second-to-last
# print(mystr[1:-2])  # "elco" - from index 1 to third-from-last
#
# print(mystr[-5:-2]) # "lco" - using negative indices


# Formatting strings using F-Strings
# F-String was introduced in Python 3.6 and is the preferred formatting method.
# To specify a string as an f-string, put 'f' in front and use {} for placeholders.

# Example 1: Basic variable interpolation
# age = 30
# str = f"My name is John, I am {age}"
# print(str)

# Example 2: Format with decimal places
# Output: The price is 55.00
# price = 55
# str = f"The price is {price:.2f} "
# print(str)

# Example 3: Expressions inside f-strings
# price = 20
# str = f"The price is {price * 10} dollars"
# print(str)  # "The price is 200 dollars"


# Membership operators (in, not in) with strings
# Returns boolean value True/False

# str = "welcome"
# print("come" in str)       # True - substring exists
# print("lome" in str)       # False - substring doesn't exist
#
# print("come" not in str)   # False - substring exists
# print("lome" not in str)   # True - substring doesn't exist
