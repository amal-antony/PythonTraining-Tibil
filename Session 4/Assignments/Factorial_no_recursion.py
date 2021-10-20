def recusrs(n):
    fact = 1
    while (n > 0):
        fact = fact * n
        n = n - 1
    print("Factorial of the number is: ")
    print(fact)

n=int(input("Enter number:"))
recusrs(n)
