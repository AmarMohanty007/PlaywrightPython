"""
Day 4 - Match Statement (Structural Pattern Matching)

This module demonstrates Python's match statement, introduced in Python 3.10.
The match statement provides a more readable alternative to multiple if-elif-else
statements when comparing a value against several patterns.

Key concepts covered:
- Basic match-case syntax
- Using the pipe operator (|) for combining multiple cases
- Default case using underscore (_)
"""

# ============================================================================
# Introduction to Match Statement
# 
# The match statement is used to perform different actions based on different
# conditions. Instead of writing many if..else statements, you can use the
# match statement for cleaner, more readable code.
# ============================================================================

# ----------------------------------------------------------------------------
# Example 1: Basic Match Statement - Day of Week
# 
# This example shows how to match a number to a specific day of the week.
# Each 'case' represents a possible value and its corresponding action.
# The 'case _' is the default case (similar to 'else' in if-else).
# ----------------------------------------------------------------------------

# day = 10
# match day:
#     case 1: print("Sunday")
#     case 2: print("Monday")
#     case 3: print("Tuesday")
#     case 4: print("Wednesday")
#     case 5: print("Thursday")
#     case 6: print("Friday")
#     case 7: print("Saturday")
#     case _: print("Invalid week day")  # Default case for values not 1-7


# ============================================================================
# Example 2: Combining Multiple Values with Pipe Operator (|)
#
# Use the pipe character | as an OR operator in the case evaluation to check
# for more than one value match in a single case. This is useful when multiple
# values should trigger the same action.
#
# In this example:
# - Weekdays (2-6) are grouped together
# - Weekend days (1, 7) are grouped together
# - Any other value triggers the default case
# ============================================================================

day = 10
match day:
    case 2 | 3 | 4 | 5 | 6:
        print("Weekday")  # Matches Monday through Friday
    case 1 | 7:
        print("Weekend")  # Matches Sunday (1) and Saturday (7)
    case _:
        print("Invalid week")  # Default case for invalid day numbers



















