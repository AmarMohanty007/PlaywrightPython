"""
Day 5 - String Methods in Python
Comprehensive demonstration of built-in string methods.
This module covers methods for:
- Case conversion: capitalize(), lower(), upper(), title(), swapcase()
- Formatting: center(), format()
- Searching: find(), index(), count()
- Replacement: replace()
- Validation: isalnum(), isalpha(), isdecimal(), isdigit(), isnumeric(), islower(), isupper()
"""

# capitalize() - Converts the first character to upper case
# s = "hello"
# print(s.capitalize())  # Output: "Hello"


# casefold() and lower() - Converts string to lower case
# s = "Hello"
# print(s.casefold())    # Output: "hello"
# print(s.lower())       # Output: "hello"

# upper() - Converts string to upper case
# s = "Hello"
# print(s.upper())       # Output: "HELLO"

# title() - Converts the first character of each word to upper case
# s = "welcome to python"
# print(s.title())       # Output: "Welcome To Python"

# swapcase() - Swaps cases: lower becomes upper and vice versa
# s = "Welcome To Python"
# print(s.swapcase())    # Output: "wELCOME tO pYTHON"


# center() - Returns a centered string
# str = "banana"
# print(str.center(10))        # Output: "  banana  "
# print(str.center(10, '*'))   # Output: "**banana**"

# format() - Formats specified values in a string
# name = "John"
# print("Hello {}".format(name))  # Output: "Hello John"



# find() - Searches for a value and returns its index position (or -1 if not found)
# s = "hello"
# print(s.find("e"))    # Output: 1
# print(s.find("l"))    # Output: 2
# print(s.find("x"))    # Output: -1 (not found)

# index() - Similar to find(), but raises ValueError if value not found
# print(s.index("e"))   # Output: 1
# print(s.index("l"))   # Output: 2
# print(s.index("x"))   # ValueError: substring not found

# count() - Returns the number of times a value occurs in a string
# s = "banana"
# print(s.count("a"))   # Output: 3
# print(s.count("na"))  # Output: 2

# replace() - Replaces a specified value with another specified value
# s = "Hello world"
# print(s.replace("world", "There"))  # Output: "Hello There"
# print(s.replace("l", "X"))          # Output: "HeXXo worXd"


# isalnum() - Returns True if all characters are alphanumeric (letters and numbers only)
# s = "ABC123"
# print(s.isalnum())    # Output: True
# s = "abc!"
# print(s.isalnum())    # Output: False


# isalpha() - Returns True if all characters are in the alphabet
# s = "Hello"
# print(s.isalpha())    # Output: True
# s = "123"
# print(s.isalpha())    # Output: False

# isdecimal() - Returns True if all characters are decimal digits (0-9)
# s = "123"
# print(s.isdecimal())  # Output: True
# s = "123.55"
# print(s.isdecimal())  # Output: False
# s = "xyz"
# print(s.isdecimal())  # Output: False


# isdigit() - Returns True if all characters are digits
# s = "123"
# print(s.isdigit())    # Output: True
# s = "xyz"
# print(s.isdigit())    # Output: False
# s = "12.5"
# print(s.isdigit())    # Output: False

# isnumeric() - Returns True if all characters are numeric
# Note: "-1" and "1.5" are NOT considered numeric because all characters must be numeric
# s = "123"
# print(s.isnumeric())  # Output: True
# s = "xyz"
# print(s.isnumeric())  # Output: False
# s = "12.5"
# print(s.isnumeric())  # Output: False


# islower() - Returns True if all characters are lower case
# isupper() - Returns True if all characters are upper case
# s = "welcome"
# print(s.islower())    # Output: True
# print(s.isupper())    # Output: False
