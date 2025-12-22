n = int(input("Enter Number: "))

while n%3 == 0 and n>1:
    n = n//3
if n == 1:
    print("Power of 3")
else:
    print("Not Power of 3")