"""
Day 9 - Dictionaries in Python
Comprehensive demonstration of dictionary operations.
Dictionaries are used to store data values in key:value pairs.
Dictionaries are ordered (as of Python 3.7), changeable (mutable), and do not allow duplicate keys.
This module covers:
- Creating dictionaries
- Accessing items (keys, values, items)
- Modifying and adding items
- Removing items
- Copying dictionaries
- Looping through dictionaries
"""

# 1. Creating a dictionary

# Approach 1: Using curly braces and key:value pairs
# mydic = {"brand": "Ford", "model": "Aspire", "year": 2024}
# mydic = {
#     "brand": "Ford",
#     "model": "Aspire",
#     "year": 2024
# }
# print(mydic)  # Output: {'brand': 'Ford', 'model': 'Aspire', 'year': 2024}


# Approach 2: Using dict() constructor
# mydic = dict(name="John", age=35, country="India")
# print(mydic)  # Output: {'name': 'John', 'age': 35, 'country': 'India'}


# A key can have multiple values (e.g., a list of colors)
# mydic = {
#     "brand": "Ford",
#     "model": "Aspire",
#     "year": 2024,
#     "colors": ["red", "white", "blue"]
# }
# print(mydic)


# 2. Accessing items from dictionary

# Approach 1: Using square brackets []
# mydic = {"brand": "Ford", "model": "Aspire", "year": 2024}
# print(mydic["model"])  # Output: "Aspire"

# Approach 2: Using get() method
# print(mydic.get("brand"))  # Output: "Ford"


# 3. Get all keys - keys() method returns a list of all keys
# mydic = {"brand": "Ford", "model": "Aspire", "year": 2024}
# print(mydic.keys())  # Output: dict_keys(['brand', 'model', 'year'])

# 4. Get all values - values() method returns a list of all values
# mydic = {"brand": "Ford", "model": "Aspire", "year": 2024}
# print(mydic.values())  # Output: dict_values(['Ford', 'Aspire', 2024])


# 5. Get all items - items() method returns each item as tuples in a list
# mydic = {"brand": "Ford", "model": "Aspire", "year": 2024}
# print(mydic.items())  # Output: dict_items([('brand', 'Ford'), ('model', 'Aspire'), ('year', 2024)])
# print(mydic)


# 6. Check if key exists (searching for a key in a dictionary)
# mydic = {"brand": "Ford", "model": "Aspire", "year": 2024}
#
# if "model" in mydic:
#     print("Exists")
# else:
#     print("Not exists")


# 7. Adding items to the dictionary
# mydic = {"brand": "Ford", "model": "Aspire", "year": 2024}
# mydic["color"] = "red"  # Add a new key-value pair
# print(mydic)  # Output: {'brand': 'Ford', 'model': 'Aspire', 'year': 2024, 'color': 'red'}



# 8. Updating dictionary - update() method
# mydic = {"brand": "Ford", "model": "Aspire", "year": 2024}
# mydic["color"] = "red"
# print("Before updating:", mydic)
#
# mydic.update({"year": 2025})    # Update existing key
# mydic.update({"color": "white"})  # Update existing key
# print("After updation:", mydic)  # Output: {'brand': 'Ford', 'model': 'Aspire', 'year': 2025, 'color': 'white'}



# 9. Removing items from dictionary

# Approach 1: Using pop() - removes specified key
# mydic = {"brand": "Ford", "model": "Aspire", "year": 2024}
# mydic.pop("model")
# print(mydic)  # Output: {'brand': 'Ford', 'year': 2024}


# Approach 2: Using popitem() - removes the last inserted item
# (In versions before 3.7, a random item is removed)
# mydic = {"brand": "Ford", "model": "Aspire", "year": 2024}
# mydic.popitem()
# print(mydic)  # Output: {'brand': 'Ford', 'model': 'Aspire'}


# Approach 3: Using del keyword - removes item with specified key name
# mydic = {"brand": "Ford", "model": "Aspire", "year": 2024}
# del mydic["model"]  # Remove only the "model" key-value pair
# print(mydic)  # Output: {'brand': 'Ford', 'year': 2024}
#
# mydic = {"brand": "Ford", "model": "Aspire", "year": 2024}
# del mydic  # Delete the entire dictionary
# print(mydic)  # NameError - mydic is no longer defined


# Approach 4: clear() method - clears all items from dictionary
# mydic = {"brand": "Ford", "model": "Aspire", "year": 2024}
# mydic.clear()
# print(mydic)  # Output: {}


# 10. Copying a dictionary

# Approach 1: Using copy() method
# mydic1 = {"brand": "Ford", "model": "Aspire", "year": 2024}
# mydic2 = mydic1.copy()
#
# print(mydic1)  # Output: {'brand': 'Ford', 'model': 'Aspire', 'year': 2024}
# print(mydic2)  # Output: {'brand': 'Ford', 'model': 'Aspire', 'year': 2024}

# Approach 2: Using dict() constructor
# mydic1 = {"brand": "Ford", "model": "Aspire", "year": 2024}
# mydic2 = dict(mydic1)
# print(mydic1)  # Output: {'brand': 'Ford', 'model': 'Aspire', 'year': 2024}
# print(mydic2)  # Output: {'brand': 'Ford', 'model': 'Aspire', 'year': 2024}


# 11. Length of dictionary
# mydic = {"brand": "Ford", "model": "Aspire", "year": 2024}
# print(len(mydic))  # Output: 3


# 12. Looping with dictionary

mydic = {"brand": "Ford", "model": "Aspire", "year": 2024}


# Print all key names in the dictionary, one by one
# for x in mydic:
#     print(x)
#
# for x in mydic.keys():
#     print(x)

# Print all values in the dictionary, one by one
# for x in mydic:
#     print(mydic[x])
#
# for x in mydic.values():
#     print(x)


# Print all the items from the dictionary
for x, y in mydic.items():
    print(x, y)
