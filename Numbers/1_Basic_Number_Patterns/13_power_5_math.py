n =int(input("Enter Number: "))

while n%5 == 0 and n>1:
    n //= 5
if n == 1:
    print("Power of 5")
else:
    print("Not power of 5")