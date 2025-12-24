print("\t1. Decimal\n\t2. Binary\n\t3. Hex\n\t4. Octal")
In = int(input("Select Input Number System: "))

print("\t1. Decimal\n\t2. Binary\n\t3. Hex\n\t4. Octal")
out = int(input("Select Output Number System: "))

num = input("Enter the number: ")

# Step 1: Convert input number to decimal
if In == 1:          # Decimal
    decimal = int(num)
elif In == 2:        # Binary
    decimal = int(num, 2)
elif In == 3:        # Hexadecimal
    decimal = int(num, 16)
elif In == 4:        # Octal
    decimal = int(num, 8)
else:
    print("Invalid Input System")
    exit()

# Step 2: Convert decimal to output system
if out == 1:
    result = decimal
elif out == 2:
    result = bin(decimal)[2:]
    #2: removes the ob from the binary number, ob1010 for decimal 10
elif out == 3:
    result = hex(decimal)[2:]
elif out == 4:
    result = oct(decimal)[2:]
else:
    print("Invalid Output System")
    exit()

print("Converted Result:", result)
