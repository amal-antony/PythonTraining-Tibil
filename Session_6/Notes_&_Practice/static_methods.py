#Methods at Class Level
'''
In Object-oriented programming, at the class level, we use class methods and static methods.

    Class methods: Used to access or modify the state of the class. if we use only class variables, we should declare such methods as a class method.
    Static methods: A static method is a general utility method that performs a task in isolation.
        Inside this method, we don’t use instance or class variable because this static method doesn’t take any parameters like self and cls.
'''

#What is Static Methods in Python
'''
1.A static method is a general utility method that performs a task in isolation. Static methods in Python are similar to those found in Java or C++.

2.A static method is bound to the class and not the object of the class. Therefore, we can call it using the class name.

3.A static method doesn’t have access to the class and instance variables because it does not receive an implicit first argument like self and cls. 
    Therefore it cannot modify the state of the object or class.

4.The class method can be called using ClassName.method_name() as well as by using an object of the class.

'''
class Employee:
    @staticmethod
    def sample(x):
        print('Inside static method', x)

# call static method
Employee.sample(10)

# can be called using object
emp = Employee()
emp.sample(10)

#Defining a static method
'''
1.Any method we create in a class will automatically be created as an instance method. We must explicitly tell Python that it is a static method 
    using the @staticmethod decorator or staticmethod() function.

2.Static methods are defined inside a class, and it is pretty similar to defining a regular function. To declare a static method:

class C:
    @staticmethod
    def f(arg1, arg2, ...): ...
'''


#Creating a static method using @staticmethod decorator
'''
1.The @staticmethod decorator is a built-in function decorator in Python to declare a method as a static method. 
    It is an expression that gets evaluated after our function is defined.

2.Example-create a static method gather_requirement() that accepts the project name and returns all requirements to complete under this project.

3.Static methods are a special case of methods. Sometimes we write code that belongs to a class, 
    but that doesn’t use the object itself at all. It is a utility method and doesn’t need an object (self parameter) 
    to complete its operation. So we declare it as a static method. 

4.Also, we can call a static method from another method of a class.
'''
print("\n\nStatic method -@staticmethod and using it in another method\n")
class Employee(object):

    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name

    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        return requirement

    # instance method
    def work(self):
        # call static method from instance method
        requirement = self.gather_requirement(self.project_name)
        print(f"Employee {self.name}`s work status says he/she")
        for task in requirement:
            print('Completed', task)
        print("")

emp = Employee('Kelly', 12000, 'ABC Project')
emp.work()
emp2 = Employee('Johny', 12000, 'XYS Project')
emp2.work()


#Advantages of a Static Method

'''

    1.Consume Less memory: Instance methods are object too, and creating them has a cost. 
        Having a static method avoids that. Let’s assume you have ten employee objects and if you create gather_requirement() 
        as a instance method then Python have to create a ten copies of this method (seperate for each object) 
        which will consume more memeory. On the other hand static method has only one copy per class.
'''
print("Ist advantage-less memory\n\n\n\n")
kelly = Employee('Kelly', 12000, 'ABC Project')
jessa = Employee('Jessa', 7000, 'XYZ Project')

print("comparing Kelly's and jessa's work are same or not")
# false
# because seperate copy of instance method is created for each object
print(kelly.work is jessa.work)

print("comparing Kelly's and jessa's gather requirement are same or not")
# True
# because only one copy is created
# kelly and jess objects share the same methods
print(kelly.gather_requirement is jessa.gather_requirement)

print("comparing Kelly's and an employee's gather requirement are same or not")
# True
print(kelly.gather_requirement is Employee.gather_requirement)

'''
    1.To Write Utility functions: Static methods have limited use because they don’t have access to the attributes of an object (instance variables) 
            and class attributes (class variables). However, they can be helpful in utility such as conversion form one type to another. 
            The parameters provided are enough to operate.
            
    2.Readabiltity: Seeing the @staticmethod at the top of the method, we know that the method does not depend on the object’s state or the class state.
'''


#staticmethod function
'''
We should only use staticmethod() function to define static method if we have to support older versions of Python (2.2 and 2.3). 
Otherwise, it is recommended to use the @staticmethod decorator.

Syntax:

staticmethod(function)

    function: It is the name of the method you want to convert as a static method.
    It returns the converted static method.
'''
#Example:

print("\n\nusing staticmethod function\n")
class Employee:
    def sample(x):
        print('Inside static method', x)

# convert to static method
Employee.sample = staticmethod(Employee.sample)
# call static method
Employee.sample(10)


#Call Static Method from Another Method
print("\n\nCall static method from a class method using cls.static_method_name()\n")
class Test :
    @staticmethod
    def static_method_1():
        print('static method 1')

    @staticmethod
    def static_method_2() :
        Test.static_method_1()

    @classmethod
    def class_method_1(cls) :
        cls.static_method_2()

# call class method
Test.class_method_1()



