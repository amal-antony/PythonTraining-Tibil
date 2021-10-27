def checkValueInRange(maxlim,key,val):
   dict1 = dict(zip(key, val))
   interval=int(maxlim)+1
   intervalRange=list(range(0,interval))
   print(intervalRange)
   print("Your dictionary has the following elements in key:value format")
   for k, v in dict1.items():
      print(f"{k}:{v}")
   print("\nOut of all values in your dictonary\n")
   for i in val:
      if int(i) in intervalRange:
         print(f"Value '{i}' corresponding to key '{key[val.index(i)]}' is in the range of 0-{maxlim}")
      else:
         print(f"Value '{i}' corresponding to key '{key[val.index(i)]}' is not in the range of 0-{maxlim}")


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
searchRange=input("Enter your range to check\n")
checkValueInRange(searchRange,keyList,valueList)
