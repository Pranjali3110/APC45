# Q14. Write a PYTHON program to print the multiplication table.

n = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1