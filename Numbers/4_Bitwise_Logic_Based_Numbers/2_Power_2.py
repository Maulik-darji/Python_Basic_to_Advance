n = int(input("Enter Number: "))

if n>0 and (n & (n-1)== 0):
    print(f"{n} is power of 2")
else:
    print(f"{n} is not power of 2")