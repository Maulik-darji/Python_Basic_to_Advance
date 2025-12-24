n = int(input("Enter Number: "))

original = n
product = 1

while n>0:
    digit = n%10
    product = product*digit
    n //= 10
print("Product of Digits of Number: ", product)