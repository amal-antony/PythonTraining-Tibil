def multTable(num1,num2):
    print(f"printing multiplication table of all numbers from {num1} to {num2}\n")
    for i in range(num1,num2+1):
        print(f"printing multiplication table of {i}")
        for j in range(1,11):
            print(f"{i} * {j} = {i*j}")
        print("\n")

number=int(input("enter a lower limit\n"))
number2=int(input("enter a upper limit\n"))
multTable(number,number2)