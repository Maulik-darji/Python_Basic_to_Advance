n = int(input("Enter Number: "))

print("XOR Pattern with ", n)
for i in range(1, n+1):
    print(f"{n} ^ {i} = {n^i}")