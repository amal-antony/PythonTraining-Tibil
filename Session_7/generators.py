#Generator-Function :
'''
A generator-function is defined like a normal function

Whenever it needs to generate a value, it does so with the yield keyword rather than return.

If the body of a def contains yield, the function automatically becomes a generator function.
'''


# A generator function that yields 1 for first time,
# 2 second time and 3 third time
print("\n\nGenerator function eg1-for loop\n")
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)

#Generator-Object :
'''
Generator functions return a generator object. 

Generator objects are used either by calling the next method on the generator object 
    or using the generator object in a “for in” loop 
'''
# A Python program to demonstrate use of
# generator object with next()

# A generator function
print("\n\nGenerator function eg2-next() method\n")


def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

a = my_gen()
next(a)
next(a)
next(a)

#Example 3
print("\n\nGenerator function eg3-next() method\n")
def simpleGenerator():
    yield 1
    yield 2
    yield 3

# x is a generator object
x = simpleGeneratorFun()

print(next(x))
print(next(x))
print(next(x))

#Example 4
print("\n\nGenerator function eg4-next() method\n")

def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
x = fib(5)

# Iterating over the generator object using next
print(next(x))  # In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))
print(next(x))




#Example 5
print("\n\nGenerator function for loop and yield\n")

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
    print(i)


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)

#Example 5
print("\n\nGenerator function -double elements of a list\n")

my_list = [1, 3, 6, 10]

a = (x**2 for x in my_list)
print(next(a))

print(next(a))

print(next(a))

print(next(a))

#next(a)
