#Abstraction
'''
Abstraction is used to hide the internal functionality of the function from the users.
The users only interact with the basic implementation of the function, but inner working is hidden.
User is familiar with that "what function does" but they don't know "how it does."
'''
#Why Abstraction important
'''
1.An abstraction is used to hide the irrelevant data/class in order to reduce the complexity. 
2.It also enhances the application efficiency

'''


#Abstraction classes in Python
'''
In Python, abstraction can be achieved by using abstract classes and interfaces.

1.A class that consists of one or more abstract method is called the abstract class. 
2.Abstract methods do not contain their implementation. 
3.Abstract class can be inherited by the subclass and abstract method gets its definition in the subclass. 
4.Abstraction classes are meant to be the blueprint of the other class. 
5.An abstract class can be useful when we are designing large functions. 
6.An abstract class is also helpful to provide the standard interface for different implementations of components. 
7.Python provides the abc module to use the abstraction in the Python program. Let's see the following syntax.

    from abc import ABC  
    class ClassName(ABC):  

'''

#Abstract Base Classes
'''
An abstract base class is the common application program of the interface for a set of subclasses. 
It can be used by the third-party, which will provide the implementations such as with plugins. 
It is also beneficial when we work with the large code-base hard to remember all the classes.
'''

#Working of the Abstract Classes
'''
Unlike the other high-level language, Python doesnt provide the abstract class itself.
We need to import the abc module, which provides the base for defining Abstract Base classes (ABC). 
The ABC works by decorating methods of the base class as abstract. 
It registers concrete classes as the implementation of the abstract base. 
We use the @abstractmethod decorator to define an abstract method or if we dont provide the definition to the method, 
it automatically becomes the abstract method
'''


print("\n\nAbstract class -Example 1\n")
from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")


class Renault(Car):
    def mileage(self):
        print(f"The mileage is 27kmph ")

    # Driver code


t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()

#Example 2-Abstract Class
print("\n\nExample 2-Abstract Class\n")
from abc import ABC


class Polygon(ABC):

    # abstract method
    def sides(self):
        pass


class Triangle(Polygon):

    def sides(self):
        print("Triangle has 3 sides")


class Pentagon(Polygon):

    def sides(self):
        print("Pentagon has 5 sides")


class Hexagon(Polygon):

    def sides(self):
        print("Hexagon has 6 sides")


class square(Polygon):

    def sides(self):
        print("Square have 4 sides")

    # Driver code


t = Triangle()
t.sides()

s = square()
s.sides()

p = Pentagon()
p.sides()

k = Hexagon()
k.sides()

#Example 3-Abstract Class
print("\n\nExample 3-Abstract Class\n")

from abc import ABC, abstractmethod


class Animal(ABC):

    def move(self):
        pass


class Human(Animal):

    def move(self):
        print("I can talk , walk and run")


class Snake(Animal):

    def move(self):
        print("I can crawl")


class Dog(Animal):

    def move(self):
        print("I can bark,walk and run")


class Lion(Animal):

    def move(self):
        print("I can roar, walk and run")


# Driver code
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()

