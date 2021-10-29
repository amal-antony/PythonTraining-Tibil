#What are Errors ?
'''
Errors are the problems in a program due to which the program will stop the execution.

Errors cannot be handled.

An Error might indicate critical problems that a reasonable application should not try to catch

Errors are a form of an unchecked exception and are irrecoverable
'''

#Types of Errors:

#1.Syntax Error/Compile Time Error:
'''
This is usually caused diue to wrong syntax in our code .

Syntax errors often called as parsing errors, are predominantly caused when the parser detects a syntactic issue in your code.
'''
#Example 1

a = 8
b = 10
c = a b

#Example 2

amount = 10000
if (amount > 2999)
    print("You are eligible to purchase Dsa Self Paced")

#2.Intendation Errors:
'''
Indentation error is similar in spirit to the syntax error and falls under it. 

Specific to the only indentation related issues in the script.
'''

#Example
for i in range(10):
    print('Hello world')


#3.Logical Errros
'''
When in the runtime an error that occurs after passing the syntax test is called exception or logical type. 

For example, when we divide any number by zero then the ZeroDivisionError exception is raised.

when we import a module that does not exist then ImportError is raised.

When we get an unexpected output i.e the output we get isnt the exact output we wanted but we didnt see any compile time errors.
'''

#Example
x = float(input('Enter a number: '))
y = float(input('Enter a number: '))

z = x+y/2
print ('The average of the two numbers you have entered is:',z)



#4.Runtime Errors
'''
No syntactical error , no logical error but program doesnt give output in every case .

One reason can be wrong input from user
Network issues that causes an error in Banking software etc..
'''

#Example 1
marks = 10000
a = marks / 0
print(a)

#Other Types of Errors

#1.IndexError   -   When the wrong index of a list is retrieved.
L1=[1,2,3]
L1[3]

#2.AssertionError   -   It occurs when the assert statement fails
'''
An expression is tested, and if the result comes up false, an exception is raised.

Programmers often place assertions at the start of a function to check for valid input, 
    and after a function call to check for valid output.
    
    assert Expression[, Arguments]
'''

def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32
print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(-5))

#3.AttributeError   -   It occurs when an attribute assignment is failed.

'''
AttributeError can be defined as an error that is raised when an attribute reference or assignment fails. 
'''

X = 10
X.append(6)
y=[1,2,3]
y.append(4)


class Gone():

    def __init__(self):
        self.a = 'Gone for ever'


obj = Gone()
print(obj.a)
print(obj.b)

#4.ImportError  -   It occurs when an imported module is not found.

from math import cube

#5.KeyError     -   It occurs when the key of the dictionary is not found.

D1={'1':"aa", '2':"bb", '3':"cc"}
D1['4']

#6.NameError    -   It occurs when the variable is not defined.
print(age)

#7.MemoryError	    -        It occurs when a program runs out of memory.

'''
A memory error means that your program has ran out of memory. 
This means that your program somehow creates too many objects.

Memory errors are mostly dependent on your systems RAM and are related to Heap. 
If we have large objects (or) referenced objects in memory,


'''

#8.TypeError	     -       It occurs when a function and operation are applied in an incorrect type.
a='2'
b=2
a+b

#9.ZeroDivisionError    -   The ZeroDivisionError is thrown when the second operator in the division is zero.
x=100/0



#How Exception Differs ?
'''
Exception is actually a kind of error itself - a type of logical error

An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions. 

In general, when a Python script encounters a situation that it cannot cope with, it raises an exception.
 
An exception is a Python object that represents an error.

When a Python script raises an exception, it must either handle the exception immediately otherwise it terminates and quits.
'''
