def pell(n):
    if n==0:
        return 0
    if n==1:
        return 1

    a = 0
    b = 1
    for i in range(2, n+1):
        new = 2*b + a
        a,b = b,new
    return b
ran = int(input("Enter Range: "))
for i in range(ran):
    print(pell(i))