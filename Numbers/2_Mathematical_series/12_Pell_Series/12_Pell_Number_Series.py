def pell(ran):
    a = 0
    b = 1

    if ran >= 1:
        print(a)
    if ran >= 2:
        print(b)

    for i in range(2, ran):
        new = 2*b + a
        print(new)
        a = b
        b = new
ran = int(input("Enter Range: "))
pell(ran)
