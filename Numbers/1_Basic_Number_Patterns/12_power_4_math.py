n = int(input("Enter Number: "))

while n%4 == 0 and n>1:
    n //= 4
if n == 1:
    print("Power of 4")
else:
    print("Not power of 4")