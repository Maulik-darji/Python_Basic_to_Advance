def prime_fact(n):
    print("Prime Factors: ", end=" ")
    i = 2
    while i*i<=n:
        while n%i == 0:
            print(i, end=",")
            n = n//i
        i += 1
    if n>1:
        print(n,end=",")
num = int(input("Enter Number: "))
prime_fact(num)