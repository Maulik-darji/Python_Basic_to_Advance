def prime_fact(n):
    factors = []
    i = 2
    while i*i <= n:
        while n%i == 0:
            factors.append(i)
            n = n//i
        i += 1
    if n>1:
        factors.append(n)
    return factors
n= int(input("Enter Number: "))
print("Prime Factors: ", prime_fact(n))