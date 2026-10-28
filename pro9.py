# Q9. Write a PYTHON program to find a factorial of given number.

n = int(input("Enter a number: "))

fact = 1
i = 1

while i <= n:
    fact = fact * i
    i += 1

print("Factorial =", fact)