"""
Day 4 - While Loops in Python
Demonstrates while loop for iterating with a condition.
This module covers:
- Basic while loop
- While loop with condition checks
- Decrement operations
- Infinite loops
"""

# while loop: Executes as long as the condition is True

# Example 1: Print numbers 1 to 10
# i = 1
# while i <= 10:
#     print(i)  # Prints: 1 2 3 4 5 6 7 8 9 10
#     i += 1  # Increment by 1


# Example 2: Print even numbers between 1 to 10

# Method 1: Start at 2 and increment by 2
# i = 2
# while i <= 10:
#     print(i)  # Prints: 2, 4, 6, 8, 10
#     i += 2  # Increment by 2

# Method 2: Check if number is even using modulus
# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1


# Example 3: Print odd numbers between 1 to 10

# Method 1: Start at 1 and increment by 2
# i = 1
# while i <= 10:
#     print(i)  # Prints: 1, 3, 5, 7, 9
#     i += 2  # Increment by 2

# Method 2: Check if number is odd (not divisible by 2)
# i = 1
# while i <= 10:
#     if i % 2 != 0:
#         print(i)
#     i += 1


# Example 4: Print numbers 1 to 10 in descending order (10, 9, 8, ..., 1)
i = 10

while i >= 1:
    print(i)
    i -= 1  # Decrement by 1 (i = i - 1)


# Example 5: Infinite loop (dangerous, commented out)
# while True:
#     print(1)  # This would print 1 forever - causes infinite loop
