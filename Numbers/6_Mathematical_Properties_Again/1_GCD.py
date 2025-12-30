def gcd(x,y):
    while y!=0:
        x,y = y,x%y
    return x
n = int(input("Enter First Number: "))
m = int(input("Enter Second Number: "))
print(f"GCD of {n} and {m}: ", gcd(n,m))