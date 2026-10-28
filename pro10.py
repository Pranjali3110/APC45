# Q10. Write a PYTHON program to check the entered number is prime or not.

n = int(input("Enter a number: "))

i = 2
count = 0

while i < n:
    if n % i == 0:
        count += 1
    i += 1

if n > 1 and count == 0:
    print("Prime Number")
else:
    print("Not a Prime Number")