#Inheritance
'''
The process of inheriting the properties of the parent class into a child class is called inheritance.
The existing class is called a base class or parent class and the new class is called a subclass or child class or derived class.
The main purpose of inheritance is the reusability of code because we can use the existing class to create a new class instead of creating it from scratch.

In inheritance, the child class acquires all the data members, properties, and functions from the parent class.
    Also, a child class can also provide its specific implementation to the methods of the parent class.

For example, In the real world, Car is a sub-class of a Vehicle class. We can create a Car by inheriting the properties of a Vehicle
    such as Wheels, Colors, Fuel tank, engine, and add extra properties in Car as required.

Syntax

class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
'''

#Types Of Inheritance
'''
In Python, based upon the number of child and parent classes involved, there are five types of inheritance. The type of inheritance are listed below:

    Single inheritance
    Multiple Inheritance
    Multilevel inheritance
    Hierarchical Inheritance
    Hybrid Inheritance
'''

#Single Inheritance
'''
In single inheritance, a child class inherits from a single-parent class. 
Only one child class and one parent class.
'''
print("\n\nSingle inheritance\n")
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')

# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')

# Create object of Car
car = Car()

# access Vehicle's info using car object
car.Vehicle_info()
car.car_info()


#Multiple Inheritance
'''
In multiple inheritance, one child class can inherit from multiple parent classes.
 So here is one child class and multiple parent classes.
'''
print("\n\nMultiple inheritance\n")
class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)

# Parent class 2
class Company:
    def company_info(self, company_name, location):
        print('\nInside Company class')
        print('Name:', company_name, 'location:', location)

# Child class
class Employee(Person, Company):
    def Employee_info(self, salary, skill):
        print('\nInside Employee class')
        print('Salary:', salary, 'Skill:', skill)

# Create object of Employee
emp = Employee()

# access data
emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.Employee_info(12000, 'Machine Learning')


#Multilevel inheritance
'''
In multilevel inheritance, a class inherits from a child class or derived class. 
Suppose three classes A, B, C. A is the superclass, B is the child class of A, C is the child class of B. 
In other words, we can say a chain of classes is called multilevel inheritance.
'''
print("\n\nMultiLevel inheritance\n")
# Base class
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')

# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')

# Child class
class SportsCar(Car):
    def sports_car_info(self):
        print('Inside SportsCar class')

# Create object of SportsCar
s_car = SportsCar()

# access Vehicle's and Car info using SportsCar object
s_car.Vehicle_info()
s_car.car_info()
s_car.sports_car_info()

#Hierarchical Inheritance
'''
1.In Hierarchical inheritance, more than one child class is derived from a single parent class. 
2.In other words, we can say one parent class and multiple child classes.
'''
print("\n\nHierarchial inheritance\n")
class Vehicle:
    def info(self):
        print("This is Vehicle")

class Car(Vehicle):
    def car_info(self, name):
        print("Car name is:", name)

class Truck(Vehicle):
    def truck_info(self, name):
        print("Truck name is:", name)

obj1 = Car()
obj1.info()
obj1.car_info('BMW')

obj2 = Truck()
obj2.info()
obj2.truck_info('Ford')



#Hybrid Inheritance
'''
When inheritance is consists of multiple types or a combination of different inheritance is called hybrid inheritance
'''
print("\n\nHybrid inheritance\n")
class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle class")

class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")

class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")

# Sports Car can inherits properties of Vehicle and Car
class SportsCar(Car, Vehicle):
    def sports_car_info(self):
        print("Inside SportsCar class")

# create object
s_car = SportsCar()

s_car.vehicle_info()
s_car.car_info()
s_car.sports_car_info()


#Python super() function
'''
When a class inherits all properties and behavior from the parent class is called inheritance. 
In such a case, the inherited class is a subclass and the latter class is the parent class.

In child class, we can refer to parent class by using the super() function. 
The super function returns a temporary object of the parent class that allows us to call a parent class method inside a child class method.

super()-Function benefits;
    We are not required to remember or specify the parent class name to access its methods.
    We can use the super() function in both single and multiple inheritances.
    The super() function support code reusability as there is no need to write the entire function
'''
print("\n\nSuper method illustration\n")
class Company:
    def company_name(self):
        return 'Google'

class Employee(Company):
    def info(self):
        # Calling the superclass method using super()function
        c_name = super().company_name()
        print("Jessa works at", c_name)

# Creating object of child class
emp = Employee()
emp.info()


#issubclass()
'''
In Python, we can verify whether a particular class is a subclass of another class. 
For this purpose, we can use Python built-in function issubclass(). 
This function returns True if the given class is the subclass of the specified class. Otherwise, it returns False.

Syntax

issubclass(class, classinfo)

Where,

    class: class to be checked.
    classinfo: a class, type, or a tuple of classes or data types.
'''
print("\n\nis sub class demo\n")
class Company:
    def fun1(self):
        print("Inside parent class")

class Employee(Company):
    def fun2(self):
        print("Inside child class.")

class Player:
    def fun3(self):
        print("Inside Player class.")

# Result True
print(issubclass(Employee, Company))

# Result False
print(issubclass(Employee, list))

# Result False
print(issubclass(Player, Company))

# Result True
print(issubclass(Employee, (list, Company)))

# Result True
print(issubclass(Company, (list, Company)))


#Method Overriding
'''
In inheritance, all members available in the parent class are by default available in the child class. 
If the child class does not satisfy with parent class implementation, then the child class is allowed to redefine 
    that method by extending additional functions in the child class. This concept is called method overriding.

When a child class method has the same name, same parameters, and same return type as a method in its superclass, 
then the method in the child is said to override the method in the parent class.
'''
print("\n\nMethod Overriding-class\n")
class Vehicle:
    def max_speed(self):
        print("max speed is 100 Km/Hour")

class Car(Vehicle):
    # overridden the implementation of Vehicle class
    def max_speed(self):
        print("max speed is 200 Km/Hour")

# Creating object of Car class
car = Car()
car.max_speed()


#Method Resolution Order in Python
'''
In Python, Method Resolution Order(MRO) is the order by which Python looks for a method or attribute. 
First, the method or attribute is searched within a class, and then it follows the order we specified while inheriting.

This order is also called the Linearization of a class, and a set of rules is called MRO (Method Resolution Order). 
The MRO plays an essential role in multiple inheritances as a single method may found in multiple parent classes.

In multiple inheritance, the following search order is followed.

    First, it searches in the current parent class if not available, then searches in the parents class specified while inheriting (that is left to right.)
    We can get the MRO of a class. For this purpose, we can use either the mro attribute or the mro() method.
    
'''
print("\n\nIllustrate Method resolution order\n")
class A:
    def process(self):
        print(" In class A")

class B(A):
    def process(self):
        print(" In class B")

class C(B, A):
    def process(self):
        print(" In class C")

# Creating object of C class
C1 = C()
C1.process()
print(C.mro())
# In class C
# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]


