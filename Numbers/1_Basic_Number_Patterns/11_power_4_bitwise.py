n =int(input("Enter Number: "))
if n>0 and (n & (n-1))==0 and (n & (0x55555555)):
    print("Power of 4")
else:
    print("Not Power of 4")