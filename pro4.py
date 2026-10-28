# Q4. Write a PYTHON program to print sum of natural numbers up to n.

n = int(input("Enter n: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i += 1

print("Sum =", sum)