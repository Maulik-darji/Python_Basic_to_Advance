def mod_exp(b,p,m):
    result = 1
    b = b%m

    while p>0:
        if p%2 == 1:
            result = (result*b)%m
        b = (b*2)%m
        p = p//2
    return result

b = int(input("Enter Base: "))
p = int(input("Enter Power: "))
m = int(input("Enter Divisor: "))

print(f"Answer: {mod_exp(b, p, m)}")