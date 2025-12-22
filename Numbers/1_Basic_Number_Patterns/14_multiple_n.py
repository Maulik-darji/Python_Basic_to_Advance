n = int(input("Enter Number to find Multiple: "))
ran = int(input("Enter Range: "))

for i in range(ran):
    x = n * (i+1)
    print(f"{x}")