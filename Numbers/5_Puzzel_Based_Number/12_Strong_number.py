import math
def strong(n):
    x = n
    sum = 0
    while n>0:
        digit = n%10
        sum += math.factorial(digit)
        n = n//10
    return x == sum

num = int(input("Enter Number: "))
print("Strong Number" if strong(num) else "Not Strong Number")