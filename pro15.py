# Q15. Write a PYTHON program to print the largest of n numbers.

n = int(input("How many numbers: "))

i = 1
largest = None

while i <= n:
    num = int(input("Enter number: "))

    if largest is None or num > largest:
        largest = num

    i += 1

print("Largest number =", largest)