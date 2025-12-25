def find_odd_occuring(arr):
    resut = 0
    for num in arr:
        result ^= num
    return result
arr = [1,2,3,2,3,1,3]
print("Odd Occuring Element: ", find_odd_occuring(arr))
