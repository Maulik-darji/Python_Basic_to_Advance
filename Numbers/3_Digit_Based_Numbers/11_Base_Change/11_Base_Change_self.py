print("\t1. Decimal\n\t2. Binary\n\t3. Octal\n\t4. Hexadecimal")
In = int(input("Select Input Number System: "))

print("\t1. Decimal\n\t2. Binary\n\t3. Octal\n\t4. Hexadecimal")
Out = int(input("Select Output Number System: "))

x = int(input("Enter Number: "))

if In == 1:
    decimal = int(x)
elif In == 2:
    decimal = int(x, 2)
elif In == 3:
    decimal = int(x, 8)
elif In == 4:
    decimal = int(x, 16)
else:
    print("Invalid Input System")
    exit()

if Out == 1:
    result = decimal
elif Out == 2:
    result = bin(decimal)[2:]
elif Out == 3:
    result = oct(decimal)[2:]
elif Out == 4:
    result = hex(decimal)[2:]

print("Converted Number: ", result)