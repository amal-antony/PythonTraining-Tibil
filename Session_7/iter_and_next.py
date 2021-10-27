# What is __iter__() function and __next__() function ?
'''
The __iter__() function returns an iterator for the given object (array, set, tuple, etc. or custom objects).

It creates an object that can be accessed one element at a time using __next__() function,
    which generally comes in handy when dealing with loops.
'''

#Syntax of iter
'''
iter(object)
iter(callable, sentinel)

    Object: The object whose iterator has to be created. It can be a collection object like list or tuple or a user-defined object (using OOPS).
    
    Callable, Sentinel: Callable represents a callable object, and sentinel is the value at which the iteration is needed to be terminated, 
        sentinel value represents the end of sequence being iterated.
        
        If we call the iterator after all the elements have been iterated, then StopIterationError is raised.

'''

#working of iter
'''
The __iter__() function returns an iterator object that goes through each element of the given object. 

The next element can be accessed through __next__() function. 

In the case of callable object and sentinel value, the iteration is done until the value is found or the end of elements reached. 

Original object is not modified.

'''
#Example 1
print("\n\nIter-basic illustration 1\n")
listA = ['a', 'e', 'i', 'o', 'u']

iter_listA = iter(listA)

try:
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))  # StopIteration error
except:
    pass

#Example 2
print("\n\nIter-basic illustration 2\n")
lst = [11, 22, 33, 44, 55]

iter_lst = iter(lst)
while True:
    try:
        print(iter_lst.__next__())
    except:
        break

#Example 3
print("\n\nIter-basic illustration 3\n")

listB = ['Cat', 'Bat', 'Sat', 'Mat']

iter_listB = listB.__iter__()

try:
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())  # StopIteration error
except:
    print(" \nThrowing 'StopIterationError'",
          "I cannot count more.")

#Example 4
print("\n\nIter-basic illustration 3 - without try block to show stopiteration error\n")

listB = ['Cat', 'Bat', 'Sat', 'Mat']

iter_listB = listB.__iter__()

print(iter_listB.__next__())
print(iter_listB.__next__())
print(iter_listB.__next__())
print(iter_listB.__next__())
#print(iter_listB.__next__())  # StopIteration error



#Example 4
print("\n\nIter-basic illustration 4 - OOP - With and without iter\n")
class Counter:
    def __init__(self, start, end):
        self.num = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            self.num += 1
            return self.num - 1


# Driver code
if __name__ == '__main__':

    a, b = 2, 5

    c1 = Counter(a, b)
    c2 = Counter(a, b)

    # Way 1-to print the range without iter()
    print("Print the range without iter()-using a for loop")

    for i in c1:
        print("Eating more Pizzas, counting ", i, end="\n")

    print("\nPrint the range using iter() and next()\n")

    # Way 2- using iter()
    obj = iter(c2)
    try:
        while True:  # Print till error raised
            print("Eating more Pizzas, counting ", next(obj))
    except:
        # when StopIteration raised, Print custom message
        print("\nDead on overfood, GAME OVER")
