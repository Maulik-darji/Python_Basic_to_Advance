def count_set(n):
    count = 0
    while n>0:
        n = n & (n-1)
        count += 1
    return count
x = int(input("Enter Number: "))
print("Set Bits Presetn: ",count_set(x))