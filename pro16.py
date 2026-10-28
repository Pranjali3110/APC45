# Q16. Write a PYTHON program to print the smallest of n numbers.

n = int(input("How many numbers: "))

i = 1
smallest = None

while i <= n:
    num = int(input("Enter number: "))

    if smallest is None or num < smallest:
        smallest = num

    i += 1

print("Smallest number =", smallest)