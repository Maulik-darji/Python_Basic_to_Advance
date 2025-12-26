def perfect(n):
    if n<=1:
        return False
    sum_div = 0
    for i in range(1,n):
        if n%i == 0:
            sum_div += i
    return sum_div == n
limit = int(input("Enter Range: "))
for i in range(2,limit+1):
    if perfect(i):
        print(i)