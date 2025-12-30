def sum_of_div(n):
    total_sum = 1
    p = 2

    while p * p <= n:
        if n % p == 0:
            power_sum = 1
            term = 1

            while n % p == 0:
                n //= p
                term *= p
                power_sum += term

            total_sum *= power_sum
        p += 1

    if n > 1:
        total_sum *= (1 + n)

    return total_sum


n = int(input("Enter Number: "))
print("Sum of divisors:", sum_of_div(n))
