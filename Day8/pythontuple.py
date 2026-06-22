"""
Day 8 - Tuples in Python
Comprehensive demonstration of tuple operations.
Tuples are immutable (unchangeable) collections of elements.
This module covers:
- Creating tuples
- Accessing tuple elements
- Counting and searching
- Converting tuples to lists for modification
- Copying and joining tuples
"""

# Creating tuples

# mytuple = ("apple", "banana", "cherry")
# print(mytuple)  # Output: ('apple', 'banana', 'cherry')


# Access tuple elements/values
# mytuple = ("apple", "banana", "cherry")
# print(mytuple[0])   # Output: apple (first element)
# print(mytuple[-1])  # Output: cherry (last element)

# Count number of times a value is repeated
# mytuple = ("apple", "banana", "cherry", "apple", "apple")
# print(mytuple.count("apple"))  # Output: 3


# Access range of indexes (slicing)
# mytuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(mytuple[2:5])     # Output: ('cherry', 'orange', 'kiwi')
# print(mytuple[-4:-1])   # Output: ('orange', 'kiwi', 'melon')


# Change values in a tuple
# By default, tuples are immutable (cannot change values directly)
# However, there is a workaround: convert tuple -> list -> modify -> convert back to tuple

# mytuple = ("apple", "banana", "cherry")
# # mytuple[1] = "orange"  # NOT POSSIBLE - TypeError
#
# # Workaround: convert to list, modify, convert back to tuple
# mylist = list(mytuple)
# print("After converting to list:", mylist)  # ['apple', 'banana', 'cherry']
# mylist[1] = "orange"  # Modify the list
# print("After changing mylist:", mylist)     # ['apple', 'orange', 'cherry']
#
# mytuple = tuple(mylist)  # Convert back to tuple
# print(mytuple)  # ('apple', 'orange', 'cherry')


# Retrieve data from tuple using looping statement
# mytuple = ("apple", "banana", "cherry")
#
# for i in mytuple:
#     print(i)


# Check if item exists in tuple (searching an item in a tuple)

# mytuple = ("apple", "banana", "cherry")
#
# print("cherry" in mytuple)  # Output: True
#
# if "cherry" in mytuple:
#     print("exists")
# else:
#     print("not exists")


# Length - count number of values in a tuple
# mytuple = ("apple", "banana", "cherry")
# print(len(mytuple))  # Output: 3


# Adding new values - NOT POSSIBLE (tuples are immutable)
# mytuple = ("apple", "banana", "cherry")
# # mytuple[3] = "orange"  # TypeError - cannot assign to tuple


# Copying a tuple
# mytuple1 = ("apple", "banana", "cherry")
# mytuple2 = mytuple1  # Create a reference (shallow copy)
# print(mytuple2)  # Output: ('apple', 'banana', 'cherry')


# Remove values from tuple - NOT POSSIBLE (tuples are immutable)
# mytuple = ("apple", "banana", "cherry")
# # mytuple.remove("apple")  # AttributeError - tuples don't have remove()


# Joining/Concatenating tuples
# tuple1 = ("a", "b", "c")
# tuple2 = (10, 20, 30)
# tuple3 = tuple1 + tuple2  # Concatenate tuples
# print(tuple3)  # Output: ('a', 'b', 'c', 10, 20, 30)
