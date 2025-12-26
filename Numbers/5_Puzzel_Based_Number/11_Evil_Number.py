def evil(n):
    binary = bin(n)[2:]
    count = 0
    size = len(binary)

    i = 0
    while i<size:
        d = binary[i]
        if d == '1':
            count+=1
        i += 1
    return count%2 == 0
n = int(input("Enter Number: "))

print("Binary Number: ", bin(n)[2:])
print("Evil Number" if evil(n) else "Not Evil Number")