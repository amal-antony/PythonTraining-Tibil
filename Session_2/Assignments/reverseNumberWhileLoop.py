def reverseNum(num1):
    org_no=num1
    rev_num=""
    while org_no>=1:
        digit=org_no%10
        rev_num+=str(digit)
        org_no=org_no//10
    print(f"The number when reversed becomes {rev_num}")


number=int(input("enter a number to reverse\n"))
reverseNum(number)