arr = list(map(int, input("Enter numbers: ").split()))

unique = 0
for num in arr:
    unique = unique ^ num

print("Unique element is:", unique)
