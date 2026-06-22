"""
Day 4 - For Loops in Python
Demonstrates the for loop with range() function.
This module covers:
- Basic for loop with range()
- Using range with step parameter
- Reverse iteration
- Loop variable scope in Python
"""

# Example 1: Print numbers 1 to 10
# range(1, 11) generates numbers from 1 to 10 (11 is exclusive)
# for i in range(1, 11):
#     print(i)


# Example 2: Print even numbers between 1 to 10

# Method 1: Using range with step of 2
# range(2, 11, 2) starts at 2, stops before 11, steps by 2
# for i in range(2, 11, 2):
#     print(i)  # Prints: 2, 4, 6, 8, 10

# Method 2: Using if condition to check for even numbers
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)


# Example 3: Print numbers from 10 to 1 (reverse order)
# range(10, 0, -1) starts at 10, stops before 0, steps by -1
# for i in range(10, 0, -1):
#     print(i)  # Prints: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1


# Example 4: Loop variable scope in Python
# In Python, loop variables are accessible after the loop ends
# (unlike many other languages where they are scoped to the loop)

# for i in range(1, 6):
#     print(i)
#
# print(i)  # This prints 5 - the loop variable is still accessible


# Example 5: Accessing loop variable after loop
for i in range(1, 6):
    pass  # Do nothing in the loop

print(i)  # Output: 5 - Loop variable retains its last value
