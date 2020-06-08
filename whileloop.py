#while(1) means it is true while statement
while(1):
    #\n is new line character
    inp=int(input("Enter Your Number\n"))
    if inp>=100:
        print("Congrats you have entered a number greater than 100")
        break
    else:
        print("Try Again!\n")
        continue
