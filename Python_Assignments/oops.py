# from _testcapi import instancemethod
# from pyee import cls
#
#
# class car():
#
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
#     @instancemethod
#     def show(self):
#         print(self.x,self.y,self.z)
#
#     @classmethod
#     def show2(cls):
#         print(f"class method: {cls}")
#
#     @staticmethod
#     def show3():
#         print(f"Static method")
#
#     @instancemethod
#     def show4(self):
#         print(f"Instance method: {self.x, self.y, self.z}")
#
# car.show2()
# car.show(car(1,2,3))
# car.show3()
# car.show4(car(1,2,3))


# name = "Amar"
# age = 30
#
# print(f"Name: {name}, Age: {age}")
#
#
# print("Hello\nWorld")
# print("Python\tProgramming")
# print("She said \'Hello\'")


# print(ord('A'))
# print(ord('a'))
# print(ord('0'))
#
# print(chr(65))
# print(chr(97))


# count = 10
#
# def increment():
#     global count
#     count += 1
#
# increment()
#
# print(count)


# x = 100
# print(x)
#
# del x

# print(x)  # Raises NameError


# x = 100
#
# print(id(x))



# values = [0, 1, "", "Hello", [], [10], None]
#
# for value in values:
#     print(value, bool(value))


# num = 15
#
# result = "Even" if num % 2 == 0 else "Odd"
#
# print(result)



age = 25
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")
    else:
        print("Not a Citizen")
else:
    print("Under Age")

























