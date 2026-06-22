"""
Python looping lesson covering for loops, while loops, range, match, break, and continue. This file focuses on Loopingstatement.
"""




# 12. Skip Multiples with continue: Print all numbers from 1 to 20, but skip the numbers
# that are multiples of 3 using the continue statement.

# for num in range(1, 21):    #generates numbers from 1 to 20.
#     if num % 3 == 0:        #checks if the number is divisible by 3.
#         continue            #skips the current iteration (so multiples of 3 won’t be printed).
#     print(num)              # prints only the numbers that are not multiples of 3.


#13. Simple ATM Simulator with break: Create a simple loop that shows an "ATM" menu
#with options like "Deposit," "Withdraw," and "Exit." Use break to end the program
#when the user chooses "Exit."

# while True:
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
#         break
#     else:
#         print("Invalid choice. Please try again.")


#14. Count 'a's and 'b's in a word: Get a word from the user. Iterate through the word and
#count the occurrences of the letter 'a' and 'b', using continue to skip any other letters.


word = input("Enter a word: ")

count_a = 0
count_b = 0

for ch in word:
    if ch == 'a':
        count_a += 1
    elif ch == 'b':
        count_b += 1
    else:
        continue  # skip any other letters

print(f"Number of 'a's: {count_a}")
print(f"Number of 'b's: {count_b}")
