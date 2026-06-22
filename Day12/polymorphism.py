"""
Day 12 - Polymorphism in Python
Demonstrates polymorphism through method overloading using default parameters.
Polymorphism allows methods to work with different types of data or different numbers of arguments.
This module covers:
- len() function polymorphism (works on strings, lists, tuples, dicts)
- Method overloading using default parameters
- Same method name, different behavior based on arguments
"""

# Example 1: Polymorphism with built-in len() function
# The same len() function works on different data types

# mystring = "welcome"
# print(len(mystring))  # Output: 7
#
# mylist = [10, 20, 30, 40, 50]
# print(len(mylist))    # Output: 5
#
# mytuple = (1, 2, 3, 4, 5)
# print(len(mytuple))   # Output: 5
#
# mydic = {"id": 123, "name": "john"}
# print(len(mydic))     # Output: 2 (number of key-value pairs)


# Example 2: Method overloading through default parameters (Polymorphism)

# class Human:
#     def sayHello(self, name=None):
#         if name is not None:
#             print("Hello " + name)
#         else:
#             print("Hello")
#
# h = Human()
# h.sayHello()        # Output: Hello (no name provided)
# h.sayHello("John")  # Output: Hello John (name provided)


# Example 3: Method overloading with multiple default parameters

class Calculation:
    """
    Class demonstrating method overloading using default parameters.
    The add() method can be called with 0, 1, 2, or 3 arguments.
    """
    def add(self, a=0, b=0, c=0):
        """
        Add up to 3 numbers with default values of 0.

        Args:
            a: First number (default: 0)
            b: Second number (default: 0)
            c: Third number (default: 0)
        """
        print(a + b + c)


# Create object
cal = Calculation()

# Call method with different number of arguments
cal.add()           # Output: 0 (0 + 0 + 0)
cal.add(10, 20)     # Output: 30 (10 + 20 + 0)
cal.add(10, 20, 30) # Output: 60 (10 + 20 + 30)
