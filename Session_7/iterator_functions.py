#Python iterator Functions
'''
Python in its definition also allows some interesting and useful iterator functions for efficient looping and making execution of the code faster.
There are many build-in iterators in the module “itertools“.
This module implements a number of iterator building blocks.
'''

#Some useful Iterators :
'''

1. accumulate(iter, func) :- This iterator takes two arguments, iterable target and the function which would be followed at each iteration of value in target.
    If no function is passed, addition takes place by default.If the input iterable is empty, the output iterable will also be empty.

2. chain(iter1, iter2..) :- This function is used to print all the values in iterable targets one after another mentioned in its arguments.
'''

print("\n\nDemonstrating Chain and accumulate - 1 Single program\n")
import itertools

# importing "operator" for operator operations
import operator

# initializing list 1
li1 = [1, 4, 5, 7]

# initializing list 2
li2 = [1, 6, 5, 9]

# initializing list 3
li3 = [8, 10, 5, 4]

print("The actual elements of list on which accumulate is being applied")
print(li1)
# using accumulate()
# prints the successive summation of elements
print("\nThe sum after each iteration is : ", end="")
print(list(itertools.accumulate(li1)))

# using accumulate()
# prints the successive multiplication of elements
print("\nThe product after each iteration is : ", end="")
print(list(itertools.accumulate(li1, operator.mul)))

print("\nChain is going to be applied on the following lists\n")
print(li1)
print(li2)
print(li3)
# using chain() to print all elements of lists
print("\nAll values in mentioned chain are : ")
print(list(itertools.chain(li1, li2, li3)))

'''
3. chain.from_iterable() :- This function is implemented similarly as chain() but the argument here is a list of lists or any other iterable container.

4. compress(iter, selector) :- This iterator selectively picks the values to print from the passed container according to the 
    boolean list value passed as other argument. The arguments corresponding to boolean true are printed else all are skipped.
 
'''
print("\n\n2.Demonstrating Chain.from_itrerable and compress - 1 Single program\n")
import itertools

# initializing list 1
li1 = [1, 4, 5, 7]

# initializing list 2
li2 = [1, 6, 5, 9]

# initializing list 3
li3 = [8, 10, 5, 4]

# initializing list of list
li4 = [li1, li2, li3]

print("The 3 actual lists are\n")
print(li1)
print(li2)
print(li3)
print("\nAll these lists are nested to the new list\n")
print(li4)

# using chain.from_iterable() to print all elements of lists
print("\nAll values in mentioned chain are :\n ")
print(list(itertools.chain.from_iterable(li4)))

# using compress() selectively print data values
print("\nThe compressed values in string are :\n ")
print(list(itertools.compress('GEEKSFORGEEKS', [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0])))

'''
5. dropwhile(func, seq) :- This iterator starts printing the characters only after the func. in argument returns false for the first time.

6. filterfalse(func, seq) :- As the name suggests, this iterator prints only values that return false for the passed function. 
'''

print("\n\n3.Demonstrating dropwhile and filterfalse- 1 Single program\n")
import itertools

# initializing list
li = [2, 4, 5, 7, 8]
print(f"The actual list is {li}\n")

# using dropwhile() to start displaying after condition is false
print("The values after condition returns false : ", end="")
print(list(itertools.dropwhile(lambda x: x % 2 == 0, li)))

# using filterfalse() to print false values
print("The values that return false to function are : ", end="")
print(list(itertools.filterfalse(lambda x: x % 2 == 0, li)))