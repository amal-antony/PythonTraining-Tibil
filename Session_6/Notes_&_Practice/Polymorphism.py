#Polymorphism


#What is Polymorphism in Python?
'''
1.Polymorphism in Python is the ability of an object to take many forms.
In simple words, polymorphism allows us to perform the same action in many different ways.

For example, Jessa acts as an employee when she is at the office.
However, when she is at home, she acts like a wife. Also, she represents herself differently in different places.
Therefore, the same person takes different forms as per the situation.

In polymorphism, a method can process objects differently depending on the class type or data type
'''

#Eg len function()
'''
The built-in function len() calculates the length of an object depending upon its type. If an object is a string, 
it returns the count of characters, and If an object is a list, it returns the count of items in a list.

The len() method treats an object as per its class type.
'''
print("\n\npolymorphism of en function w.r.t to list and string\n")
students = ['Emma', 'Jessa', 'Kelly']
school = 'ABC School'

# calculate count
print(len(students))
print(len(school))

#Polymorphism With Inheritance
'''
1.Polymorphism is mainly used with inheritance. In inheritance, child class inherits the attributes and methods of a parent class. 
    The existing class is called a base class or parent class, and the new class is called a subclass or child class or derived class.

2.Using method overriding polymorphism allows us to defines methods in the child class that have the same name 
    as the methods in the parent class. This process of re-implementing the inherited method in the child class is known as Method Overriding.
'''

#Method Overriding and advanages
'''

    1.It is effective when we want to extend the functionality by altering the inherited method. 
        Or the method inherited from the parent class doesn’t fulfill the need of a child class, so we need to 
        re-implement the same method in the child class in a different way.
    
    2.Method overriding is useful when a parent class has multiple child classes, and one of that child class wants to redefine the method. 
        The other child classes can use the parent class method. Due to this, we don’t need to modification the parent class code

In polymorphism, Python first checks the object’s class type and executes the appropriate method when we call the method. 
For example, If you create the Car object, then Python calls the speed() method from a Car class.
'''
print("\n\nMethod overriding Vehicle class-parent and Car Class-Child\n")
class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')


# inherit from vehicle class
class Car(Vehicle):
    def max_speed(self):
        print('Car max speed is 240')

    def change_gear(self):
        print('Car change 7 gear')


# Car Object
car = Car('Car x1', 'Red', 20000)
car.show()
# calls methods from Car class
car.max_speed()
car.change_gear()

print("")
# Vehicle Object
vehicle = Vehicle('Truck x1', 'white', 75000)
vehicle.show()
# calls method from a Vehicle class
vehicle.max_speed()
vehicle.change_gear()


#Overrride Built-in Functions
'''
In Python, we can change the default behavior of the built-in functions. 
For example, we can change or extend the built-in functions such as len(), abs(), or divmod() by redefining them in our class.

'''
print("\n\nRedefining built in len function\n")
class Shopping:
    def __init__(self, basket, buyer):
        self.basket = list(basket)
        self.buyer = buyer

    def __len__(self):
        print('Redefine length by making a user define =d len function ')
        count = len(self.basket)
        # count total items in a different way
        # pair of shoes and shir+pant
        return count * 2

shopping = Shopping(['Shoes', 'dress'], 'Jessa')
print(len(shopping))


#Polymorphism In Class methods
'''
Polymorphism with class methods is useful when we group different objects having the same method. 
we can add them to a list or a tuple, and we don’t need to check the object type before calling their methods. 
Instead, Python will check object type at runtime and call the correct method. 
We can call the methods without being concerned about which class type each object is. We assume that these methods exist in each class.
'''
print("\n\nPolymorphism in class methods-without checkimg class and instead looping through tuple\n")
class Ferrari:
    def fuel_type(self):
        print("\nfor Ferrari")
        print("Petrol")

    def max_speed(self):
        print("Max speed 350")

class BMW:
    def fuel_type(self):
        print("\nfor BMW")
        print("Diesel")

    def max_speed(self):
        print("Max speed is 240")

ferrari = Ferrari()
bmw = BMW()

# iterate objects of same type
for car in (ferrari, bmw):
    # call methods without checking class of object
    car.fuel_type()
    car.max_speed()


#Polymorphism with Function and Objects
'''
We can create polymorphism with a function that can take any object as a parameter and execute its method without checking its class type. 
Using this, we can call object actions using the same function instead of repeating method calls.
'''
print("\n\nPolymorphism with functions and objects-without checkimg class and instead looping through tuple\n")
class Ferrari:
    def fuel_type(self):
        print("\nfor Ferrari")
        print("Petrol")

    def max_speed(self):
        print("Max speed 350")

class BMW:
    def fuel_type(self):
        print("\nfor BMW")
        print("Diesel")

    def max_speed(self):
        print("Max speed is 240")

# normal function
def car_details(obj):
    obj.fuel_type()
    obj.max_speed()

ferrari = Ferrari()
bmw = BMW()

car_details(ferrari)
car_details(bmw)


#Method Overloading
'''
1.The process of calling the same method with different parameters is known as method overloading. 
2.Python does not support method overloading. 
3.Python considers only the latest defined method even if you overload the method. 
4.Python will raise a TypeError if you overload the method.

Example
'''

def addition(a, b):
    c = a + b
    print(c)


def addition(a, b, c):
    d = a + b + c
    print(d)



#addition(4, 5)

# This line will call the second product method
print("\n\nMethod Overloading\n")
addition(3, 7, 5)
#addition(4, 5)


#Creating area
print("\n\nFinding area using method overloading\n")
class Shape:
    # function with two default parameters
    def area(self, a, b=0):
        if b>0:
            print('Area of Rectangle is:', a * b)
        else:
            print('Area of Square is:', a ** 2)

square = Shape()
square.area(5)

rectangle = Shape()
rectangle.area(5, 3)


#Operator Overloading
'''

Operator overloading means changing the default behavior of an operator depending on the operands (values) that we use. 
In other words, we can use the same operator for multiple purposes.

For example, the + operator will perform an arithmetic addition operation when used with numbers.
    It will perform concatenation when used with strings.

The operator + is used to carry out different operations for distinct data types. 
This is one of the most simple occurrences of polymorphism in Python.
'''
print("\n\nOperator Overloading + operator\n")
print(100 + 200)

# concatenate two strings
print('Jess' + 'Roy')

# merger two list
print([10, 20, 30] + ['jessa', 'emma', 'kelly'])


#Overloading + operator for custom objects
'''
Suppose we have two objects, and we want to add these two objects with a binary + operator. 
It will throw an error if we perform addition because the compiler doesn’t add two objects

'''
print("\n\nWhen we add 2 objects using + operaor\n")
class Book:
    def __init__(self, pages):
        self.pages = pages

# creating two objects
b1 = Book(400)
b2 = Book(300)

# add two objects-error
#print(b1 + b2)

#Solving problem-creating add method
print("\n\nSolving problem-creating add method\n")
class Book:
    def __init__(self, pages):
        self.pages = pages

    # Overloading + operator with magic method
    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(400)
b2 = Book(300)
print("Total number of pages: ", b1 + b2)

#Overloading the * Operator
'''
The * operator is used to perform the multiplication. 
To to calculate the salary of an employee for a specific period. 
Internally * operator is implemented by using the __mul__() method.
'''
print("\n\nOverloading the * Operator\n")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, timesheet):
        print('Worked for', timesheet.days, 'days')
        # calculate salary
        return self.salary * timesheet.days


class TimeSheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days


emp = Employee("Jessa", 800)
timesheet = TimeSheet("Jessa", 50)
print("salary is: ", emp * timesheet)



