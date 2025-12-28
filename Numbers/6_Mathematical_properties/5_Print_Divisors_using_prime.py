def count_divisors(n):
    total = 1
    i = 2

    while i * i <= n:
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        if count > 0:
            total *= (count + 1)
        i += 1

    if n > 1:        # remaining prime factor
        total *= 2

    return total


n = int(input("Enter number: "))
print("Number of divisors:", count_divisors(n))
