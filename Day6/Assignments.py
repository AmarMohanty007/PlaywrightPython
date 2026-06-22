"""
Day 6 - String Operations Assignments
Practical exercises and assignments for string manipulation in Python.
This module covers assignment solutions for:
- String creation and type checking
- String immutability and memory addressing
- Multiplication tables
- String concatenation and repetition
- String slicing and indexing
- Substring checking with 'in' and 'not in'
- F-string formatting
- Case conversion methods
- String counting and replacement
- Character validation (isalpha, isdigit, isalnum)
- Split and strip operations for string parsing
"""

#1. Create Strings in Different Ways
#Task: Write a program to create strings using single quotes, double quotes, and str()
#constructor. Print them and check their type using type().

# Variable Declaration
# string1 = 'Hello World'
# string2 = "Hello Python"
# string3 = str("Hello Pycharm")
#
# # Print statements
# print(string1)
# print(string2)
# print(string3)
#
# # Type() Function
# print(type(string1))
# print(type(string2))
# print(type(string3))

#2. Immutable Strings Demo
#Task: Create a string "hello", print its memory address using id().
#Now modify it (e.g., s = s + " world") and print again. Show that the address changes.

# # Create a string
# s = "hello"
# print("Original string:", s)
# print("Memory address of s:", id(s))
#
# # Modify the string
# s = s + " world"
# print("\nModified string:", s)
# print("Memory address of s after modification:", id(s))






# string1 = "hello"
# print(id(string1))
# string1 = string1 + " World"
# print(id(string1))
#
# list1 = [1, 2, 3]
# print(id(list1))
# list1 = [1 ,2 , 3, 4, 5, 6]
# print(id(list1))


#3. print any tables until 10

# num = int(input("Enter a Table Number: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

# 3. Concatenation and Repetition
# Task: Take two strings "Python" and "Rocks".
# • Concatenate them using +.
# • Repeat the string "Python" 3 times using *.

# string1 = "Python"
# string2 = "Rocks"
# print(string1+string2)
# print(string1*3)
# print(string2*3)

# 4. String Slicing Practice
# Task: Take a string "welcome". Print:
# • Characters from index 1 to 4
# • First 5 characters
# • Last 3 characters using negative indexing
# • Middle substring "lco" using slicing

# str = "welcome"
# print(str)
# print(str[1:4])
# print(str[0:5])
# print(str[-3:7])
# print(str[2:5])

# 5. Check Substring using in and not in
# Task: Write a program that asks the user to input a word.
# Check if "python" is present in that word. Print "Found" or "Not Found".

# word=input("Enter a word: ")
# if "" in word:
#     print("Found")
# else:
#     print("Not Found")

# 6. String Formatting with f-strings
# Task: Take user input for name and age.
# Use an f-string to print:
# "My name is <name>, and I am <age> years old."


# name = str(input("Enter Your Name: "))
# age = int(input("Enter Your  Age: "))
# print(f"My name is {name}, and I am {age} years old.")

# 7. Case Conversion Methods
# Task: Write a program that takes "welcome to python" and prints:
# • Capitalized string
# • Title case string
# • Uppercase string
# • Swapcase string


# str = "welcome to python"
# print(str.capitalize())
# print(str.title())
# print(str.upper())
# print(str.swapcase())

# 8. Counting and Replacing
# Task: Given string "banana", count how many times "a" appears.
# Then replace "banana" with "orange" in the string "I like banana".

# string1 = "I like banana"
# string2 = "Orange"
# print(string1.count("a"))
# print(string1.replace("banana","orange"))
#
# 9. Validation Check
# Task: Ask the user to input a string. Check if:
# • It contains only alphabets (isalpha())
# • It contains only digits (isdigit())
# • It is alphanumeric (isalnum())
# Print results accordingly.

# s = input("Enter the string: ")
# print(s.isalpha())
# print(s.isdigit())
# print(s.isalnum())
#
# 10. Split and Strip
# Task:
# • Given string " apple,banana,grape ", strip spaces.
# • Split the string by commas ,.
# • Print the list of fruits.

string1 = str(" apple,banana,grape ")
string2 = string1.lstrip().rstrip()
print("Fruits:",string2.split(","))


s = "  apple,banana,grape  "
# Strip spaces
s = s.strip()
# Split by comma
fruits = s.split(",")
print("Fruits:", fruits)


