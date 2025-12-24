n = int(input("Enter Number: "))

original = n
sum = 0

while n > 0:
    digit = n%10
    sum = sum + digit
    n = n//10
print("Sum of Digits of Number: ", sum)