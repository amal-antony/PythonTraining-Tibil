def iterateDict(key,val):
    dict1=dict(zip(key,val))
    print("Your dictionary has the following elements in key:value format")
    for k,v in dict1.items():
        print(f"{k}:{v}")


limit=int(input("Enter limit\n"))
keyList=[]
valueList=[]
for i in range(limit):
   k=(input(f"Enter key {i+1}\n"))
   v = (input(f"Enter value {i + 1}\n"))
   keyList.append(k)
   valueList.append(v)
print(f"\nKeys are {keyList}")
print(f"Corresponding Values are  {valueList}")
iterateDict(keyList,valueList)