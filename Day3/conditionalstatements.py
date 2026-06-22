"""
Day 3 - Conditional Statements in Python
Demonstrates if, if-else, if-elif-else, nested if, and ternary operators.
This module covers:
- Simple if statements
- if-else conditions
- if-elif-else statements
- Nested if statements
- Shorthand if (ternary operator)
- Combining logical operators with conditionals
- The 'pass' statement
"""

# if statement - executes code only if condition is True
# Example 1: Check voting eligibility
# age=15
# if age>=18:
#     print("eligible for vote")

# Example 2: Check discount eligibility
# amount=500
# discount=0
#
# if amount>1000:
#     discount=amount*10/100
#
# print("Actual amount after reducing discount:", amount-discount)


# if-else statement - executes one block if True, another if False
# Example 1: Check voting eligibility and ineligibility
# age=15
#
# if age>=18:
#     print("Eligible for vote")
# else:
#     print("Not eligible for vote")

# Example 2: Check if number is even or odd
# num=11
#
# if num%2==0:
#     print(num, "Even number")
# else:
#     print(num, "Odd number")


# if-elif-else statement - multiple conditions
# Example 1: Apply discount based on purchase amount slab
# Discount slabs:
# - 20% on amount exceeding 10000
# - 10% for amount between 5000-10000
# - 5% if it is between 1000-5000
# - no discount if amount<1000

# amount= 500
# print("Actual amount: ", amount)
#
# if amount>10000:
#     discount=amount*20/100
# elif amount>5000:
#     discount=amount*10/100
# elif amount>1000:
#     discount=amount*5/100
# else:
#     discount=0
#
# print("Payment amount after discount:", amount-discount)

# Example 2: Get day name from week number (1=Sunday, 2=Monday, etc.)
#
# weekno=10
#
# if weekno==1:
#     print("sunday")
# elif weekno==2:
#     print("monday")
# elif weekno==3:
#     print("Tuesday")
# elif weekno==4:
#     print("Wednesday")
# elif weekno==5:
#     print("Thursday")
# elif weekno==6:
#     print("Friday")
# elif weekno==7:
#     print("Saturday")
# else:
#     print("invalid week number")


# Nested if-else statements - if statements inside other if statements
# Example: Check if a number is divisible by 2 and/or 3
# num ---> divisible by both 2 and 3
# num ---> divisible by 2 but not 3
# num ---> divisible by 3 but not 2
# num ---> not divisible by 2 and not by 3

# num=6
# print("Number:", num)
#
# if num%2==0:
#     if num%3==0:
#         print("divisible by both 2 & 3")
#     else:
#         print("divisible by 2 but not 3")
# else:
#     if num%3==0:
#         print("divisible by 3 but not 2")
#     else:
#         print("not divisible by 2 and 3")


# Shorthand if - write if statement in one line
# a,b=20,10
#
# if a>b:
#     print("a is greater")
#
# # One-liner version:
# if a>b:print("a is greater")


# Shorthand if-else (Ternary operator) - conditional expression
# a,b=20,10
#
# if a>b:
#     print("a is greater")
# else:
#     print("b is greater")
#
# # Ternary operator version:
# print("a is greater") if a>b else print("b is greater")


# Using logical 'and' operator with if-elif-else
# Find the largest of 3 numbers
# Conditions:
# - if a>b and a>c   then a is largest
# - elif b>a and b>c then b is largest
# - else c is largest

# a=30
# b=200
# c=50
#
# if a>b and a>c:
#     print(" a is largest ", a)
# elif b>a and b>c:
#     print(" b is largest", b)
# else:
#     print(" c is largest", c)


# pass statement - used as placeholder when condition is empty
# The pass statement does nothing; it is used when a statement is required syntactically
a = 10
b = 100

if a > b:
    pass  # Do nothing if a is greater than b

print("something")
