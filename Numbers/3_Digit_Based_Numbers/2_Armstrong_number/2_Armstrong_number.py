n = int(input("Enter Number: "))
original = n
arm = 0
length = len(str(n))
while n>0:
    digit = n%10
    arm = arm + (digit**length)
    n = n//10
if arm == original:
    print("Armstrong Number")
else:
    print("Not Armstrong")