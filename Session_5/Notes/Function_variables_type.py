#Types of Variables


#1.Global Variables
'''
1.In Python, a variable declared outside of the function or in global scope is known as a global variable.
2.This means that a global variable can be accessed inside or outside of the function.
3.Example 1: Create a Global Variable
'''

x = "global"
def foo():
    print("x inside:", x)
foo()
print("x outside:", x)

'''we created x as a global variable and defined a foo() to print the global variable x. 
Finally, we call the foo() which will print the value of x.'''


#change the value of x inside a function?

x = "global"
def foo():
    x = x * 2
    print(x)
foo()

'''Python treats x as a local variable and x is also not defined inside foo().
To make this work, we use the global keyword'''


#2Local Variables
'''
1.A variable declared inside the function's body or in the local scope is known as a local variable.
2.Accessing local variable outside the scope
'''

def foo():
    y = "local"
foo()
print(y)

'''The output will show error because we are trying to access a local variable y in a global scope 
whereas the local variable only works inside foo() or local scope.
How a local variable is created in Python.'''

#Create a Local Variable
'''We declare a variable inside the function to create a local variable.'''

def foo():
    y = "local"
    print(y)
foo()

'''Problem where x was a global variable and we wanted to modify x inside foo().'''


#3.Global and local variables
'''
1.Here, we will show how to use global variables and local variables in the same code.
2.Example - Using Global and Local variables in the same code
'''

x = "global "
def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)
foo()

'''
we declare x as a global and y as a local variable in the foo(). Then, we use multiplication operator * to modify 
the global variable x and we print both x and y.

1.After calling the foo(), the value of x becomes global global because we used the x * 2 to print two times global. 
2.After that, we print the value of local variable y i.e local.'''


#Example-Global variable and Local variable with same name

x = 5
def foo():
    x = 10
    print("local x:", x)
foo()
print("global x:", x)


'''
1.we used the same name x for both global variable and local variable. We get a different result when we print the same variable 
because the variable is declared in both scopes, i.e. the local scope inside foo() and global scope outside foo().
2.When we print the variable inside foo() it outputs local x: 10. This is called the local scope of the variable.
3.Similarly, when we print the variable outside the foo(), it outputs global x: 5. This is called the global scope of the variable.
'''



# 4. Nonlocal Variables
'''
1.Nonlocal variables are used in nested functions whose local scope is not defined. T
2.This means that the variable can be neither in the local nor the global scope.
3.An example of how a nonlocal variable is used in Python.

# We use nonlocal keywords to create nonlocal variables.
Example- Create a nonlocal variable'''

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)
outer()


'''
1.There is a nested inner() function. 
2.We use nonlocal keywords to create a nonlocal variable. 
3.The inner() function is defined in the scope of another function outer().
'''