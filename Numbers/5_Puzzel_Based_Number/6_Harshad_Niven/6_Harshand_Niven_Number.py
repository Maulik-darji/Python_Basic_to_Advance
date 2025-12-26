def har_niv(n):
    original = n
    sum_digit = 0
    while n>0:
        digit = n%10
        sum_digit += digit
        n = n//10
    return original%sum_digit == 0
num = int(input("Enter Number: "))
if har_niv(num):
    print("Harshad Niven Number")
else:
    print("Not Harshad Niven NUmber")