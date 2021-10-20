def swap_first_and_last(list1):
    no_of_elm=len(list1)
    for i in range(0,no_of_elm):
        if(i==0):
            temp=list1[0]
            list1[0]=list1[no_of_elm-1]
            list1[no_of_elm-1]=temp
    print("Your new list after swapping first and last elements")
    print( list1)


limit=int(input("Enter limit\n"))
inputList=[]
for i in range(limit):
   number=(input(f"Enter element {i+1}\n"))
   inputList.append(number)

print(f"Your original list \n {inputList}")
swap_first_and_last(inputList)