def hcf(a,b):
    while b!=0:
        a,b = b,a%b
    return a
def lcm(a,b):
    return (a*b)//hcf(a,b)
x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
print(f"LCM of {x} and {y}: {lcm(x,y)}")