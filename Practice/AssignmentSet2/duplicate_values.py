def remDuplocate(inputList):
   inputDict=dict.fromkeys(inputList,0)
   outputDict=[]
   for i in inputList:
      if i in inputDict.keys():
         inputDict[i]+=1

   for m,n in inputDict.items():
      if n>1:
         outputDict.append(m)
   if len(outputDict)==0:
      print("Sorry there are no duplicate elements in your list")
   elif len(outputDict)>=1:
      print("The duplicate or repeating elements in your list is/are")
      print(" , ".join(outputDict))


limit=int(input("Enter limit\n"))
inputList=[]
for i in range(limit):
   number=(input(f"Enter element {i+1}\n"))
   inputList.append(number)

print(f"Your list is {inputList}")
remDuplocate(inputList)
