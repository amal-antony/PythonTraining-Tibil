mytuple = ("apple", "banana", "cherry")

'''Tuple Items

Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
Ordered

When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
Unchangeable

Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
Allow Duplicates

Since tuples are indexed, they can have items with the same value:'''

#Accessing
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

'''Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

But there are some workarounds.
Change Tuple Values

Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
Example

Convert the tuple into a list to be able to change it:'''
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Add Items

'''Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.

1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
Example

Convert the tuple into a list, add "orange", and convert it back into a tuple:'''
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

'''2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
Example

Create a new tuple with the value "orange", and add that tuple:'''
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

'''Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.
Remove Items

Note: You cannot remove items in a tuple.

Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
Example

Convert the tuple into a list, remove "apple", and convert it back into a tuple:'''
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

'''Or you can delete the tuple completely:
Example

The del keyword can delete the tuple completely:'''
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

'''Join Two Tuples

To join two or more tuples you can use the + operator:
Example

Join two tuples:'''
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

'''Multiply Tuples

If you want to multiply the content of a tuple a given number of times, you can use the * operator:
Example

Multiply the fruits tuple by 2:'''
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

'''count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found'''

'''Loop Through a Tuple

You can loop through the tuple items by using a for loop.
Example

Iterate through the items and print the values:'''
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

'''Learn more about for loops in our Python For Loops Chapter.
Loop Through the Index Numbers

You can also loop through the tuple items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.
Example

Print all items by referring to their index number:'''
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


#Using a While Loop

'''You can loop through the list items by using a while loop.

Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by refering to their indexes.

Remember to increase the index by 1 after each iteration.
Example

Print all items, using a while loop to go through all the index numbers:'''

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1