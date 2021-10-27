#Methods in Python_Intro
'''
In Object-oriented programming, we use instance methods and class methods. Inside a Class, we can define the following three types of methods.

    1.Instance method: Used to access or modify the object state. If we use instance variables inside a method, such methods are called instance methods.
        It must have a self parameter to refer to the current object.
    2.Class method: Used to access or modify the class state. In method implementation, if we use only class variables,
        then such type of methods we should declare as a class method. The class method has a cls parameter which refers to the class.
    3.Static method: It is a general utility method that performs a task in isolation. Inside this method, we don’t use instance or class
            variable because this static method doesn’t take any parameters like self and cls.
'''

#What is Class Method ?
'''
Class methods are methods that are called on the class itself, not on a specific object instance. Therefore, it belongs to a class level, 
and all class instances share a class method.

    1.A class method is bound to the class and not the object of the class. It can access only class variables.
    2.It can modify the class state by changing the value of a class variable that would apply across all the class objects.

In method implementation, if we use only class variables, we should declare such methods as class methods. 
The class method has a cls as the first parameter, which refers to the class.

Class methods are used when we are dealing with factory methods. Factory methods are those methods that return a class object for different use cases. 
Thus, factory methods create concrete implementations of a common interface. 

Note-The class method can be called using ClassName.method_name() as well as by using an object of the class.
'''

#Defining a class method
'''
1.Any method we create in a class will automatically be created as an instance method. 
    We must explicitly tell Python that it is a class method using the @classmethod decorator or classmethod() function.

2.Class methods are defined inside a class, and it is pretty similar to defining a regular function.

3.Like, inside an instance method, we use the self keyword to access or modify the instance variables. 
4.Inside the class method, we use the cls keyword as a first parameter to access class variables. 
    Therefore the class method gives us control of changing the class state.
5.The class method can only access the class attributes, not the instance attributes
'''

#Create Class Method Using @classmethod Decorator
'''
1.To make a method as class method, add @classmethod decorator before the method definition, and add cls as the first parameter to the method.
2.The @classmethod decorator is a built-in function decorator. In Python, we use the @classmethod decorator to declare a method as a class method.
    The @classmethod decorator is an expression that gets evaluated after our function is defined.
3.We will create a Student class object using the class method.
'''
print("\n\nCreate Class Method Using @classmethod Decorator\n")
from datetime import date

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name_cls, birth_year_cls):
        # calculate age and set it as a age
        # return new object
        #gives error-print(name,age)
        return cls(name_cls, date.today().year - birth_year_cls)


    def show(self):
        print(self.name + "'s age is: " + str(self.age))

jessa = Student('Jessa', 20)
jessa.show()

''''''
Amal=Student.calculate_age("Amal",2001)
Amal.show()
print(Amal)

# jessa a class attribute cannot access .show() method if not created using Student.calculate age

# create new object using the factory method
joy = Student.calculate_age("Joy", 1995)
joy.show()

'''
    1.In the above example, we created two objects, one using the constructor and the second using the calculate_age() method.
    2.The constructor takes two arguments name and age. On the other hand, class method takes cls, name, and birth_year 
        and returns a class instance which is nothing but a new object.
    3.The @classmethod decorator is used for converting calculate_age() method to a class method.
    4.The calculate_age() method takes Student class (cls) as a first parameter and returns constructor 
        by calling Student(name, date.today().year - birthYear), which is equivalent to Student(name, age).
'''


#Create Class Method Using classmethod() function
'''
1.The built-in function classmethod() is used to convert a normal method into a class method. 
2.The classmethod() is an inbuilt function in Python, which returns a class method for a given function.

3.Syntax:

classmethod(function)

    function: It is the name of the method you want to convert as a class method.
    It returns the converted class method.
'''

'''
Note: 

1.The method we want to convert as a class method must accept class (cls) as the first argument, 
    just like an instance method receives the instance (self).

2.As we know, the class method is bound to class rather than an object. So we can call the class method both by calling class and object.

3.A classmethod() function is the older way to create the class method in Python. In a newer version of Python, 
    we should use the @classmethod decorator to create a class method.
'''

#Create class method using classmethod() function
print("\n\nCreating class method using classmethod() function\n")

class School:
    # class variable
    name = 'ABC School'

    def school_name(cls):
        print('School Name is :', cls.name)


# create class method
School.school_name = classmethod(School.school_name)

# call class method
School.school_name()


#Example 3: Access Class Variables in Class Methods
'''
1.Using the class method, we can only access or modify the class variables. Let’s see how to access and modify the class variables in the class method.
2.Class variables are shared by all instances of a class. Using the class method we can modify the class state by 
    changing the value of a class variable that would apply across all the class objects.
'''

print("\n\n Access and modify the class variables-class.variablename\n")
class Student:
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, school_name):
        # class_name.class_variable
        cls.school_name = school_name

    # instance method
    def show(self):
        print(self.name, self.age, 'School:', Student.school_name)

jessa = Student('Jessa', 20)
jessa.show()
amal = Student('Amal', 21)
amal.show()

print("\nchanged value of class variable\n")
# change school_name
Student.change_school('XYZ School')
jessa.show()

amal = Student('Amal', 21)
amal.show()



#Class Method in Inheritance
'''
1.In inheritance, the class method of a parent class is available to a child class.
2.Whenever we derive a class from a parent class that has a class method then it creates the correct instance of the derived class

An Example
.A Vehicle class that contains a factory class method from_price() that will return a Vehicle instance from a price. 
        When we call the same method using the child’s class name, it will return the child’s class object.
'''
print("\n\nClass Methods in inheritance\n")
class Vehicle:
    brand_name = 'BMW'

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.brand=Vehicle.brand_name

    @classmethod
    def from_price(cls, name, price):
        # ind_price = dollar * 76
        # create new Vehicle object
        return cls(name, (price * 75))

    def show(self):
        print(self.name, self.price)

class Car(Vehicle):
    def average(self, distance, fuel_used):
        mileage = distance / fuel_used
        print(self.name, 'Mileage', mileage)


bmw_us = Car('BMW X5', 65000)
print(f"The brand of ur car is {bmw_us.brand}")
bmw_us.average(40000,4000)
bmw_us.show()

# class method of parent class is available to child class
# this will return the object of calling class
bmw_ind = Car.from_price('BMW X5', 65000)
bmw_ind.show()

# check type
print(type(bmw_ind))



#Dynamically Add Class Method to a Class
'''
We need to use the classmethod() function to add a new class method to a class.
'''
print("\n\nDynamically Add Class Method to a Class-classmethod()\n")
class Student:
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

# class ended

# method outside class
def exercises(cls):
    # access class variables
    print("Below exercises for", cls.school_name)

# Adding class method at runtime to class
Student.exercises = classmethod(exercises)

jessa = Student("Jessa", 14)
jessa.show()
# call the new method
Student.exercises()
jessa.exercises()


#Dynamically Delete Class Methods
'''
We can dynamically delete the class methods from the class. In Python, there are two ways to do it:

    By using the del operator
    By using delattr() method

By using the del operator

The del operator removes the instance method added by class. Use the del class_name.class_method syntax to delete the class method.
'''

#delete the class method named change_school() from a Student class. If you try to access it after removing it, you’ll get an Attribute Error.
print("\n\nDelete Class method using del\n")
class Student:
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, school_name):
        cls.school_name = school_name

jessa = Student('Jessa', 20)
print(Student.change_school('XYZ School'))
print(Student.school_name)

# delete class method
#error-del Student.change_school

# call class method
# it will give error
print(Student.change_school('PQR School'))
print(jessa.change_school('DEF School'))


#By using delatt() method
'''
The delattr() method is used to delete the named attribute and method from the class. 
The argument to delattr is an object and string. 
    1.The object=Class name
    2.The string must be the name of an attribute or method name.
'''

print("\n\nDelete Class method using delattr\n")
jessa = Student('Jessa', 20)
print(Student.change_school('XYZ School'))
print(Student.school_name)

# delete class method
#error-delattr(Student, 'change_school')

# call class method
# it will give error
print(Student.change_school('PQR School'))







