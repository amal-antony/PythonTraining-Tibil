
double=lambda x: x*2
print("You can enter a limit to create a list of numbers from 1 to limit")
limit=int(input("Enter limit \n"))

# Manually enter input user
num_array=[]
for i in range(limit):
    number=int(input(f"Enter number {i+1}\n"))
    num_array.append(number)
print(num_array)
print(f"\nYour entire list is \n{num_array}\n")
result=list(map(double,num_array))
print("The newlist containing double the value of ur previous list elements are")
print(result)


'''
num_list=list(range(1,limit+1))
print(f"\nYour entire list is \n{num_list}\n")
result=list(map(double,num_list))
print("The newlist containing double the value of ur previous list elements are")
print(result)

'''