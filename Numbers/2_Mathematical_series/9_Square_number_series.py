def square(n):
    ans = n*n
    return ans

ran = int(input("Enter Range: "))
for i in range(1, ran+1):
    print(square(i))