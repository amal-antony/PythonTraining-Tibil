sume=lambda numarray: sum(num_array)

limit=int(input("Enter limit \n"))
num_array=[]
for i in range(limit):
    number=int(input(f"Enter number {i+1}\n"))
    num_array.append(number)
print(num_array)
print(f"\nYour entire list is \n{num_array}\n")
total=0
print("The sum of your list elements are")
result=sume(num_array)
print(result)
