#What is an Exception
'''
An event that occurs during the excecution of a program, that disrupts the normal flow of program instructions

A disruption b/w the code that prevents smooth flow of program excecution.
'''


def divbyzero(a):
    return a/0
    print("When dividing by zero\n")
    print("U know its ot going to work right ?")

n=int(input("enter number\n"))
divbyzero(n)
print("Thats impossible")



#What is Exception Handling ?
'''
The process of responding to occurence of an exception.
During compilation of exceptional statements during computations.
Requires special processing - might change the normal flow of execution.
'''

#HOw is Exception Handled ?
'''
Exceptions can be handled using python blocks such as
    1.try
    2.except
    3.finally
    4.raise
'''
