n = int(input("Enter First Term: "))
d = int(input("Enter Common Difference: "))
ran = int(input("Enter Range: "))

container = []

for i in range(ran):
    container.append(n)
    n = n+d
print(container)