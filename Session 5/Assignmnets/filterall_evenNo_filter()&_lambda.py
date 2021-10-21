
print("You can enter a limit to create a list of numbers from 1 to limit")
limit=int(input("Enter limit \n"))


# Manually enter input user
num_array=[]
for i in range(limit):
    number=int(input(f"Enter number {i+1}\n"))
    num_array.append(number)
print(num_array)
print(f"\nYour entire list is \n{num_array}\n")
filtered=lambda x:x%2==0
result=list(filter(filtered,num_array))
print(f"The even numbers in your list are \n{result}")

'''
# just random range
num_list=list(range(1,limit+1))
print(f"\nYour entire list is \n{num_list}\n")
filtered=lambda x:x%2==0
result=list(filter(filtered,num_list))
print(f"The even numbers in your list are \n{result}")

'''
