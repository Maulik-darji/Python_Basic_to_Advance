n = int(input("Enter Number: "))
x = n
while x%2 == 0 and x>1:
    x = x//2
if x == 1:
    print(f"{n} is Power of 2")
else:
    print("Not power of 2")