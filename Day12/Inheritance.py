"""
Day 12 - Inheritance in Python
Comprehensive demonstration of inheritance concepts in Object-Oriented Programming.
This module covers:
- Single inheritance
- Multilevel inheritance
- Hierarchy inheritance (Multiple children, one parent)
- Multiple inheritance
- Method and variable overriding
- Using super() to call parent class methods
"""

# Example 1: Basic inheritance (Parent-Child relationship)

# class A:
#     def m1(self):
#         print("This is m1 method from class A")
#
# class B(A):  # B inherits from A
#     def m2(self):
#         print("This is m2 method from class B")
#
# bobj = B()
# bobj.m1()  # Call inherited method from A
# bobj.m2()  # Call own method from B



# Example 2: Single inheritance with class variables

# class A:
#     x, y = 10, 20
#     def m1(self):
#         print(self.x + self.y)  # Output: 30
#
# class B(A):
#     a, b = 200, 100
#     def m2(self):
#         print(self.a - self.b)  # Output: 100
#
# bobj = B()
# bobj.m1()  # Calls parent method A.m1() - Output: 30
# bobj.m2()  # Calls own method B.m2() - Output: 100


# Example 3: Multilevel inheritance (A -> B -> C)
# C inherits from B, B inherits from A

# class A:
#     x, y = 10, 20
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A):
#     a, b = 200, 100
#     def m2(self):
#         print(self.a - self.b)
#
# class C(B):  # C inherits from B which inherits from A
#     i, j = 5, 2
#     def m3(self):
#         print(self.i * self.j)
#
# cobj = C()
# cobj.m1()  # Calls A.m1() - Output: 30
# cobj.m2()  # Calls B.m2() - Output: 100
# cobj.m3()  # Calls C.m3() - Output: 10


# Example 4: Hierarchical inheritance (Multiple children, one parent)
# Both B and C inherit from A independently

# class A:
#     x, y = 10, 20
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A):
#     a, b = 200, 100
#     def m2(self):
#         print(self.a - self.b)
#
# class C(A):
#     i, j = 5, 2
#     def m3(self):
#         print(self.i * self.j)
#
# bobj = B()
# bobj.m1()  # From A - Output: 30
# bobj.m2()  # From B - Output: 100
#
# cobj = C()
# cobj.m1()  # From A - Output: 30
# cobj.m3()  # From C - Output: 10


# Example 5: Multiple inheritance (C inherits from both A and B)
# C inherits from both A and B

# class A:
#     x, y = 10, 20
#     def m1(self):
#         print(self.x + self.y)
#
# class B:
#     a, b = 200, 100
#     def m2(self):
#         print(self.a - self.b)
#
# class C(A, B):  # C inherits from both A and B
#     i, j = 5, 2
#     def m3(self):
#         print(self.i * self.j)
#
# cobj = C()
# cobj.m1()  # From A - Output: 30
# cobj.m2()  # From B - Output: 100
# cobj.m3()  # From C - Output: 10


# Example 6: Calling parent class method using super()
# super() allows accessing methods from the parent class

# class A:
#     def m1(self):
#         print("This is m1 from class A")
#
# class B(A):
#     def m1(self):
#         print("This is m1 from class B")
#         super().m1()  # Invoke the immediate parent class method
#
# bobj = B()
# bobj.m1()
# # Output:
# # This is m1 from class B
# # This is m1 from class A


# Example 7: Calling parent class variables using child class

# class A:
#     a, b = 10, 20
#
# class B(A):
#     i, j = 100, 200
#
#     def m1(self, x, y):
#         print(x + y)          # Local variables - Output: 3000
#         print(self.i + self.j)  # B class variables - Output: 300
#         print(self.a + self.b)  # A class variables - Output: 30
#
# bobj = B()
# bobj.m1(1000, 2000)


# Example 8: Overriding variables (Child class overrides parent variable)

# class Parent:
#     name = "Scott"
#
# class Child(Parent):
#     name = "John"  # Overridden variable
#     def m(self):
#         print(super().name)  # Access parent's variable using super()
#
# cobj = Child()
# print(cobj.name)  # Output: John (child's value)
# cobj.m()          # Output: Scott (parent's value via super())


# Example 9: Overriding methods (Polymorphism - same method name, different behavior)

# class Bank:
#     def rateOfInterest(self):
#         return 0
#
# class XBank(Bank):
#     def rateOfInterest(self):
#         return 10.5  # XBank provides 10.5% interest
#
# class YBank(Bank):
#     def rateOfInterest(self):
#         return 12.5  # YBank provides 12.5% interest
#
# x = XBank()
# print(x.rateOfInterest())  # Output: 10.5
#
# y = YBank()
# print(y.rateOfInterest())  # Output: 12.5
