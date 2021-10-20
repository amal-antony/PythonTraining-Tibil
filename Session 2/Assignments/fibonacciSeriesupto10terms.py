def fibonacci(num1,num2):
    count=0
    while count<10:
        print(num1)
        next = num1 + num2
        num1 = num2
        num2 = next
        count += 1


n1=int(input("Enter first number\n"))
n2=int(input("Enter second number\n"))
fibonacci(n1,n2)