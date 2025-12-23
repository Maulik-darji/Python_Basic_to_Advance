def triangular(n):
    ans = (n*(n+1))//2
    return ans

n = int(input("Enter Range: "))
for i in range(1,n+1):
    print(triangular(i))