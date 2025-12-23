n = int(input("Enter Range: "))

a = 2
b = 1

if n >= 1:
    print(a)
if n>=2:
    print(b)
for i in range(3, n+1):
    new = a+b
    print(new)
    a = b
    b = new