ran = int(input("Enter range to print Fibonacci series: "))

first = 0
second = 1

if ran >= 1:
    print(first)
# we use the >= to force the loop to print the 1 always hence if any number will be greater than that then along with all the numbers the first will also get print, and same for the second.
if ran >= 2:
    print(second)

for i in range(3, ran + 1):
    new = first + second
    print(new)
    first = second
    second = new
