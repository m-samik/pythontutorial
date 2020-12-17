#Operators in Pyhton
#Arithematic Operator-->Helps in numerical calculations
print("62+8 is ",62+8)#-->Addition
print("5**3 is", 5**3)#-->To the power(Square)
print("5-3 is ",5-3)#-->Subtraction
print("5*3 is ",5*3)#--> Multiplication
print("15 / 3 is",15/3)#-->Division
print("15%5 is ",15%5)#-->Remainder

#Assignment Operator--> Assigns a Value to a variablle or anything else...
x=5
print(x) #-->prints out x as the value for 5
x+=7 #-->+= Adds the given number to x
print(x)

#Comparission Operator
i=5
#if i==5 it prints the right output i.e; True
print(i==5)#--> Determines whether i is equal to 5 or not
#if i==7 it prints the wrong output i.e; False
print(i==10)

#Logical Opertaor
a= True
b= False
# ---and--- Logical Operator
#prints true when both conditions are true for each other
print(a and a)#--> True
#prints false when both conditions are false for each other
print(a and b)#--> False
# ---or--- Logical Operator
#prints true when one of the both conditions are true
print(a or b)

# Identity Operators
# is and is not operator
# ----is---- operator
print(a is b)
print(a is a)
# ----is not---- operator
print(a is not b)
print(a is not a)

# Membership Operator
# in and not in
# ----in--- operator
list=[3,45,78,897,456,524,42,54,65,578,1,23,24,26,72]
print(578 in list)#--> True
# ----not in---- operator
print(786 not in list) #--> True

# Bitwise operator
# Includes Bolean Knowledge
