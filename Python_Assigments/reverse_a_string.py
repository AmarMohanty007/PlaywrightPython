from os import remove

# # --------------------------------------------------------------------
# # write a Python program to reverse a string using looping statement
# # --------------------------------------------------------------------


# Method 1: Using a loop
# actual_text = 'India is my country'
#
# print("Actual String:",actual_text)
# reversed_text = ""
#
# for ch in actual_text:
#     reversed_text = ch + reversed_text
#
# print("Reversed string:", reversed_text)

# my_str = 'i am Sunita!!'
#
#
# print("Actual list is =====>",my_str)
#
# empty_str = ''
# target = 'i'
# count = 0
# empty_space = ' '
#
# # input a string and reverse it
# # count the no. occurence of alphabet 'i'
# # remove the empty space from the string
#
# for i in my_str:
#     if target in i:
#         count=count+1
#         continue
#     elif i not in empty_space:
#         empty_str = i + empty_str
#         continue
#
# print("After Reverse list =====>",empty_str)
# print("Alphabet i occurence in the string:",count)


n = 5

for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)

for i in range(2, n + 1):
    print(" " * (n - i) + "* " * i)