




def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


'''def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")'''


'''def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")'''


def recusrs(n):
  fact = 1
  while (n > 0):
    fact = fact * n
    n = n - 1
  print("Factorial of the number is: ")
  print(fact)


n = int(input("Enter number:"))
recusrs(n)


def recursive_fibonacci(n):
  if n <= 1:
    return n
  else:
    return (recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2))


n_terms =int(input("Enter number"))

if n_terms <= 0:
  print("Invalid input ! Please input a positive value")
else:
  print("\nFibonacci series:")
  for i in range(n_terms):
    print(recursive_fibonacci(i))

#lambda functions

''' lambda arguments:expression'''
double = lambda x: x*2

double(5)