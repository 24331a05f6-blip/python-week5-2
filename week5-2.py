
n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial of",n," without recursion is:",fact)
def fact(n):
    if n==0|n==1:
        return 1
    else:
        return n*fact(n-1)
print("factorial of",n," with recursion is:",fact(n))
