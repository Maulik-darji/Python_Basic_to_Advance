def cube(n):
    return n*n*n

ran = int(input("Enter Range: "))
for i in range(1,ran+1):
    print(cube(i))