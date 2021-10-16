def checkArmstrong(num1):
    sum=0
    org_no=num1
    number_as_string=str(num1)
    order=len(number_as_string)
    while org_no>=1:
        each_place_value=org_no%10
        sum=sum+each_place_value**order
        org_no=org_no//10
    print("A number is an armstrong number if sum of every digit to the power of number of digits is equal to actual digit\n")
    print("For eg: The number 407, no of digits =3 and 4^3+0^3+7^3=407 means its an armstrong number\n")
    print(f"Here The sum is {sum}\n")
    print(f"The Number is {num1}\n")
    if(sum==num1):
        print(f"sum is equal to number entered So the number is armstrong number")
    else:
        print(f"sum is not equal to number entered , So the number is not an armstrong number")


a=int(input("enter number to check\n"))
checkArmstrong(a)