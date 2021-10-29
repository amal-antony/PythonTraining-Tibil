#try block
'''
The block that contains all our critical statements.

This is basically like programmer asking python to try executing 1/more/all the critical statements in the code.

The syntax is
                try :
                   ---critical statements---
'''


#Except block:
'''
This block takes care of the error by excepting it.

This block contains code that tells python how to handle the error or say exception.

Except block is only executed when we have an error

        The syntax is 
                except error_name/Exception:
                   ---code---

'''

#Example 1
print("\n1.Handling by Exception and not actual name in except block\n")
a=5
b=0
try:
    print(a/b)
except Exception:
    print("You cannot divide a number by zero")
print("Bye")

#Example 2
print("\n2.Handling by  actual exception name which is ZeroDivisionError in except block\n")
a=5
b=0
try:
    print(a/b)
except ZeroDivisionError:
    print("You cannot divide a number by zero")
print("Bye")



#Note-If we dont have any error it will jump out of the block and avoids executing the except block
print("\n3.When there is no error => no except block is visited\n")
a=5
b=2
try:
    print(a/b)
except ZeroDivisionError:
    print("You cannot divide a number by zero")
print("Bye")



#Printing the Exception as well - Using as keyword in except block - prints exception message
print("\n4.Printing the Exception as well - Using as keyword in except block\n")
a=5
b=0
try:
    print(a/b)
except ZeroDivisionError as e:
    print("You cannot divide a number by zero")
    print(e)
print("Bye")


#Finally Block
'''
The block of code inside a finally block will be always excuted .
It doesnt matter whether the error/exception is handled or not inside except block or the error/exception remains unhandled
    The code inside Finally block is always executed
'''

#.Demo finally block with error
print("\n5.Demo finally block with error\n")
a=5
b=0
try:
    print("Trying Division")
    print(a/b)
except ZeroDivisionError as e:
    print("You cannot divide a number by zero")
    print(e)
finally:
    print("Division attempted and completed")

print("Bye")


#Demo finally block without error
print("\n6.Demo finally block with error\n")
a = 5
b = 2
try:
    print("Trying Division")
    print(a / b)
except ZeroDivisionError as e:
    print("You cannot divide a number by zero")
    print(e)
finally:
    print("Division attempted and completed")

print("Bye")


#Demo-fILE

try:
    f = open("file2", "w")
    try:
        f.write('Hello World!')
    finally:
        f.close()
except IOError:
    print('oops!')
finally:
    print("Success\n")


#Else block in Python -optional else block
'''
This code is executed only if no exceptions were raised in the try block. 

Code executed in this block is just like normal code: if there is an exception, 
    it will not be automatically caught (and probably stop the program). 

If the else block is executed, then the except block is not, and vice versa. 
This block is optional.

    try:
           # Some Code.... 
    
    except:
           # optional block
           # Handling of exception (if required)
    
    else:
           # execute if no exception
    
    finally:
          # Some code .....(always executed)
          
    1.First try clause is executed i.e. the code between try and except clause.
    2.If there is no exception, then only try clause will run, except clause will not get executed.
    3.If any exception occurs, the try clause will be skipped and except clause will run.
    4.If any exception occurs, but the except clause within the code doesn’t handle it, it is passed on to the outer try statements. 
    5. If the exception is left unhandled, then the execution stops.
    6.A try statement can have more than one except clause.
'''

print("\n7.Try Catch with an Else\n")
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)


# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)

print("\n7.Try Catch with an Else and Finally\n")
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)
    finally:
        # this block is always executed
        # regardless of exception generation.
        print('This is always executed')

    # Look at parameters and note the working of Program


divide(3, 2)
divide(3, 0)



#Multiple Except
'''
try:
 #something1
 #something2
except ExceptionType1:
 #return xyz
except ExceptionType2:
 #return abc
 '''
#1
print("\n7.Multiple Except\n")
a,b=1,0
try:
          print(a/b)
          print("This won't be printed")
          print('10'+10)
except TypeError:
          print("You added values of incompatible types")
except ZeroDivisionError:
          print("You divided by 0")

#2
print("\n7.Multiple Except in 1 except\n")
try:
      print('10'+10)
      print(1/0)
except (TypeError,ZeroDivisionError):
      print("Invalid input")

#3
print("\n7.Generic except after all except\n")
try:
           print('1'+1)
           print(sum)
           print(1/0)
except NameError:
           print("sum does not exist")
except ZeroDivisionError:
           print("Cannot divide by 0")
except:
           print("Something went wrong")



#Raise Keyword

#1
print("\n8.Raise keyword example 1\n")

x = input("Enter integer\n")

try:
    print("Checking type")
    y = int(x)
    if not type(y) is int:
        raise TypeError
except TypeError:
    print("What u entered is not an integer")
except ValueError:
    print("What u entered is not an integer might be a string it cant be converted")
else:
    print("Well done thats an integer")





#3
print("\n8.Raise keyword example 3\n")
a=int(input("Enter Ist\n"))
b=int(input("Enter IInd\n"))
try:
    if b==0:
        raise ZeroDivisionError
except:
   print("You divided by 0")
else:
    print(f"The product is {a*b}\n")
print("Will this print?")


