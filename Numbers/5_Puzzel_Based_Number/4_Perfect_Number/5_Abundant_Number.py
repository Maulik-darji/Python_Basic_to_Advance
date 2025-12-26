n = int(input("Enter Number: "))
sum_div = 0
for i in range(1, n):
    if n%i == 0:
        sum_div += i
if sum_div > n:
    print("Abundant Number")
elif sum_div < n:
    print("Deficient Number")
else:
    print("Perfect Number")