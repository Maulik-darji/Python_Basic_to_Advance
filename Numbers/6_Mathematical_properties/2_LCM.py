def hcf(x,y):
    while y != 0:
        x,y = y,x%y
    return x
def lcm(x,y):
    return (x*y)//hcf(x,y)

n = int(input("Enter First Number: "))
m = int(input("Enter Second Number: "))
print(f"LCM of {n} and {m}: {lcm(n,m)}")