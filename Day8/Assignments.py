"""
Day 8 - Collections Assignments
Practical exercises for lists, sets, and tuples in Python.
This module covers assignment solutions for:
- List append, extend, and sort operations
- List copying (shallow vs reference)
- Set creation and duplicate handling
- Set operations (add, pop, intersection)
- Tuple indexing and counting
- Tuple concatenation and repetition
- Set operations with operators (& for intersection, ^ for symmetric difference)
- Edge cases like single-element tuples with trailing comma
"""

# nums = [1, 2, 3, 4]
#
# nums.append([40, 50])
#
# print(nums)

# list1 = [1,2,3,4]
# list1.extend([5,2])
#
#
# print(list1)
# x = [3, 1, 4, 2]
# x.sort()
# print(x)

# x = [10, 20, 30]
# y = x
# y.append(40)
# x.append(50)
# print(x)
# print(y)


# x = [10,20,30,0,50,60,70,80,90,99]
# print(x[100])


# nums = [1, 2, 3] * 2
# print(nums)

# set1 = {}
# print(set1)

# set2 = {"apple", "banana", "cherry"}
# set2.add("Orange")
# print(set2)

# set2 = {"apple", "banana", "cherry"}
# set2.pop()
# print(set2)

# set2 = {1,2,3,2}
# print(set(set2))


# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# print(s1 & s2)

# s = set("banana")
# print(s)

# tuple1 = (1,2,3,4,5,6,7)
# print(tuple1[5])

# t = (1, 2,3,4,3,1,3)
# print(t.count(3))

# t = (1,2,3,[6],4,5)
# q = t.index(1)
# print(t)

# t = (1, 2, [3, 4])
# t[2][0] = 10
# print(t)

# t = (1,2,3,4)*2
# print(t)

#
# t1 = (1, 2)
# t2 = (3, 4)
# print(t1 + t2)


# t = (1,2,3)
# print(len(t))

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
#
# # Using the ^ operator
# result = set1 ^ set2
# print(result)  # Output: {1, 2, 5, 6}


# mylist = [5]
# print(mylist)

mytuple = (1,)
print(mytuple)
