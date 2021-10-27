# What is a class
'''
1.A class is a user-defined blueprint or prototype from which objects are created.
2.Classes provide a means of bundling data and functionality together.
3.Creating a new class creates a new type of object, allowing new instances of that type to be made.
4.Each class instance can have attributes attached to it for maintaining its state.
5.Class instances can also have methods (defined by their class) for modifying their state.
'''

# Main Points-Creating a class
'''
1.Classes are created by keyword class 
2.Attributes are the variables that belong to aclass .
3.Attributes are always public and can be accessed using the dot(.) operator.
Eg.: Myclass.Myattribute

'''

class Car:
    pass

# The self parameter
'''

1.Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method,
Python provides it.
2.If we have a method that takes no arguments, then we still have to have one argument.
3.This is similar to this pointer in C++ and this reference in Java.
4.When we call a method of this object as myobject.method(arg1, arg2),
this is automatically converted by Python into MyClass.method(myobject, arg1, arg2)
'''
print("\n\nClass and define methods\n")
class Car:
    key='ignition'

    def start(self):
        print(f"Start car by turning on {self.key}")
    def drive(self):
        print("Start Driving")

mycar=Car()
mycar.start()
mycar.drive()

#__init__ method
'''
1.The __init__ method is similar to constructors in C++ and Java. 
2.Constructors are used to initializing the object’s state. Like methods, a constructor also contains a collection of statements(i.e. instructions) 
that are executed at the time of Object creation. It runs as soon as an object of a class is instantiated. 
3.The method is useful to do any initialization you want to do with your object.
'''

#Class Naming Convention
'''
Naming conventions are essential in any programming language for better readability.
    Names should be sensible.

We should follow specific rules while we are deciding a name for the class in Python.

    Rule-1: Class names should follow the UpperCaseCamelCase convention
    Rule-2: Exception classes should end in “Error“.
    Rule-3: If a class is callable (Calling the class from somewhere), in that case, we can give a class name like a function.
    Rule-4: Python’s built-in classes are typically lowercase words

'''




