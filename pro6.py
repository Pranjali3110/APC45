# Q6. Write a PYTHON program to print sum of even numbers up to n.

n = int(input("Enter n: "))

i = 2
sum = 0

while i <= n:
    sum = sum + i
    i += 2

print("Sum of even numbers =", sum)