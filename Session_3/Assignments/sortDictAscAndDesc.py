def sortAsc(key,val):
      dict1 = dict(zip(key, val))
      sorted_dict_asc = sorted(dict1.items(),key=
      lambda kv: kv[1])
      sorted_dict_desc=sorted(dict1.items(),key =
             lambda kv:kv[1],reverse=True)
      print(f"\n Sorted in ascending order of values becomes \n{sorted_dict_asc}")
      print(f"\nSorted in descending order of values becomes \n{sorted_dict_desc}")

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
sortAsc(keyList,valueList)
