def spy(n):
    s = 0
    p = 1
    while n>0:
        digit = n%10
        s += digit
        p *= digit
        n //= 10
    return s == p
num = int(input("Enter Number: "))
print("Spy Number" if spy(num) else "Not Spy Number")