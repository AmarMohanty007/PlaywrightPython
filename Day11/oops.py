"""
Day 11 - Object-Oriented Programming (OOP) in Python
Demonstrates classes, objects, instance methods, static methods, and constructors.
This module covers:
- Creating classes and objects
- Instance methods vs static methods
- Class variables and instance variables
- Local, global, and class variables scope
- Constructors (__init__) and initialization
- Employee and Car class examples
"""

# Import os module
import os


# Example 1: Creating a class with methods and creating objects
# class Myclass:
#     def myfun(self):
#         pass
#
#     def display(self, name):
#         print(name)
#
# # Create objects from the class
# mc1 = Myclass()
# mc1.myfun()
# mc1.display("John")
#
# mc2 = Myclass()
# mc2.myfun()
# mc2.display("Scott")


# Example with static method:
# class Phones:
#     def my_samsung(self):
#         print("Samsung", self)
#
#     @staticmethod
#     def my_apple(shape, operatingsystem):
#         return shape, operatingsystem
#
# obj1 = Phones()
# Phones.my_samsung("Phones")
# print(obj1.my_apple(shape="Blue", operatingsystem="IOS"))


# Example 2: Instance Method vs Static Method
# Note: 'self' inside a static method is just a parameter name; it doesn't refer to the object.
#
# class Myclass:
#     def m1(self):
#         print("this is instance method...")
#
#     @staticmethod
#     def m2(self, num):
#         print(self, num)
#
# mc = Myclass()
# mc.m1()      # Instance method - called on object
# mc.m2(10, 20)  # Static method - can be called on object
#
# Myclass.m2(10, 20)  # Static methods can be accessed directly from the class


# Example 3: Class variables and instance variables
#
# class Myclass:
#     a, b = 10, 20  # Class variables
#
#     def add(self):
#         print(self.a + self.b)
#
#     def mul(self):
#         print(self.a * self.b)
#
# mc = Myclass()
# mc.add()   # 30
# mc.mul()   # 200


# Example 4: Local, Global, and Class variables scope
#
# i, j = 15, 25  # Global variables
#
# class Myclass:
#     a, b = 10, 20  # Class variables
#
#     def add(self, x, y):
#         print(x + y)                        # 300 - local variables
#         print(self.a + self.b)              # 30 - class variables
#         print(i + j)                        # 40 - global variables
#
# mc = Myclass()
# mc.add(100, 200)


# Example 5: Local, Global, and Class variables with same variable names
#
# a, b = 15, 25  # Global variables
#
# class Myclass:
#     a, b = 10, 20  # Class variables
#
#     def add(self, a, b):
#         print(a + b)                                      # 300 - local variables
#         print(self.a + self.b)                           # 30 - class variables
#         print(globals()['a'] + globals()['b'])           # 40 - access global variables
#
# mc = Myclass()
# mc.add(100, 200)


# Example 6: Class with constructor
# __init__(self) is a constructor
# Constructors are used to initialize data
# Constructors are invoked automatically when an object is created.
#
# class Myclass:
#     def __init__(self):
#         print("This is constructor...")
#
#     def m1(self):
#         print("Hello...")
#
#     def m2(self, x, y):
#         return x + y
#
# mc = Myclass()  # Constructor is called automatically
# mc.m1()
# print(mc.m2(10, 20))


# Example 7: Constructor with parameters and class variables
#
# class Myclass:
#     name = "john"  # Class variable
#
#     def __init__(self, name):
#         print(name)           # David - local parameter
#         print(self.name)      # John - class variable
#
# mc = Myclass("David")


# Example 8a: Employee class with constructor and methods
#
# class Emp:
#     def __init__(self, eid, ename, sal):
#         self.eid = eid          # instance variable
#         self.ename = ename      # instance variable
#         self.sal = sal          # instance variable
#
#     def display(self):
#         print(self.eid, self.ename, self.sal)
#
# e1 = Emp(101, "John", 500000)
# e1.display()   # 101 John 500000
#
# e2 = Emp(102, "David", 600000)
# e2.display()   # 102 David 600000


# Example 8b: Car class with constructor and show method
#
# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#
#     def show(self):
#         print("Brand Name: ", self.brand)
#
# my_car = Car("Ford")
# my_car.show()


# Example 8c: Student class with modifiable attributes
#
# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
# s1 = Student("Anna", "A")
# print(s1.grade)   # A
#
# s1.grade = "B"    # Modify instance variable
# print(s1.grade)   # B
