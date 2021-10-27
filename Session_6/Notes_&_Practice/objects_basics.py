#Class Objects
'''
1.An Object is an instance of a Class.
2.A class is like a blueprint while an instance is a copy of the class with actual values.


An object consists of :

   1. State: It is represented by the attributes of an object. It also reflects the properties of an object.
   2. Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
   3. Identity: It gives a unique name to an object and enables one object to interact with other objects.

'''


#Declaring Objects
'''
1.Declaring Objects are also called instantiating a class
2.When an object of a class is created, the class is said to be instantiated. 
3.All the instances share the attributes and the behavior of the class. 
4.The values of those attributes, i.e. the state are unique for each object. 
5.A single class may have any number of instances.
'''

print("\n\nclass and declaring objects\n")
class Dog:
    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def introduce(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)


# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.introduce()

#Modify Object Properties
'''
Every object has properties associated with them. We can set or modify the object’s properties after object initialization 
by calling the property directly using the dot operator.

Obj.PROPERTY = value
'''
print("\n\nModify Object\n")
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print("Fruit is", self.name, "and Color is", self.color)

# creating object of the class
obj = Fruit("Apple", "red")

# Modifying Object Properties
obj.name = "strawberry"

# calling the instance method using the object obj
obj.show()
# Output Fruit is strawberry and Color is red



#Delete object properties
'''
We can delete the object property by using the del keyword. After deleting it, if we try to access it, we will get an error.
'''
print("\n\nDelete Object\n")
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print("Fruit is", self.name, "and Color is", self.color)

# creating object of the class
obj = Fruit("Apple", "red")

# Deleting Object Properties
del obj.name

# Accessing object properties after deleting
print(obj.name)
# Output: AttributeError: 'Fruit' object has no attribute 'name'