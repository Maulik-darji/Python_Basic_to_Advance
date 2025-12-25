import math
n = int(input("Enter number to find nth Catalan Number: "))


upper = math.factorial(2*n)
lower = (math.factorial(n+1))*math.factorial(n)
catalan = int(upper/lower)
print(catalan)