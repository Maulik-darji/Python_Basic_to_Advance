def palin(n):
    original = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    return original == rev


x = int(input("Enter Range of Palindrome: "))
for i in range(x):
    if palin(i):
        print(i)
