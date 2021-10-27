#Install multiple dispatch
'''
Multiple dispatch or multimethods is the feature of some object-oriented programming languages in which a function or method can be dynamically
dispatched based on the run time (dynamic) type of more than one of its arguments

pip3 install multipledispatch
'''


#Example 1
def add(datatype, *args):
    # if datatype is int
    # initialize answer as 0
    if datatype == 'int':
        answer = 0

    # if datatype is str
    # initialize answer as ''
    if datatype == 'str':
        answer = ''

    # Traverse through the arguments
    for x in args:
        # This will do addition if the
        # arguments are int. Or concatenation
        # if the arguments are str
        answer = answer + x

    print(answer)


# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Geeks')


#Example2

from multipledispatch import dispatch


# passing one parameter
@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result);


# passing two parameters
@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result);


# you can also pass data type of any value as per requirement
@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result);


# calling product method with 2 arguments
product(2, 3, 2)  # this will give output of 12
product(2.2, 3.4, 2.3)  # this will give output of 17.985999999999997


