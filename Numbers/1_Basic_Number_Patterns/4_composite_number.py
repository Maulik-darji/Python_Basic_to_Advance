n = int(input("Enter Number to Check prime: "))

if n < 2:
    print("Not Composite ")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Composite Number")
            break
    else:
        print("Not Composite")
