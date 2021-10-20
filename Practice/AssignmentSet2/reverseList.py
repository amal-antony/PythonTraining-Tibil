def reverseList(list1):
    no_of_elm=len(list1)
    newlist=[]
    for i in range(no_of_elm-1,-1,-1):
        newlist.append(list1[i])
    print(f"\nAfter reversing the list is \n{newlist}")

limit=int(input("Enter limit\n"))
inputList=[]
for i in range(limit):
   number=(input(f"Enter element {i+1}\n"))
   inputList.append(number)
print(f"\nOriginal list is \n {inputList}")
reverseList(inputList)