def hcf(x, y):
    while y != 0:
        x, y = y, x % y
    return x

x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

print(f"HCF of {x} and {y} is: {hcf(x, y)}")
