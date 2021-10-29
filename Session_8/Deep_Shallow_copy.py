#
'''
 Assignment statements do not copy objects, they create bindings between a target and an object.

It only creates a new variable that shares the reference of the original object.

Sometimes a user wants to work with mutable objects, in order to do that user looks for a way to create “real copies” or “clones” of these objects.

If a user wants copies that user can modify without automatically modifying the original at the same time, in order to do that we create copies of objects.
'''


#DeepCopy
'''
Deep copy is a process in which the copying process occurs recursively. 

 First constructing a new collection object and then recursively populating it with copies of the child objects found in the original. 
 
In case of deep copy, a copy of object is copied in other object. 

Any changes made to a copy of object do not reflect in the original object. 
'''
print("\n\nDeep Copy\n")
import copy

# initializing list 1
li1 = [1, 2, [3, 5], 4]

# using deepcopy to deep copy
li2 = copy.deepcopy(li1)

# original elements of list
print("The original elements before deep copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")

print("\r")

# adding and element to new list
li2[2][0] = 7

# Change is reflected in l2
print("The new list of elements after deep copying ")
for i in range(0, len(li1)):
    print(li2[i], end=" ")

print("\r")

# Change is NOT reflected in original list
# as it is a deep copy
print("The original elements after deep copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")


#
'''
A shallow copy means constructing a new collection object and then populating it with references to the child objects found in the original. 

The copying process does not recurse and therefore won’t create copies of the child objects themselves. 

In case of shallow copy, a reference of object is copied in other object. 

Any changes made to a copy of object do reflect in the original object. In python, this is implemented using “copy()” function.
'''
print("\n\nShallow Copy\n")
import copy

# initializing list 1
li1 = [1, 2, [3, 5], 4]

# using copy to shallow copy
li2 = copy.copy(li1)

# original elements of list
print("The original elements before shallow copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")

print("\r")

# adding and element to new list
li2[2][0] = 7

# checking if change is reflected
print("The original elements after shallow copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")