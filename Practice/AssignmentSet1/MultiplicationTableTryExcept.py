def multTableTryCatch(num1,lmt):
    print(f"printing multiplication table of {num1} till limit {lmt-1}")
    for i in range(1,lmt):
        print(f"{num1} * {i} = {num1*i}")

number=int(input("enter a number to print multiplication table\n"))
limit=10
try:
    limit=int(input("Will print table upto limit 10 , press Enter if u want to do so , else specify limit below\n"))
except ValueError:
    print("Ok u didnt enter any number so will print multiplication table till 10\n")
    print("printing multiplication table till 10\n")
multTableTryCatch(number, limit+1)




