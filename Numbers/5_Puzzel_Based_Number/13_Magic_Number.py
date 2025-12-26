def magic(n):
    sum = 0

    while n>9:
        sum = 0
        while n>0:
            d = n%10
            sum += d
            n = n//10
        n = sum
    return n == 1

x = int(input("Enter Number: "))
print("Magic Number" if magic(x) else "Not Magic Number")