#Types of Varaibles in python
'''
There are several kinds of variables in Python:

    1.Instance variables in a class: these are called fields or attributes of an object
    2.Local Variables: Variables in a method or block of code
    3.Parameters: Variables in method declarations
    4.Class variables: This variable is shared between all objects of a class
'''


#Instance vs Class Variables_Intro
'''
In Object-oriented programming, when we design a class, we use instance variables and class variables.

    1.Instance variables: If the value of a variable varies from object to object, then such variables are called instance variables.
    2.Class Variables: A class variable is a variable that is declared inside of class, but outside of any instance method or __init__() method.
    
'''

#Instance Variables Naming Conventions
'''
    1.Instance variable names should be all lower case. For example, id
    2.Words in an instance variable name should be separated by an underscore. For example, store_name
    3.Non-public instance variables should begin with a single underscore
    4.If an instance name needs to be mangled, two underscores may begin its name
'''

#Instance Varaibles_Detail
'''

1.If the value of a variable varies from object to object, then such variables are called instance variables. 
    For every object, a separate copy of the instance variable will be created.

2.Instance variables are not shared by objects. Every object has its own copy of the instance attribute. 
    This means that for each object of a class, the instance variable value is different.

3.When we create classes in Python, instance methods are used regularly. 
    we need to create an object to execute the block of code or action defined in the instance method.

4.Instance variables are used within the instance method. We use the instance method to perform a set of actions on the data/value 
    provided by the instance variable.

5.We can access the instance variable using the object and dot (.) operator.

6.In Python, to work with an instance variable and method, we use the self keyword. 
    We use the self keyword as the first parameter to a method. The self refers to the current object.
    
'''

class Test:
    def __init__(self,num):
        self.val=num
        print(self.val)

t1=Test(10)
t2=Test(20)
t3=Test(30)

'''
1.Instance variables are declared inside a method using the self keyword. 
2.We use a constructor to define and initialize the instance variables.
'''

#Creating Instance Variable-name and age-Example
print("\n\n2.Example 2 name and age\n")
class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create first object
s1 = Student("Jessa", 20)

# access instance variable
print('Object 1')
print('Name:', s1.name)
print('Age:', s1.age)

# create second object
s2= Student("Kelly", 10)

# access instance variable
print('Object 2')
print('Name:', s2.name)
print('Age:', s2.age)



#Modify Instance Variables
'''
1.We can modify the value of the instance variable and assign a new value to it using the object reference.
2.When you change the instance variable’s values of one object, the changes will not be reflected in the remaining objects 
    because every object maintains a separate copy of the instance variable.
'''

print("\n\n3.Modify Instance Variable\n")
class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create object
stud = Student("Jessa ", 20)

print('Before')
print('Name:', stud.name, ', Age:', stud.age)

# modify instance variable
stud.name = 'Emma'
stud.age = 15

print('After')
print('Name:', stud.name, ', Age:', stud.age)


#Accessing Instance Variable
'''
There are two ways to access the instance variable of class:

    1.Within the class in instance method by using the object reference (self)
    2. Using getattr() method

'''
#Example 1: Access instance variable in the instance method
print("\n\n4.Accessing Instance Variable-self\n")
class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method access instance variable
    def show(self):
        print('Name:', stud.name, 'Age:', stud.age)

# create object
stud = Student("Jessa", 20)


# call instance method
stud.show()

#Access Instance Variable-getattr
  # getattr(Object, 'instance_variable')
print("\n\n5.Access Instance Variable-getattr\n")
class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create object
stud = Student("Jessa", 20)

# Use getattr instead of stud.name
print('Name:', getattr(stud, 'name'))
print('Age:', getattr(stud, 'age'))

#Dynamically Add Instance Variable to a Object
'''

1.We can add instance variables from the outside of class to a particular object. 
2. We can use the following syntax to add the new instance variable to the object.

        object_referance.variable_name = value
'''
print("\n\n6.Modify Instance variable\n")
class Student:
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create object
stud = Student("Jessa", 20)

print('Before')
print('Name:', stud.name, 'Age:', stud.age)

# add new instance variable 'marks' to stud
stud.marks = 75
print('After')
print('Name:', stud.name, 'Age:', stud.age, 'Marks:', stud.marks)


'''
Note:

    1.We cannot add an instance variable to a class from outside because instance variables belong to objects.
    2.Adding an instance variable to one object will not be reflected the remaining objects because 
        every object has a separate copy of the instance variable.
'''


#Dynamically Delete Instance Variable
'''
In Python, we use the del statement and delattr() function to delete the attribute of an object. Both of them do the same thing.

    1.del statement: The del keyword is used to delete objects. In Python, everything is an object, 
        so the del keyword can also be used to delete variables, lists, or parts of a list, etc.
    2.delattr() function: Used to delete an instance variable dynamically.

Note: When we try to access the deleted attribute, it raises an attribute error.
'''
#Example 1: Using the del statement
print("\n\n7-Using del statement\n")
class Student:
    def __init__(self, roll_no, name):
        # Instance variable
        self.roll_no = roll_no
        self.name = name

# create object
s1 = Student(10, 'Jessa')
print(s1.roll_no, s1.name)

# del name
del s1.name
# Try to access name variable
#print(s1.name)


#delattr() function
'''
The delattr() function is used to delete the named attribute from the object with the prior permission of the object. Use the following syntax.

# delattr(object, name)

    object: the object whose attribute we want to delete.
    name: the name of the instance variable we want to delete from the object.
'''
#Example
print("\n\n8.Using delattr function\n")
class Student:
    def __init__(self, roll_no, name):
        # Instance variable
        self.roll_no = roll_no
        self.name = name

    def show(self):
        print(f"Roll no {self.roll_no}", self.name)

s1 = Student(10, '-Jessa')
s1.show()

# delete instance variable using delattr()
delattr(s1, 'roll_no')
#s1.show()

#List all Instance Variables of a Object
'''
We can get the list of all the instance variables the object has. 
Use the __dict__ function of an object to get all instance variables along with their value.

The __dict__ function returns a dictionary that contains variable name as a key and variable value as a value

Example:
'''
print("\n\nThe dict function-list all variables\n")
class Student:
    def __init__(self, roll_no, name):
        # Instance variable
        self.roll_no = roll_no
        self.name = name

s1 = Student(10, 'Jessa')
print('Instance variable object has')
print(s1.__dict__)

# Get each instance variable
for key_value in s1.__dict__.items():
    print(key_value[0], '=', key_value[1])




