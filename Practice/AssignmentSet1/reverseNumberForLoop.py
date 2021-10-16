def reverseNum(num1):
    org_no=str(num1)
    no_of_digits=len(org_no)
    rev_num=""
    for i in range(no_of_digits-1,-1,-1):
       rev_num+=org_no[i]
    print(int(rev_num))


number=int(input("enter a number to reverse\n"))
reverseNum(number)