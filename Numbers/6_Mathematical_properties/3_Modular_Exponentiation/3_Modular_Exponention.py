def mod_exp(a, b, m):
    result = 1
    a = a % m

    while b > 0:
        if b % 2 == 1:          # if exponent is odd
            result = (result * a) % m
        a = (a * a) % m        # square the base
        b = b // 2             # reduce exponent

    return result

a = int(input("Enter a: "))
b = int(input("Enter b: "))
m = int(input("Enter modulus m: "))

print("(a^b) % m =", mod_exp(a, b, m))
