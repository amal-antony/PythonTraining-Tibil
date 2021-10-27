def printcubes(lim):
    number=1
    count=0
    print(f"Cubes of numbers from 1 to {lim}")
    while count<lim:
        print(number**3)
        count+=1
        number+=1


limit=int(input("Enter limit\n"))
printcubes(limit)