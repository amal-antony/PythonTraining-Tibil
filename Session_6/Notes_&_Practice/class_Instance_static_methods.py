#Methods
'''
In Object-oriented programming, when we design a class, we use the following three methods

    1.Instance method performs a set of actions on the data/value provided by the instance variables. If we use instance variables
        inside a method, such methods are called instance methods.

    2.Class method is method that is called on the class itself, not on a specific object instance. Therefore, it belongs to a class level,
        and all class instances share a class method.

    3.Static method is a general utility method that performs a task in isolation. This method doesn’t have access to the instance and class variable.
'''

#Difference


#1: Primary Use
'''
    Class method Used to access or modify the class state. It can modify the class state by changing the value of a class variable 
            that would apply across all the class objects.

    The instance method acts on an object’s attributes. It can modify the object state by changing the value of instance variables.

    Static methods have limited use because they don’t have access to the attributes of an object (instance variables) and class attributes (class variables).
        They can be helpful in utility such as conversion form one type to another.
'''

#Difference #2: Method Defination

'''

    All three methods are defined inside a class, and it is pretty similar to defining a regular function.
    
    Any method we create in a class will automatically be created as an instance method. We must explicitly tell Python that 
    it is a class method or static method.
    
    Use the @classmethod decorator or the classmethod() function to define the class method
    
    Use the @staticmethod decorator or the staticmethod() function to define a static method.

Example:

    Use self as the first parameter in the instance method when defining it. The self parameter refers to the current object.
    
    On the other hand, Use cls as the first parameter in the class method when defining it. The cls refers to the class.
    
    A static method doesn’t take instance or class as a parameter because they don’t have access to the instance variables and class variables.
    
'''
print("\n\nMethod Definitions\n")
class Student:
    # class variables
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance variables
    def show(self):
        print(self.name, self.age, Student.school_name)

    @classmethod
    def change_School(cls, name):
        cls.school_name = name

    @staticmethod
    def find_notes(subject_name):
        return ['chapter 1', 'chapter 2', 'chapter 3']

#Difference #3: Method Call
'''
    Class methods and static methods can be called using ClassName or by using a class object.
    The Instance method can be called only using the object of the class.

Example:
'''
print("\n\nMethod Call\n")
# create object
jessa = Student('Jessa', 12)
# call instance method
jessa.show()

# call class method using the class
Student.change_School('XYZ School')
# call class method using the object
jessa.change_School('PQR School')
jessa.show()

# call static method using the class
print(Student.find_notes('Math'))
# call class method using the object
print(jessa.find_notes('Math'))


#Attribute Access
'''
Both class and object have attributes. Class attributes include class variables, and object attributes include instance variables.

    The instance method can access both class level and object attributes. Therefore, It can modify the object state.
    Class methods can only access class level attributes. Therefore, It can modify the class state.
    A static method doesn’t have access to the class attribute and instance attributes. Therefore, it cannot modify the class or object state.
'''
print("\n\nAttribute Access\n")
class Student:
    # class variables
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def show(self):
        # access instance variables
        print('Student:', self.name, self.age)
        # access class variables
        print('School:', self.school_name)

    @classmethod
    def change_School(cls, name):
        # access class variable
        print('Previous School name:', cls.school_name)
        cls.school_name = name
        print('School name changed to', Student.school_name)

    @staticmethod
    def find_notes(subject_name):
        # can't access instance or class attributes
        return ['chapter 1', 'chapter 2', 'chapter 3']

# create object
jessa = Student('Jessa', 12)
# call instance method
jessa.show()

# call class method
Student.change_School('XYZ School')

#Difference #5: Class Bound and Instance Bound
'''

    1.An instance method is bound to the object, so we can access them using the object of the class.
    2.Class methods and static methods are bound to the class. So we should access them using the class name.

'''
print('\n\nClass Bound and Instance Bound\n')
class Student:
    def __init__(self, roll_no): self.roll_no = roll_no

    # instance method
    def show(self):
        print('In Instance method')

    @classmethod
    def change_school(cls, name):
        print('In class method')

    @staticmethod
    def find_notes(subject_name):
        print('In Static method')

# create two objects
jessa = Student(12)

# instance method bound to object
print(jessa.show)

# class method bound to class
print(jessa.change_school)

# static method bound to class
print(jessa.find_notes)


#Note
'''
In Python, a separate copy of the instance methods will be created for every object.

Suppose you create five Student objects, then Python has to create five copies of the show() method (separate for each object). 
So it will consume more memory. On the other hand, the static method has only one copy per class.

Example:
'''
print('\n\nSeparete instnace methods for each object\n')
# create two objects
jessa = Student(12)
kelly = Student(25)

# False because two separate copies
print(jessa.show is kelly.show)

# True objects share same copies of static methods
print(jessa.find_notes is kelly.find_notes)

