#Difference
'''

1.Iterable is an object, which one can iterate over. It generates an Iterator when passed to iter() method.

2.Iterator is an object, which is used to iterate over an iterable object using __next__() method.
    Iterators have __next__() method, which returns the next item of the object.

Note that every iterator is also an iterable, but not every iterable is an iterator.
        For example, a list is iterable but a list is not an iterator.

An iterator can be created from an iterable by using the function iter().

'''

for city in ["Berlin", "Vienna", "Zurich"]:
    print(city)

print("\n")

for city in ("Python", "Perl", "Ruby"):
    print(city)

print("\n")

for char in "Iteration is easy":
    print(char, end=" ")


#Example 2
print("\n\n2.Eg:iterator vs iterable\n")
cities = ["Berlin", "Vienna", "Zurich"]

# initialize the object
iterator_obj = iter(cities)

print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))


#Example 3
print("\n\n2.Check if an object is an iterable\n")
def iterable(obj):
    try:
        iter(obj)
        return True

    except TypeError:
        return False


# Driver Code
for element in [34, [4, 5], (4, 5),
                {"a": 4}, "dfsdf", 4.5]:
    print(element, " is iterable : ", iterable(element))

#iter(34)