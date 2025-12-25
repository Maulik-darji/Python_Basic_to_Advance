def fact(n):
    if n == 0 or n == 1:
        return 1
    return n*fact(n-1)
b = int(input("Enter Number to find Catalan: "))
x = b

upper = (2*b)
la = (b)
lb = (b+1)
lower = (la)*(lb)
ans = fact(upper)/(fact(la)*fact(lb))
print(int(ans))

