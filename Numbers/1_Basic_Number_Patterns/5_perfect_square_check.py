import math
n = int(input("Enter Number to Check if Perfect Square: "))

x = int(math.sqrt(n))

condition = x * x
if condition:
    print("Perfect Square")
else:
    print("Not Perfect Square")