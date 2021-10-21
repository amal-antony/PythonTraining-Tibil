# 1 . Anonymous Function
'''In Python, an anonymous function is a function that is defined without a name.
While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.
Hence, anonymous functions are also called lambda functions.'''

#Lambda Function syntax
# The syntax of lambda functions are the follows
            # lambda arguments: expression
'''Lambda functions can have any number of arguments but only one expression. 
The expression is evaluated and returned. 
Lambda functions can be used wherever function objects are require.'''

#Example for a lambda function definition and call
double = lambda x: x * 2
print("\nUsing Lambda Function called double , we get the output")
print(double(5))

#without using lambda function the double function would have been in the format
def double(x):
   return x * 2
print("\nWithout Using Lambda Function called double , we create a user defined function double and gets output")
print(double(5))


#Uses of lambda Function
'''1.We use lambda functions when we require a nameless function for a short period of time.
2. In Python, we generally use it as an argument to a higher-order function (a function that takes in other functions as arguments). 
Lambda functions are used along with built-in functions like filter(), map() etc...'''


# 2 . Filter function - filter()
'''
1.The filter() function in Python takes in a function and a list as arguments.
2.The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True.
3.Example use of filter() function to filter out only even numbers from a list.
'''

# 2 arguements -
# a.function to be applied to each element in list
# b.list itself
print("\nUse of filter() function with lambda")
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(f"\nsorting out only even numbers using filter and lambda function from the list {my_list} we get following output")
print(new_list)

tables = [lambda x=x: x * 10 for x in range(1, 11)]
print("\nLambda function along with list comprehension")
print(f"{tables}")
print("Printing tables")
for table in tables:
   print(table())



# 3. Map Function- map()
'''
1.The map() function in Python takes in a function and a list.
2.The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item.
3.Example use of map() function to double all the items in a list.
'''
print("\nUse of map() function with lambda\n")
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(f"Doubling every element using lambda and map function in the list {my_list} we get following output")
print(new_list)


# 4 . Reduce Function-reduce()
'''
1. The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements 
mentioned in the sequence passed along.
2. This function is defined in “functools” module-so we must import it from itertools

3.Working :  
   a.At first step, first two elements of sequence are picked and the result is obtained.
   b.Next step is to apply the same function to the previously attained result and 
      the number just succeeding the second element and the result is again stored.
   c.This process continues till no more elements are left in the container.
   d.The final returned result is returned and printed on console.
'''

import functools
lis = [1, 3, 5, 6, 2, ] # initialized list upon which reduce operation s to be performed
print("\nUse of reduce() function with lambda\n")

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))
