def find_odd_occuring(arr):
    result = 0
    for num in arr:
        result = result ^ num
    return result
x = int(input("Enter Input Range: "))
arr = []
for i in range(x):
    digit = int(input(f"Enter Number {i+1}: "))
    arr.append(digit)
print("Odd Occuring Element: ", find_odd_occuring(arr))