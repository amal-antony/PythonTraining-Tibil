import functools
#from functools import reduce

def sum(x,y):
    sum=x+y
    return sum

limit=int(input("Enter limit \n"))

# Manually enter input user
num_array=[]
for i in range(limit):
    number=int(input(f"Enter number {i+1}\n"))
    num_array.append(number)
print(num_array)
print(f"\nYour entire list is \n{num_array}\n")
result=functools.reduce(sum,num_array)
print("The sum of your list elements are")
print(result)


'''
num_list=list(range(1,limit+1))
print(f"\nYour entire list is \n{num_list}\n")
result=functools.reduce(sum,num_list)
print("The sum of your list elements are")
print(result)
'''