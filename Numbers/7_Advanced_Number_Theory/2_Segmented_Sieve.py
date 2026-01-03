def seg_siv(L,R):
    segment=[]
    for i in range(L, R+1):
        segment.append(i)
    for i in range(2, int(R**0.5)+1):
        for j in range(i*2, R+1,i):
            if j in segment:
                segment.remove(j)
        if j in segment:
            segment.remove(1)
        return segment
L = int(input("Enter L: "))
R = int(input("Enter R: "))
print("Prime Numbers In Range: ")
print(seg_siv(L,R))