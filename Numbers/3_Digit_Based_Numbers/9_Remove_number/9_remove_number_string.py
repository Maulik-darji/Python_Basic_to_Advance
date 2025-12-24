n = input("Enter Number: ")
d = input("Enter Digit to Remove: ")

result = n.replace(d, "")
if result == "":
    print(0)
else:
    print(int(result))