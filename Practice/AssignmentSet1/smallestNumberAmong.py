def checkSmallest(num1,num2,num3):
    if(num1<num2):
        if(num1<num3):
            print(f"{num1} is the smallest")
        else:
            print(f"{num3} is the smallest")
    else:
        if (num2<num3):
            print(f"{num2} is the smallest")
        else:
            print(f"{num3} is the smallest")


a=int(input("enter first number\n"))
b=int(input("enter second number\n"))
c=int(input("enter third number\n"))
checkSmallest(a,b,c)