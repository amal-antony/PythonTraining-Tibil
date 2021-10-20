# This python files contains info about he basics of lists and list operations

'''A Python list is an ordered and changeable collection of data objects. Unlike an array,
which can contain objects of a single type,
a list can contain a mixture of objects'''

#creating list
print("creating list")
myList1 = [20, 'Expresso', [1, 2, 3], 3.142, None]
print("\n")

#using list() constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
print("\n")

# Initializing an empty list
print("Initializing an empty list")
myList2 = []
print(myList2)
print("\n")

print("\nLIST METHODS\n")
'''Method 	        Description
append()	Adds an element at the end of the list
clear()	     Removes all the elements from the list
copy()	      Returns a copy of the list
count()	      Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	      Removes the element at the specified position
remove()	    Removes the item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list'''

'''A list element can be accessed using its index. The index is the position of an element in the list.
Similar to other languages, Python list elements are indexed from 0. 
This means that the first element will be at the 0 index.
To access an element, its index is enclosed in the [] brackets'''
# Accessing list elements
print("Accessing list elements")
myIntList = [1,3,5,2,4]
print(myIntList[3]) # Accessing the 4th element
print("\n")

'''The size of a list is not fixed. Elements can be added and removed at any point.'''
# Adding or removing list elements
print("Adding or removing list elements")
myList = ['a', 'b', 'c', 'd', 'e', 'f']
print("\n")

# Add an element at the end
print("Add an element at the end")
myList.append('g')
print(myList)
print("\n")

# Insert element at a specific index
# insert(index, value)
#To insert a list item at a specified index, use the insert() method.
#The insert() method inserts an item at the specified index:
print("Insert element at a specific index")
myList.insert(3, 'z') # Insertion at the 3rd index
print(myList)
print("\n")
#Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
print("\n")

#Extend
#To append elements from another list to the current list, use the extend() method.
#Add the elements of tropical to thislist:
print("Extend")
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
print("\n")

#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
#Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
print("\n")

print("LIST SLICING")
'''Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.
Return the third, fourth, and fifth item:'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

'''Note: The search will start at index 2 (included) and end at index 5 (not included).
The first item has index 0.
By leaving out the start value, the range will start at the first item:
This example returns the items from the beginning to, but NOT including, "kiwi":'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

'''By leaving out the end value, the range will go on to the end of the list:
This example returns the items from "cherry" to the end:'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

'''Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the list:
This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

'''Check if Item Exists
To determine if a specified item is present in a list use the in keyword:
Check if "apple" is present in the list:'''
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


print("\n Remove Methods")
# Delete an element from the end
#.pop
print("Delete an element from the end")
myList.pop()
print(myList)
print("\n")

# Delete the value at a specific index
#del
print("Delete the value at a specific index")
del myList[1]
print(myList)
print("\n")

#The remove() method removes the specified item.
#Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index
#The pop() method removes the specified index.
#Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


#If we do not specify the index, the pop() method removes the last item.
#Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#The del keyword also removes the specified index:
#Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely.
#Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist

#Clear the List
#The clear() method empties the list.
#The list still remains, but it has no content.
#Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Accessing the length of a list
#len
print("Accessing the length of a list")
print(len(myList))
print("\n")

print("LOOP THROUGH LIST\n")
#Loop Through a List
#We can loop through the list items by using a for loop:


#Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


#Loop Through the Index Numbers
#we can also loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
#Print all items by referring to their index number:
print("\n using for loop with range and len")
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#The iterable created in the example above is [0, 1, 2].


#Using a While Loop
#We can loop through the list items by using a while loop.
#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.
#Remember to increase the index by 1 after each iteration.
#Print all items, using a while loop to go through all the index numbers
print("\n using while loop")
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Looping Using List Comprehension
print("\nUsing List comprehension")
#List Comprehension offers the shortest syntax for looping through lists:
#A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


#List Comprehension
print("List Comprehension in Detail")

'''List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
Without list comprehension you will have to write a for statement with a conditional test inside:'''

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

'''With list comprehension you can do all that with only one line of code:'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#The Syntax
#newlist = [expression for item in iterable if condition == True]

'''The return value is a new list, leaving the old list unchanged.'''

'''Condition

The condition is like a filter that only accepts the items that valuate to True.
eg :Only accept items that are not "apple":'''

newlist = [x for x in fruits if x != "apple"]

#The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
#The condition is optional and can be omitted:
#With no if statement:
newlist = [x for x in fruits]


'''Iterable
The iterable can be any iterable object, like a list, tuple, set etc.
Example
we can use the range() function to create an iterable:'''

newlist = [x for x in range(10)]

'''Same example, but with a condition:
Accept only numbers lower than 5:'''

newlist = [x for x in range(10) if x < 5]

'''Expression
The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
Set the values in the new list to upper case:'''
newlist = [x.upper() for x in fruits]

'''You can set the outcome to whatever you like:
Set all values in the new list to 'hello':'''
newlist = ['hello' for x in fruits]

'''The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
Return "orange" instead of "banana":'''
newlist = [x if x != "banana" else "orange" for x in fruits]

'''The expression in the example above says:
Return the item if it is not banana, if it is banana return orange".'''


print("\nSORT LIST ELEMENTS\n")
'''Sort List Alphanumerically
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
Sort the list alphabetically:'''
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


#Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort Descending
'''To sort descending, use the keyword argument reverse = True:
Sort the list descending:'''
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


#Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


'''Customize Sort Function
You can also customize your own function by using the keyword argument key = function.
The function will return a number that will be used to sort the list (the lowest number first):
Sort the list based on how close the number is to 50:'''
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


#Case Insensitive Sort
'''By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
Case sensitive sorting can give an unexpected result:'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

'''we can use built-in functions as key functions when sorting a list.
So if you want a case-insensitive sort function, use str.lower as a key function:
Perform a case-insensitive sort of the list:'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


'''Reverse Order
if we want to reverse the order of a list, regardless of the alphabet?
The reverse() method reverses the current sorting order of the elements.
Reverse the order of the list items:'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

print("CHANGING LIST ELEMENTS\n")
'''Change Item Value
To change the value of a specific item, refer to the index number:
Change the second item:'''
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

'''Change a Range of Item Values
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

'''If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
Change the second value by replacing it with two new values:'''
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

'''Note: The length of the list will change when the number of items inserted does not match the number of items replaced.
If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
Change the second and third value by replacing it with one value:'''
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


print("\nCOPYING LISTS\n")
'''Copy a List
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
There are ways to make a copy, one way is to use the built-in List method copy().
Make a copy of a list with the copy() method:'''
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

'''Another way to make a copy is to use the built-in method list().
Make a copy of a list with the list() method:'''
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

print("\nJoin Two Lists\n")
'''There are several ways to join, or concatenate, two or more lists in Python.
One of the easiest ways are by using the + operator.
Join two list:'''
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

'''Another way to join two lists is by appending all the items from list2 into list1, one by one:
Append list2 into list1:'''
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)

print(list1)

'''Or you can use the extend() method, which purpose is to add elements from one list to another list:
Use the extend() method to add list2 at the end of list1:'''
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)











