"""
Day 4 - Looping Statements Practice

This module provides practice exercises for Python looping constructs:
- for loops with range()
- while loops with break and continue
- Nested conditions within loops

The file contains both commented examples and active code for hands-on practice.
"""

# ============================================================================
# Exercise 12: Skip Multiples with continue
# Print all numbers from 1 to 20, but skip the numbers that are multiples of 3
# using the continue statement.
#
# The continue statement skips the rest of the current iteration and moves
# to the next iteration of the loop.
# ============================================================================

# for num in range(1, 21):    # generates numbers from 1 to 20
#     if num % 3 == 0:        # checks if the number is divisible by 3
#         continue            # skips the current iteration (multiples of 3 won't be printed)
#     print(num)              # prints only numbers that are not multiples of 3
                              # Output: 1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20


# ============================================================================
# Exercise 13: Simple ATM Simulator with break
# Create a simple loop that shows an "ATM" menu with options like "Deposit,"
# "Withdraw," and "Exit." Use break to end the program when the user chooses "Exit."
#
# The break statement terminates the entire loop immediately.
# ============================================================================

# while True:  # Infinite loop - runs until break is encountered
#     print("\n===== ATM Menu =====")
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Exit")
#
#     choice = input("Enter your choice (1-3): ")
#
#     if choice == "1":
#         amount = float(input("Enter amount to deposit: "))
#         print(f"You deposited ₹{amount}")
#     elif choice == "2":
#         amount = float(input("Enter amount to withdraw: "))
#         print(f"You withdrew ₹{amount}")
#     elif choice == "3":
#         print("Thank you for using the ATM. Goodbye!")
#         break  # Exit the loop and end the program
#     else:
#         print("Invalid choice. Please try again.")


# ============================================================================
# Exercise 14: Count 'a's and 'b's in a word
# Get a word from the user. Iterate through the word and count the occurrences
# of the letter 'a' and 'b', using continue to skip any other letters.
#
# This demonstrates:
# - String iteration (looping through characters)
# - Multiple counters
# - Using continue to skip irrelevant iterations
# ============================================================================

word = input("Enter a word: ")

# Initialize counters for each letter we want to track
count_a = 0
count_b = 0

for ch in word:
    if ch == 'a':
        count_a += 1  # Increment counter when 'a' is found
    elif ch == 'b':
        count_b += 1  # Increment counter when 'b' is found
    else:
        continue  # Skip any other letters (not 'a' or 'b')

print(f"Number of 'a's: {count_a}")
print(f"Number of 'b's: {count_b}")
