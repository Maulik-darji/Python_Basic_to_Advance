def euler_tot(n):
    result = n
    i = 2
    while i*i <= n:
        if n%i == 0:
            while n%i == 0:
                n = n//i
            result = result - (result//i)
        i += 1
    if n>1:
        result -= result//n
    return result
num = int(input("Enter Number: "))
print("Eulers Totient Value: ", euler_tot(num))