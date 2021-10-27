#What is it and how its useful ?
'''
Overloading a constructor allows for a class to be instantiated with a different number of parameters per instance.
'''

# Types of Constructor overloading
'''
No Constructor Overloading in Python
'''
#1. More than One Python Constructor
'''
If we give it more than one constructor, that does not lead to constructor overloading in Python
'''

class one:
    def __init__(self):
        print("First constructor")

    def __init__(self):
        print("Second constructor")

print("\n1. When creating multiple init methods in a class and creating an instance for it")
o=one()


#2. Two Different Kinds of Constructors in Python
'''
If we try two different kinds of constructors:
'''

print("\n\n2.When creating multiple init methods in a class and creating an instance for it\n")
class one:
    def __init__(self):
        print("First constructor")

    def __init__(self, val):
        self.val = val
        print("Second constructor", val)
#o = one()
'''
This means is Python rebinds the name __init__ to the new method. This means the first declaration of this method is inaccessible now.

Internally, __new__ is the constructor that returns a valid and unpopulated object on which to call __init__.

'''


#3. Using Default Arguments
'''
Even the following piece of code is simply the use of default arguments, not constructor overloading:
'''


class one:
    def __init__(self, a=1, b=2):
        print(a + b)

print("\n\nWith 1 argument")
o = one(2)
print("\nWith 2 arguments")
o1=one(2,3)
print("\nWith no argument")
o2=one()