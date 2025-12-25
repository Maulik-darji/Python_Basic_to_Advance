import math
n = int(input("Enter Number to Check if Perfect Cube: "))
x = int(math.cbrt(n))
condition = x**3
if n == condition:
    print("Perfect Cube")
else:
    print("Not Perfect Cube")