#Class Variables-Intro
'''
In Class, attributes can be defined into two parts:

    1.Instance variables: If the value of a variable varies from object to object, then such variables are called instance variables.
    2.Class Variables: A class variable is a variable that is declared inside of class, but outside of any instance method or __init__() method.
'''

#What is a calss variable ?
'''
1. If the value of a variable is not varied from object to object, such types of variables are called class variables or static variables.
2. Class variables are shared by all instances of a class. 
3.Unlike instance variable, the value of a class variable is not varied from object to object.

4.Class variables are declared when a class is being constructed. They are not defined inside any methods of a class 
    because of this only one copy of the static variable will be created and shared between all objects of the class.
    
5.For example, in Student class, we can have different instance variables such as name and roll number because 
    each student’s name and roll number are different.
    
6.if we want to include the school name in the student class, we must use the class variable instead of an instance variable 
    as the school name is the same for all students. So instead of maintaining the separate copy in each object, we can create a class variable that will hold the school name so all students (objects) can share it.
'''

#Creating class Variables
'''
1.A class variable is declared inside of class, but outside of any instance method or __init__() method.
2.By convention, typically it is placed right below the class header and before the constructor method and other methods.
'''

#An Example of a class variable
class Student:
    # Class variable
    school_name = 'ABC School '

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

print("\nCreating a class variable -school name\n")
# create first object
s1 = Student('Emma', 10)
print(s1.name, s1.roll_no, Student.school_name)
# access class variable

# create second object
s2 = Student('Jessa', 20)
# access class variable
print(s2.name, s2.roll_no, Student.school_name)


#Accessing Class Variable
'''
We can access static variables either by class name or by object reference, but it is recommended to use the class name.

In Python, we can access the class variable in the following places

    1.Access inside the constructor by using either self parameter or class name.
    2.Access class variable inside instance method by using either self of class name
    3.Access from outside of class by using either object reference or class name.
'''

#Access inside class using self
class Student:
    # Class variable
    school_name = 'ABC School '

    # constructor
    def __init__(self, name):
        self.name = name
        # access class variable inside constructor using self
        print(self.school_name)
        # access using class name
        print(Student.school_name)
print("\n\nAccessing using self\n")
# create Object
s1 = Student('Emma')



#Access Class Variable in Instance method and outside class
print("\n\nAccess Class Variable in Instance method and outside class\n")
class Student:
    # Class variable
    school_name = 'ABC School '

    # constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Instance method
    def show(self):
        print('Inside instance method')
        # access using self
        print(self.name, self.roll_no, self.school_name)
        # access using class name
        print(Student.school_name)

# create Object
s1 = Student('Emma', 10)
s1.show()

print('Outside class')
# access class variable outside class
# access using object reference
print(s1.school_name)

# access using class name
print(Student.school_name)


#Modify Class Variables
'''
We assign value to a class variable inside the class declaration. However, we can change the value of the class variable 
    either in the class or outside of class.

Note: We should change the class variable’s value using the class name only.
'''
print("\n\nModify Class Variables-Outside of a class\n")
class Student:
    # Class variable
    school_name = 'ABC School '

    # constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Instance method
    def show(self):
        print(self.name, self.roll_no, Student.school_name)

# create Object
s1 = Student('Emma', 10)
print('Before')
s1.show()

# Modify class variable
Student.school_name = 'XYZ School'
print('After')
s1.show()

'''
It is best practice to use a class name to change the value of a class variable. 
 Because if we try to change the class variable’s value by using an object, a new instance variable is created for that particular object, 
which shadows the class variables.
'''

class Student:
    # Class variable
    school_name = 'ABC School '

    # constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
print("\n\nModifying class Variables outside class without using ClassName but using an object\n")
# create Objects
s1 = Student('Emma', 10)
s2 = Student('Jessa', 20)

print('Before')
print(s1.name, s1.roll_no, s1.school_name)
print(s2.name, s2.roll_no, s2.school_name)

# Modify class variable using object reference
s1.school_name = 'PQR School'
print('After')
print(s1.name, s1.roll_no, s1.school_name)
print(s2.name, s2.roll_no, s2.school_name)

#Instance Variable	vs Class Variable_How they differ ?
'''
1.Instance variables are not shared by objects. Every object has its own copy of the instance attribute but Class variables are shared by all instances.
2.Instance variables are declared inside the constructor i.e., the __init__() method whereas Class variables are declared inside the class definition 
    but outside any of the instance methods and constructors.
3.It is gets created when an instance of the class is created whereas Class Variables is created when the program begins to execute.
4.Changes made to instance variables through one object will not reflect in another object whereas 
    Changes made in the class variable will reflect in all objects.
'''
#Sample program-Class and instance variable
print('\n\nCLass variable manufacturer and instance variables mddel and price that varies to each object\n')
class Car:
    # Class variable
    manufacturer = 'BMW'

    def __init__(self, model, price):
        # instance variable
        self.model = model
        self.price = price

# create Object
car = Car('x1', 2500)
car2 = Car('x3', 4500)
print(car.model, car.price, Car.manufacturer)
print(car2.model, car2.price, Car.manufacturer)

#Class Variables In Inheritance
'''
1.Only one copy of the class variable will be created and shared between all objects of that class.

2.When we use inheritance, all variables and methods of the base class are available to the child class. 
    In such cases, We can also change the value of the parent class’s class variable in the child class.

3.We can use the parent class or child class name to change the value of a parent class’s class variable in the child class.
'''

print("\n\nClass Variables in inheritance-after changing class variable using Classname.variable=new value\n")
class Course:
    # class variable
    course = "Python"

class Student(Course):

    def __init__(self, name):
        self.name = name

    def show_student(self):
        # Accessing class variable of parent class
        print('Before')
        print("Student name:", self.name, "Course Name:", Student.course)
        # changing class variable value of base class
        print('Now')
        Student.course = "Machine Learning"
        print("Student name:", self.name, "Course Name:", Student.course)
        print("")

# creating object of Student class
stud = Student("Emma")
stud2 = Student("David")
stud.show_student()
stud2.show_student()

'''
if both child class and parent class has the same class variable name. In this case, the child class will not inherit the 
    class variable of a base class. So it is recommended to create a separate class variable for child class 
    instead of inheriting the base class variable.
'''

print('\n\nChild and parent class has same variable name-\n')
class Course:
    # class variable
    course = "Python"

class Student(Course):
    # class variable
    course = "SQL"

    def __init__(self, name):
        self.name = name

    def show_student(self):
        # Accessing class variable
        print('Before')
        print("Student name:", self.name, "Course Name:", Student.course)
        # changing class variable's value
        print('Now')
        Student.course = "Machine Learning"
        print("Student name:", self.name, "Course Name:", Student.course)

# creating object of Student class
stud = Student("Emma")
stud.show_student()

# parent class course name
print('Parent Class Course Name:', Course.course)

#1.Wrong Use of Class Variables
'''
1.In Python, we should properly use the class variable because all objects share the same copy.
2.If one of the objects modifies the value of a class variable, then all objects start referring to the fresh copy.
'''

class Player:
# class variables
    club = 'Chelsea'
    sport = 'Football'


    def __init__(self, name):
        # Instance variable
        self.name = name


    def show(self):
        print("Player :", 'Name:', self.name, 'Club:', self.club, 'Sports:', self.sport)


p1 = Player('John')

# wrong use of class variable
p1.club = 'FC'
p1.show()

p2 = Player('Emma')
p2.sport = 'Tennis'
p2.show()

#New Player Amal-doesnt change variables club and sport -so it remains the same
p3=Player('Amal')
p3.show()

# actual class variable value
print("Printing actual values of class variables club and sport below")
print('Club:', Player.club, 'Sport:', Player.sport)

'''
Note:
1.The instance variable name is unique for each player. The class variable team and sport can be accessed and modified by any object.
2.Both objects modified the class variable, a new instance variable is created for that particular object with the same name as the class variable, 
    which shadows the class variables.
3.For object p1 new instance variable club gets created, and for object p2 new instance variable sport gets created.
4.So when you try to access the class variable using the p1 or p2 object, it will not return the actual class variable value.
5.To avoid this, always modify the class variable value using the class name so that all objects gets the updated value. 
'''

print("\n\nAfter properly Changing class Variables\n")
Player.club = 'FC'
Player.sport = 'Tennis'

p1 = Player('John')
p2 = Player('Emma')
p3=Player('Amal')
p1.show()
p2.show()
p3.show()
