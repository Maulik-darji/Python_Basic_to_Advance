def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        sum_sq=0

        while n>0:
            digit = n%10
            sum_sq = digit**2
            n = n//2
        n = sum_sq
    return n == 1
num = int(input("Enter Number: "))
if is_happy(num):
    print("Happy Number")
else:
    print("Not Happy Number")