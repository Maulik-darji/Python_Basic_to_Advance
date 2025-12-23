ran = int(input("Enter Range To Print Tribonacci: "))

first = 0
second = 1
third = 1

if ran >= 1:
    print(first)
if ran >= 2:
    print(second)
if ran >= 3:
    print(third)

for i in range(3, ran+1):
    new = first+second+third
    print(new)
    first = second
    second = third
    third = new