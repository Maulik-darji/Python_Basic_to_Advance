n = int(input("Enter Number of Rows: "))
for i in range(n):
    num = 1
    for j in range(i+1):
        print(num, end=" ")
        num = num * (i-j)//(j+1)
    print()