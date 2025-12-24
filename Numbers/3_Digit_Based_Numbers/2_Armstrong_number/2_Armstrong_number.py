n = int(input("Enter Number: "))
original = n
arm = 0
convert = str(n)
length = len(convert)
while n>0:
    digit = n%10
    arm = arm + (digit**length)
    n = n//10
if arm == original:
    print("Armstrong Number")
else:
    print("Not Armstrong")