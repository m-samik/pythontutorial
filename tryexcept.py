try:
   print("Welcome to my Calculaor")
   f=input("Enter Your 1st Number : ")
   s=input("Enter Your 2nd Number : ")
   print("The Sum is ",int(f)+int(s))
except ValueError:
   print("Kindly enter integer values")
