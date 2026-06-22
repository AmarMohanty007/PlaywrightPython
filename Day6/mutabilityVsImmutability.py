"""
Python strings and mutability lesson covering string methods, assignments, and object behavior. This file focuses on mutabilityVsImmutability.
"""

# Mutability vs. Immutability
# Mutable object → Can be changed after creation. (e.g., list, dict, set)
# Immutable object → Cannot be changed after creation. (e.g., int, float, tuple, str)

#Example1

# s1="hello"
# print("original string :", s1) #hello
# print("Address: ",id(s1))  #2541334803248
#
# #print(s1[0])  #h
# #s1[0]= "H"  # String is immutable so we cannot change the value
#
# # Hello
# s1="H"+s1[1:]
#
# print(s1)
# print(id(s1))
#

#Example 2:

# s1="python"
# #s2=s1.replace("p", "P")
#
# print("Before replace:", id(s1))
# s1=s1.replace("p", "X")
# print("After replace:", id(s1))
#
# print(s1)
# #print(s2)
# print(s1)


#   Example 3

# mylist=["h","e","l","l","o"]
# print("original list:", mylist) #['h', 'e', 'l', 'l', 'o']
# print("before modification id id:",id(mylist))
# mylist[0]="H"
# print("after modification:", mylist)  # mutable
# print("after modification id is:", id(mylist))


name =str()
print(name)

myStr = "welcome"
print(myStr[1:3])
print(myStr[:6])
print(myStr[1:-1])
print(myStr[-5:-2])

age = 25
print(f"I am {age} years old")
price = 50
print(f"Price: {price:.2f}")

s = "welcome to python"
print("python" not in s)

t = "amar"
print(t.lower())
print(t.swapcase())
print(t.title())
print(t.center(6, '*'))

print("My name is {}".format("John"))
print("hello".find("l") )
print("banana".count("a") )
print("Hello World".replace("World", "Python"))
print("abc123".isalnum() )
print( "12.5".isdigit())
print("hello.py".endswith(".py") )
print(" hi ".strip())
print(" hi".lstrip() )

q = "Python"
print(q[0] + q[-1])

r = "python"
print(r.upper().lower().capitalize())
print(r.replace("o", "a"))
print("hello".find("x"))

txt = "Python"
print(txt.startswith("P") and txt.endswith("n"))
print("pyTHon".swapcase())
print("Hello" " " "World")
print("Hello", "World")

name = str()
print(name)

s = "Python"
print(s[0] + s[-1])

s = "python"
print(len(s))


















