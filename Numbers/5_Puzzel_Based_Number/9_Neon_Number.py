def neon(n):
    sum = 0
    check = n**2
    while check>0:
        digit = check%10
        sum += digit
        check = check//10
    return n == sum

x = int(input("Enter Range: "))
for i in range(1, x+1):
    if neon(i):
        print(i)
        