"""
Day 9 - Dictionary Assignments
Practical exercises for dictionary operations in Python.
This module covers assignment solutions for:
- Dictionary creation and empty dictionaries
- Accessing dictionary values by key
- Getting keys and values
- Dictionary length
- Updating and modifying dictionary items
- Using get() method with default values
- Checking key membership
- Dictionary methods (pop, clear, copy, items)
- Dictionary iteration
- Nested dictionaries
- Dictionary comparison
- Reference vs copy behavior
"""

# dic = {}
# print(dic)

# d = {"a": 1, "b": 2}
# print(d["a"])
# print(d.keys())
# print(len({"x":10, "y":20, "z":30}) )
# d["a"] = 5
# print(d["a"])

# d = {"a":1, "b":2, "c":3}
# print(d.get("a"))


# d = {"a": 1, "b": 2}
# print("c" in d)
# print(d.pop("a"))
# print(d.clear())
# print(d)

# d = {"a":1, "b": 2}
# d2 = d.copy()
# print(d2)
# print(d.items())


# d = {"x": 1, "y": 2}
# for k in d:
#  print(k)


# dict = {"a":1, "b": 2}
# dict.fromkeys(["a","b"],0)
# print(dict)

# dict = {"a": 1, "b": 2}
# dict2 = dict.update({"c": 3, "d": 4})
# print(dict)
# print(dict2)
# print(dict.popitem())
# print(dict)


# d = {"a":1, "b":2}
# print(d.get("c", 100))


# d = {"a":1, "b":2}
# d1 = {"a":1, "b":2}
# print(d==d1)

# d = {"a":{"x":10,"y":20}}
# print(d["a"]["y"])


# d = {1:"one", 2:"two"}
# print(list(d.values()))

#
# d = {"a":1, "b":2}
# for k,v in d.items():
#  print(k,v)

d = {"a":1}
d2 = d
d2["a"] = 100
print(d["a"])
