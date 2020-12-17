#Calcuator which makes three calculations wrong !!!
#45x3=120 , 56+9=69 , 56/6=9 , 129-11=116
print("\t =====Hello Welcome to My Faulty Calculator===== ")
print('Enter Your 1st Number')
num1= int(input())
print('Choose Your Mathematical Operation: +,-,/,*')
num3= input()
print('Enter Your 2nd Number')
num2= int(input())
if num1==45 and num2==3 and num3=='*':
    print("120")
elif num1==56 and num2==9 and num3=='+':
    print("69")
elif num1==56 and num2==6 and num3=='/':
    print("9")
elif num1==129 and num2==11 and num3=='-':
    print("116")
elif num3=='*':
    cross=(num1*num2)
    print(cross)
elif num3=='+':
    add=(num1+num2)
    print(add)
elif num3=='/':
    div=(num1/num2)
    print(div)
elif num3=='-':
    sub=(num1-num2)
    print(sub)
else:
    print("Wrong Input")

