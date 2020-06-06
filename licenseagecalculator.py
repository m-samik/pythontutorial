print("\t=========Welcome to your Age Calculator========")
var1= 17
var2= 18
while (1):
    print("Enter Your Age")
    var3= input()
    if var3 == "exit":
        exit()
    var3 = int(var3)
    if var3>var2:
        print("You are Eligible for the Driving License")
    elif var3==var2:
        print("We will review your application because you are 18")
    else:
        print("You are Not Eligible for the Driving License")

