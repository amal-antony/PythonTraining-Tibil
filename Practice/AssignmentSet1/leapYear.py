def checkleapYear(yr):
    if(yr%100==0 and yr%4==0):
        if(yr%400==0):
            print(f"{yr} is a leap year")
        else:
            print(f"{yr} is not a leap year")
    elif(yr%4==0):
        print(f"{yr} is a leap year")
    else:
        print(f"{yr} is not a leap year")


year=int(input("enter a year to check\n"))
checkleapYear(year)