"""
Day 4 - Break and Continue Statements in Python
Demonstrates loop control statements: break and continue.
This module covers:
- break statement - exits the loop immediately
- continue statement - skips to the next iteration
"""

# break statement - exits the loop immediately when condition is met
# Output: 1 2 3 4

# for i in range(1, 11):
#     if i == 5:
#         break  # Exit loop when i equals 5
#     print(i)   # Prints: 1 2 3 4


# continue statement - skips the current iteration and moves to the next
for i in range(1, 11):
    if i == 3 or i == 5 or i == 7:
        continue  # Skip printing when i is 3, 5, or 7
    print(i)     # Prints all numbers except 3, 5, 7
