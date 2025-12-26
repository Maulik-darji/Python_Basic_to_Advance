def infinite_lychrel(n):
    x = n
    while True:
        x = x + int(str(x)[::-1])
        print(x)

num = int(input("Enter number: "))
infinite_lychrel(num)
