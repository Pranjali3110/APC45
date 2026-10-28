# Q8. Write a PYTHON program to print Fibonacci series up to n.

n = int(input("Enter n: "))

a = 0
b = 1

while a <= n:
    print(a)
    c = a + b
    a = b
    b = c