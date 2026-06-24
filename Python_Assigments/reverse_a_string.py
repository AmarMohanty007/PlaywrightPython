
# # --------------------------------------------------------------------
# # write a Python program to reverse a string using looping statement
# # --------------------------------------------------------------------


# Method 1: Using a loop
actual_text = 'India is my country'

print("Actual String:",actual_text)
reversed_text = ""

for ch in actual_text:
    reversed_text = ch + reversed_text

print("Reversed string:", reversed_text)
