def count_div(n):
    temp = n
    total_div = 1
    i = 2
    while i*i <= n:
        power = 0
        while n%i==0:
            n //= i
            power += 1
        if power > 0:
            total_div *= power+1
        i += 1
    if n>1:
        total_div *= 2
    return total_div
num = int(input("Enter Number: "))
print("Total Divisors: ", count_div(num))