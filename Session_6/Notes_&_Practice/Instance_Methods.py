# Instance Methods
'''
Inside a Class, we can define the following two types of methods.

    1.Instance methods: Used to access or modify the object state. If we use instance variables inside a method,
        such methods are called instance methods. It must have a self parameter to refer to the current object.

    2.Class methods: Used to access or modify the class state. In method implementation, if we use only class variables,
        then such type of methods we should declare as a class method. The class method has a cls parameter which refers to the class.
'''

#What is Instance Method ?
'''
If we use instance variables inside a method, such methods are called instance methods. The instance method performs a 
    set of actions on the data/value provided by the instance variables.

    1.A instance method is bound to the object of the class.
    2.It can access or modify the object state by changing the value of a instance variables

When we create a class in Python, instance methods are used regularly. To work with an instance method, we use the self keyword. 
    We use the self keyword as the first parameter to a method. The self refers to the current object.

Any method we create in a class will automatically be created as an instance method unless we explicitly tell Python that it is a class or static method.
'''

#Define Instance Method
'''
Instance methods are defined inside a class, and it is similar to defining a regular function.

    1.Use the def keyword to define an instance method in Python.
    2.Use self as the first parameter in the instance method when defining it. The self parameter refers to the current object.
    3.Using the self parameter to access or modify the current object attributes.
'''
class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method to access instance variable
    def show(self):
        print('Name:', self.name, 'Age:', self.age)

#Calling An Instance Method
'''
We use an object and dot (.) operator to execute the block of code or action defined in the instance method.
'''

print("\n\n1.Calling Instance Method\n")
# create first object
print('First Student')
emma = Student("Jessa", 14)
# call instance method
emma.show()

# create second object
print('Second Student')
kelly = Student("Kelly", 16)
# call instance method
kelly.show()


#Modify Instance Variables inside Instance Method
'''
Create the instance method update() method to modify the student age and roll number when student data details change.
'''

class Student:
    def __init__(self, roll_no, name, age):
        # Instance variable
        self.roll_no = roll_no
        self.name = name
        self.age = age

    # instance method access instance variable
    def show(self):
        print('Roll Number:', self.roll_no, 'Name:', self.name, 'Age:', self.age)

    # instance method to modify instance variable
    def update(self, roll_number, age):
        self.roll_no = roll_number
        self.age = age

print("\n\n Udating/modifyin Instance methods\n")
# create object
print('class VIII')
stud = Student(20, "Emma", 14)
# call instance method
stud.show()

# Modify instance variables
print('class IX')
stud.update(35, 15)
stud.show()


#Instance Variables inside Instance Method
class Student:
    def __init__(self, roll_no, name, age):
        # Instance variable
        self.roll_no = roll_no
        self.name = name
        self.age = age

    # instance method to add instance variable
    def add_marks(self, marks):
        # add new attribute to current object
        self.marks = marks

# create object
stud = Student(20, "Emma", 14)
# call instance method
stud.add_marks(75)
print("\n\n3.Instance Variables inside Instance Method\n")
# display object
print('Roll Number:', stud.roll_no, 'Name:', stud.name, 'Age:', stud.age, 'Marks:', stud.marks)


#Dynamically Add Instance Method to a Object
'''
 1,We add methods to a class body when defining a class. but Python is a dynamic language that allows us to add or delete 
        instance methods at runtime. Therefore, it is helpful in the following scenarios.

    2.When class is in a different file, and you don’t have access to modify the class structure
        If we wanted to extend the class functionality without changing its basic structure because many systems use the same structure.

'''

#Example:
'''
We should add a method to the object, so other instances don’t have access to that method. 
We use the types module’s MethodType() to add a method to an object.
'''

import types

class Student:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def show(self):
        print('Name:', self.name, 'Age:', self.age)

# create new method - note theat this is outside the class so not an instance method but can be made for specific instances
def welcome(self):
    print("Hello", self.name, "Welcome to Class IX")


# create object
s1 = Student("Jessa", 15)
print("\n\n4.Dynamically Add methods\n")

# Add instance method to object
s1.welcome = types.MethodType(welcome, s1)
s1.show()

# call newly added method
s1.welcome()


#Dynamically Delete Instance Methods
'''
We can dynamically delete the instance method from the class. In Python, there are two ways to delete method:

    1.By using the del operator
    2.By using delattr() method
'''
#By using the del operator
#we will delete an instance method named percentage() from a Student class,try to access it after removing it => get an Attribute Error.
class Student:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def show(self):
        print('Name:', self.name, 'Age:', self.age)

    # instance method
    def percentage(self, sub1, sub2):
        print('Percentage:', (sub1 + sub2) / 2)

emma = Student('Emma', 14)
print("\n\n5.Delete using del\n")
emma.show()
emma.percentage(67, 62)

# Delete the method from class using del operator
# error -del emma.percentage

# Again calling percentage() method
# It will raise error
emma.percentage(67, 62)

#By using the delattr() method
'''
The delattr() is used to delete the named attribute from the object with the prior permission of the object. Use the following syntax to delete the instance method.

delattr(object, name)

    1.object: the object whose attribute we want to delete.
    2.name: the name of the instance method you want to delete from the object.
'''
#Example: will delete an instance method named percentage() from a Student class.

emma = Student('Emma', 14)
emma.show()
emma.percentage(67, 62)

print("\n\n6.Delete using delattr()\n")
# delete instance method percentage() using delattr()
#error - delattr(emma, 'percentage')
emma.show()

# Again calling percentage() method
# It will raise error
emma.percentage(67, 62)


