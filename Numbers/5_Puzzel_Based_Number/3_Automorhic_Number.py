def automorphic(n):
    x = n*n
    y = len(str(n))
    last_part = x%(10**y)
    return last_part == n
num = int(input("Enter Number: "))
if automorphic(num):
    print("Automophic Number")
else:
    print("Not Automorhpic Number")