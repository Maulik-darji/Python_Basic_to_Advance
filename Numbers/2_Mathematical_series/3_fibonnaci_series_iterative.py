ran = int(input("Enter range to print Fibonacci series: "))

first = 0
second = 1

if ran >= 1:
    print(first)

if ran >= 2:
    print(second)

for i in range(3, ran + 1):
    new = first + second
    print(new)
    first = second
    second = new
