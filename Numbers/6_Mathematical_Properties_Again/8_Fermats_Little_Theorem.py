def fermat_lil(a,p):
    if p <= 1:
        return "p must be prime number"
    if a%p == 0:
        return "a must be not divisible by p"
    return pow(a,p-1,p)
a = int(input("Enter a: "))
p = int(input("Enter Prime P: "))
result = fermat_lil(a,p)
print("Result of a^(p-1) mod p: ", result)