#Print Fibonacci series up to given term.
n = int(input("Enter number of terms: "))
a = 0
b = 1
if n <= 0:
    print("Enter a positive number")
elif n == 1:
    print(a)
else:
    print(a, b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
