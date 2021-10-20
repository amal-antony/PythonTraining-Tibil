def recur_factorial(n):
   if n == 0 or n==1:
       return n
   elif n<0:
       return("Number should be positive\n")
   else:
       return n*recur_factorial(n-1)



num=int(input("Enter number to find factorail\n"))
result=recur_factorial(num)
print(f"The factorial is {result}")