def mod_ari(b,p,m):
    formula = ((b%m)+(p%m))%m
    return formula
b = int(input("Enter First Number: "))
p = int(input("Enter Second Number: "))
m = int(input("Enter Divisor: "))
print(f"Answer: {mod_ari(b,p,m)}")