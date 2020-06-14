# Recurssive Approach for a Function
def factorial_rec(n):
    if n==1:
        return 1
    else:
        return n*factorial_rec(n-1)
n=int(input("Enter the Number\n"))
print("factorial of the Number using recurssive method is:\n",factorial_rec(n))
