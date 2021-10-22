
def filtereven(list_of_num):
    print(f"\nYour entire list is \n{list_of_num}")
    even_no_list=[]
    for i in list_of_num:
        if(i%2==0):
            even_no_list.append(i)
    return even_no_list

# Manually enter input user
num_array=[]
print("You can enter a limit to create a list of numbers from 1 to limit")
limit=int(input("Enter limit \n"))
for i in range(limit):
    number=int(input(f"Enter number {i+1}\n"))
    num_array.append(number)
print(num_array)
print(f"\nYour entire list is \n{num_array}\n")
result=filtereven(num_array)
print(f"\nThe list of even numbers in your list are\n{result}")

'''
#list of values in specified range
print("You can enter a limit to create a list of numbers from 1 to limit")
limit=int(input("Enter limit \n"))
result=filtereven(limit)
print(f"\nThe list of even numbers in your list are\n{result}")
'''