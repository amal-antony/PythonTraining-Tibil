def multTable(num1):
    print(f"printing multiplication table of {num1}")
    for i in range(1,11):
        print(f"{num1} * {i} = {num1*i}")

number=int(input("enter a number to print multiplication table\n"))
multTable(number)