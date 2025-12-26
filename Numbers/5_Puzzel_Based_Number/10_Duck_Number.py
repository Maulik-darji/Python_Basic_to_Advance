def duck(n):
    check = n

    while check>0:
        digit = check%10
        if  digit == 0:
            return True
        check = check//10
    return False

x = int(input("Enter Number: "))
print("Duck Number" if duck(x) else "Not Duck Number")