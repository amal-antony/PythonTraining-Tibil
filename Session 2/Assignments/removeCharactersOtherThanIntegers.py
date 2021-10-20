def removeString(str1):
    newStr=""
    for i in range(len(str1)):
        if str1[i].isdigit():
            newStr+=str1[i]
    print("After removing all characters other than integers from ur given string it looks like")
    print(newStr)

enteredString=str(input("Enter your string\n"))
removeString(enteredString)