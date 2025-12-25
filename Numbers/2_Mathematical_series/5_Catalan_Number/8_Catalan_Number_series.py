import math

def catalan(n):
    upper = math.factorial(2*n)
    lower = (math.factorial(n+1))*(math.factorial(n))
    ans = upper//lower
    return ans

ran = int(input("Enter Range For Catalan Series: "))
for i in range(1,ran+1):
    print(catalan(i))