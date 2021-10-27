double = lambda x: x * 2
print(double(5))

def double(x):
   return x * 2
print(double(5))

print("\nUse of filter() function with lambda")
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(f"\nsorting out only even numbers using filter and lambda function from the list {my_list} we get following output")
print(new_list)


#lambda with list comprehension
tables = [lambda x=x: x * 10 for x in range(1, 11)]
print("\nLambda function along with list comprehension")
print(f"{tables}")
print("Printing tables")
for table in tables:
   print(table())

print("\nUse of map() function with lambda\n")
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(f"Doubling every element using lambda and map function in the list {my_list} we get following output")
print(new_list)

import functools
lis = [1, 3, 5, 6, 2, ] # initialized list upon which reduce operation s to be performed
print("\nUse of reduce() function with lambda\n")

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))




