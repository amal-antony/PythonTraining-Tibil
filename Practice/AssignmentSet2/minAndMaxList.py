def minandmax(list1):
    no_of_elm=len(list1)
    min=list1[0]
    max=list1[no_of_elm-1]
    for i in range(0,no_of_elm):
        if list1[i]<min:
            min=list1[i]
        elif list1[i]>max:
            max=list1[i]
    return(f"{min} and {max}")


limit=int(input("Enter limit\n"))
inputList=[]
for i in range(limit):
   number=int((input(f"Enter element {i+1}\n")))
   inputList.append(number)

print(f"Your original list \n {inputList}")
print(f"\nThe minimum and maximum value in your list are {minandmax(inputList)} respectively")