# Pattern Printer
while(1):
    def getdate():
        import datetime
        return datetime.datetime.now()
    print(getdate())
    n=int(input("Enter The No of Rows to be Printed\n"))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end="")
        print()
