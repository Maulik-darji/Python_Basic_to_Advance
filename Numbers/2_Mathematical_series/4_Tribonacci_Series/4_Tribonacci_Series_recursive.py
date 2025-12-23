def Tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Tribonacci(n-1) + Tribonacci(n-2) + Tribonacci(n-3)
    
    