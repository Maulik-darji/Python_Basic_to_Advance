def kaprekar(n):
    x = n*n
    div = len(str(x))//2
    if div == 0:
        return n == 1
    right = x%(10**div)
    left = x//(10**div)
    if right == 0:
        return False
    return left + right == n
num = int(input("Enter Number: "))
if kaprekar(num):
    print("Kaprekar Number")
else:
    print("Not Kaprekar Number")