def multTableTryCatch(num1,num2,lmt):
    print(f"printing multiplication table of all numbers from  {num1} to {num2} till limit {lmt-1}\n")
    for i in range(num1,num2+1):
        print(f"\nMultiplication table of {i}")
        for j in range(1,lmt):
            print(f"{i} * {j} = {i*j}")

number=int(input("enter lower limit\n"))
number2=int(input("enter upper limit\n"))
limit=10
try:
    limit=int(input("Will print table upto limit 10 , press Enter if u want to do so , else specify limit below\n"))
except ValueError:
    print("Ok u didnt enter any number so will print multiplication table till 10\n")
    print("printing multiplication table till 10\n")
multTableTryCatch(number,number2,limit+1)




