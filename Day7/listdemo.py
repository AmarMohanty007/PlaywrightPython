"""
Day 7 - Lists in Python
Comprehensive demonstration of list operations.
This module covers:
- Creating lists
- Accessing and modifying list items
- Slicing lists
- List methods (append, insert, remove, pop, etc.)
- Sorting, reversing, and copying lists
- Joining and extending lists
"""

# Creating lists

# mylist1 = [10, 20, 30, 40, 50]           # List of integers
# mylist2 = ["apple", "mango", "cherry"]   # List of strings
# mylist3 = [10, "apple", "A", True]       # Mixed data types
# mylist4 = list()                         # Empty list - []
#
# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist4)


# Access items/values from a list
# Index starts from 0
# mylist = ["apple", "banana", "cherry"]
#
# print(mylist[0])    # "apple" - first element
# print(mylist[2])    # "cherry" - third element
#
# print(mylist[-1])   # "cherry" - last element
# print(mylist[-2])   # "banana" - second-to-last element


# Access multiple values from list (slicing by range of indexes)
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#
# print(mylist[2:5])     # ['cherry', 'orange', 'kiwi']
# print(mylist[-4:-1])   # ['orange', 'kiwi', 'melon']


# Change item value in list
# mylist = ["apple", "banana", "cherry"]
# print("Before change:", mylist)  # ['apple', 'banana', 'cherry']
# mylist[0] = "orange"
# print("After the change:", mylist)  # ['orange', 'banana', 'cherry']


# Loop with list
# mylist = ["apple", "banana", "cherry"]
# for i in mylist:
#     print(i)


# Check if item exists in list (membership test)
# mylist = ["apple", "banana", "cherry"]
# if "banana" in mylist:
#     print("Yes, banana exists")
# else:
#     print("No, banana does not exist")


# Find out length/size of a list
# str = "welcome"
# print(len(str))  # 7
#
# mylist = ["apple", "banana", "cherry"]
# print(len(mylist))  # 3


# Count number of times a value is repeated in the list
# mylist = ["apple", "banana", "cherry", "apple", "apple"]
# print(mylist.count("apple"))  # 3


# Sorting the list

# mylist = ['cherry', 'mango', 'banana', 'apple']
#
# print("original list:", mylist)
# mylist.sort()  # Sort in ascending order: ['apple', 'banana', 'cherry', 'mango']
# mylist.sort(reverse=True)  # Sort in descending order: ['mango', 'cherry', 'banana', 'apple']
# print("Sorted values:", mylist)


# Reversing list items
# Pre-requisite: values are ideally in sorted order
#
# mylist = ['apple', 'banana', 'cherry', 'mango']  # Ascending order
# print("original values:", mylist)
# mylist.reverse()
# print("reversed values in a list:", mylist)  # ['mango', 'cherry', 'banana', 'apple']


# Add item to list using append() or insert()

# mylist = ["apple", "banana", "cherry"]
# print("before append:", mylist)  # ['apple', 'banana', 'cherry']
# mylist.append("orange")  # Add to end
# print("after append:", mylist)  # ['apple', 'banana', 'cherry', 'orange']
#
# mylist = ["apple", "banana", "cherry"]
# print("Before insertion:", mylist)  # ['apple', 'banana', 'cherry']
# mylist.insert(1, "orange")  # Insert at index 1
# print("After insertion:", mylist)  # ['apple', 'orange', 'banana', 'cherry']


# Remove item from list - 3 approaches

# Approach 1: remove() - accepts value
# mylist = ["apple", "banana", "cherry"]
# mylist.remove("banana")
# print("After removing:", mylist)  # ['apple', 'cherry']

# Approach 2: pop() - accepts index
# mylist = ["apple", "banana", "cherry"]
# mylist.pop(2)  # Remove element at index 2
# print("after removing:", mylist)  # ['apple', 'banana']

# Approach 3: del statement
# mylist = ["apple", "banana", "cherry"]
# del mylist[1]  # Delete element at index 1
# print(mylist)  # ['apple', 'cherry']


# Delete entire list
# del mylist  # Removes the entire list

# mylist = ["apple", "banana", "cherry"]
# del mylist
# print(mylist)  # NameError - mylist is no longer defined


# Copying the list

# Approach 1: using copy() method
# mylist1 = ["apple", "banana", "cherry"]
# mylist2 = mylist1.copy()  # Create independent copy
# print(mylist1)
# print(mylist2)

# Approach 2: using list() constructor
# mylist1 = ["apple", "banana", "cherry"]
# mylist2 = list(mylist1)  # Create independent copy
# print(mylist1)
# print(mylist2)


# Join the lists - 3 approaches

# Approach 1: using + operator
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)  # ['a', 'b', 'c', 1, 2, 3]

# Approach 2: using for loop
# list1 = ["a", "b", "c"]
# list2 = [10, 20, 30]
# for i in list2:
#     list1.append(i)
# print(list1)  # ['a', 'b', 'c', 10, 20, 30]

# Approach 3: using extend() method
# list1 = ["a", "b", "c"]
# list2 = [10, 20, 30]
# list1.extend(list2)
# print(list1)  # ['a', 'b', 'c', 10, 20, 30]
