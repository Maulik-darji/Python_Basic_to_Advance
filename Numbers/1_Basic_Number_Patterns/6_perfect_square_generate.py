def square(n):
    return n*n

n = int(input("Enter Range To Generate  Perfect Square: "))
for i in range(1, n+1):
    print(square(i))