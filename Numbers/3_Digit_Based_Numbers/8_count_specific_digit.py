n = (input("Enter Number: "))
x = (input("Enter Digit to Count: "))

count = 0

for i in n:
    if i == x:
        count += 1
if count > 0:
    print(count)
else:
    print("Digit Not Found")