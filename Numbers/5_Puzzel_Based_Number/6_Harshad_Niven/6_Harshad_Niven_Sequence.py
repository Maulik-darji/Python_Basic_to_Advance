def har_niv(n):
    original = n
    sum_digits = 0
    while n>0:
        digit = n%10
        sum_digits += digit
        n = n//10
    return original%sum_digits == 0
ran = int(input("Enter Harshad_Niven Range: "))
for i in range(1, ran+1):
    if har_niv(i):
        print(i, end=",")