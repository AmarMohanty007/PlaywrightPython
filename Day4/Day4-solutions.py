"""
Day 4 Solutions - Python Looping and Conditional Statements

This module contains solutions for various programming exercises covering:
- Conditional statements (if/elif/else)
- While loops and for loops
- Break and continue statements
- Input validation
- String manipulation

Each solution demonstrates a specific programming concept or pattern.
"""

# ============================================================================
# Solution 1: Positive, Negative, or Zero
# Determines the sign of a number using conditional statements
# ============================================================================

num = float(input("Enter a number: "))

if num > 0:
    # Number is greater than zero
    print("Positive")
elif num < 0:
    # Number is less than zero
    print("Negative")
else:
    # Number is exactly zero
    print("Zero")


# ============================================================================
# Solution 2: Vowel or Consonant
# Checks if a single letter is a vowel or consonant using membership operator
# ============================================================================

ch = input("Enter a single letter: ").lower()

if ch in 'aeiou':
    # Character is one of the vowels (a, e, i, o, u)
    print("Vowel")
else:
    # Character is not a vowel (assuming valid letter input)
    print("Consonant")


# ============================================================================
# Solution 3: Grading System
# Assigns letter grades based on numeric score using if-elif ladder
# Grade boundaries: A(90+), B(80+), C(70+), D(60+), F(below 60)
# ============================================================================

score = int(input("Enter score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    # Score below 60 receives failing grade
    grade = "F"

print("Grade:", grade)


# ============================================================================
# Solution 4: Sum of Digits
# Extracts each digit from a number and calculates their sum
# Uses modulo (%) to get last digit and integer division (//) to remove it
# ============================================================================

num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10      # Extract the last digit
    total += digit        # Add digit to running total
    num //= 10            # Remove the last digit

print("Sum of digits:", total)


# ============================================================================
# Solution 5: Reverse a Number
# Reverses the digits of a number using arithmetic operations
# Builds reversed number by shifting digits left and adding new digit
# ============================================================================

num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10           # Extract the last digit
    reverse = reverse * 10 + digit  # Shift existing digits left and add new digit
    num //= 10                 # Remove the last digit

print("Reversed number:", reverse)


# ============================================================================
# Solution 6: Multiplication Table
# Prints the multiplication table (1-10) for a given number
# Uses str.format() for formatted output
# ============================================================================

n = int(input("Enter a number: "))

for i in range(1, 11):
    # Print in format: n x i = result
    print("{0} x {1} = {2}".format(n, i, n * i))


# ============================================================================
# Solution 7: Print a Square
# Creates a square pattern using asterisks
# Uses string multiplication to repeat "* " for each row
# ============================================================================

size = int(input("Enter size of square: "))

for i in range(size):
    # Print 'size' asterisks separated by spaces
    print("* " * size)


# ============================================================================
# Solution 8: Sum of First 'n' Numbers
# Calculates the sum of all integers from 1 to n
# Uses accumulator pattern with for loop
# ============================================================================

n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i  # Add each number to running total

print("Sum of first", n, "numbers is", total)


# ============================================================================
# Solution 9: Count Vowels in a Word
# Counts how many vowels appear in a given word
# Case-insensitive comparison using lower()
# ============================================================================

word = input("Enter a word: ").lower()
count = 0

for ch in word:
    if ch in 'aeiou':
        count += 1  # Increment counter for each vowel found

print("Number of vowels:", count)


# ============================================================================
# Solution 10: Fibonacci Sequence
# Generates Fibonacci sequence up to n terms
# Each number is the sum of the two preceding numbers (0, 1, 1, 2, 3, 5, 8, ...)
# ============================================================================

n = int(input("Enter number of terms: "))
a, b = 0, 1  # Initialize first two Fibonacci numbers

for i in range(n):
    print(a, end=" ")  # Print current number on same line
    a, b = b, a + b    # Update: next = current + previous


# ============================================================================
# Solution 11: Input Validation with break
# Demonstrates input validation using infinite loop and break statement
# Continues prompting until valid input is received
# ============================================================================

while True:
    num = int(input("Enter a number between 1 and 10: "))
    if 1 <= num <= 10:
        # Valid input received - exit the loop
        print("Valid number entered:", num)
        break
    else:
        # Invalid input - loop continues
        print("Invalid! Try again.")


# ============================================================================
# Solution 12: Skip Multiples with continue
# Prints numbers 1-20 but skips multiples of 3 using continue
# Demonstrates how continue skips remaining code in current iteration
# ============================================================================

for i in range(1, 21):
    if i % 3 == 0:
        # Skip multiples of 3 (3, 6, 9, 12, 15, 18)
        continue
    print(i)


# ============================================================================
# Solution 13: Simple ATM Simulator
# Menu-driven program simulating basic ATM operations
# Uses while loop with break for menu control
# ============================================================================

balance = 0

while True:
    # Display menu options
    print("\nATM Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        # Deposit: add amount to balance
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Balance:", balance)
    elif choice == "2":
        # Withdraw: subtract amount if sufficient balance
        amount = float(input("Enter withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("Balance:", balance)
        else:
            print("Insufficient balance!")
    elif choice == "3":
        # Exit: break out of the loop
        print("Exiting ATM. Goodbye!")
        break
    else:
        print("Invalid choice!")


# ============================================================================
# Solution 14: Count 'a's and 'b's
# Counts occurrences of specific characters ('a' and 'b') in a word
# Demonstrates multiple counters and selective counting with continue
# ============================================================================

word = input("Enter a word: ").lower()
count_a = 0
count_b = 0

for ch in word:
    if ch == 'a':
        count_a += 1  # Count letter 'a'
    elif ch == 'b':
        count_b += 1  # Count letter 'b'
    else:
        # Skip all other characters
        continue

print("'a' count:", count_a)
print("'b' count:", count_b)
