#Dynamic Typing:
'''
In Dynamic Typing, type checking is performed at runtime. For example, Python is a dynamically typed language.
It means that the type of a variable is allowed to change over its lifetime.
Other dynamically typed languages are -Perl, Ruby, PHP, Javascript etc.
'''
print("Dynamic Typing")
print("\n Eg 1\n")
a = "hello"
print(type(a))

## variable a is assigned to an integer
a = 5
print(type(a))

print("\n Eg 2\n")
def add(a, b):
    return a + b


## calling the function with string
print(add('hello', 'world'))

## calling the function with integer
print(add(2, 4))

#Static Typing:
'''
Static Typing is opposite to Dynamic Typing. In Static Typing, type checking is performed during compile time. 
It means that the type of a variable is known at compile time. 
For some languages, the programmer must specify what type each variable is (e.g C, C++, Java), 
other languages offer some form of type inference(e.g. Scala, Haskell).
With Static Typing, variables generally are not allowed to change types.
Let’s look at a simple example from a statically typed language. Consider the following Java snippet;
'''
#String a;
#a = "Java is good";
'''
The first line declares that the variable “a” is bound to the string type at compile time. 
In the second line, “a” is assigned a value which is not a string object. 
For example, if we say, a =5, the compiler would raise an error because of incompatible types.
Duck Typing
'''

#Duck Typing
'''
It is a concept related to Dynamic Typing, where the type or the class of an object is less important than the method it defines.
Using Duck Typing, we do not check types at all. Instead we check for the presence of a given method or attribute.
The reason behind the name is the duck test: “If it looks like a duck, swims like a duck, and quack like a duck, then it probably is a duck”.
'''

print("\n\nDuck Typing\n")
class Duck:
    def quack(self):
        print("Quack")


class Goose:
    def quack(self):
        print("Quack Quack")


class Dog:
    def bark(self):
        print("I just bark")


class ItQuacks:
    def __init__(self, animal):
        animal.quack()


ItQuacks(Duck())
ItQuacks(Goose())
ItQuacks(Dog())
