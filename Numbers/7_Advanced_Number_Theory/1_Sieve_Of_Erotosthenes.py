def siv(n):
    number = []
    for i in range(2,n+1):
        number.append(i)
    for i in number:
        for j in range(i*2, n+1, i):
            if j in number:
                number.remove(j)
    return number
n = int(input("Enter Number: "))
print("Prime Numbers Are: ")
print(siv(n))