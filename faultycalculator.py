#Program for developing a faulty calculator
print("Welcome basic calculator by iamsami.XYZ")
print("Enter First Number")
n1 = int(input())
print("Enter 2nd Number")
n2 = int(input())
#mathematical operation to be performed
print("Mathematical Operation to be Performed:+,-,/,*")
n3 = input()
if n1 ==45 and n2 ==3 and n3 =='*':
    print("555")
elif n1 ==56 and n2 ==9 and n3 =='+':
    print("77")
elif n1 ==56 and n2 ==6 and n3 =='/':
    print("4")
elif n3 =='*':
    n4= (n1*n2)
    print(n4)
elif n3 =='+':
    add=(n1+n2)
    print(add)
elif n3 =='/':
    div =(n1/n2)
    print(div)
elif n3 =='-':
    minus=(n1-n2)
    print(minus)
else:
    print("Oops! Wrong Input")