n = int(input("Enter Range: "))

first = 0
second = 1

if n >= 1:
    print(first)
if n >= 2:
    print(second)

for i in range(3, n+1):
    pell = 2*second + first
    print(pell)
    first = second
    second = pell
