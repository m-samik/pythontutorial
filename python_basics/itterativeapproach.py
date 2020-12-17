# Itterative Approach for a Function
def factorial_itr(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac
number=int(input("Enter the Nunber\n"))
print("factorial of the number using itterative method is :\n",factorial_itr(number))
