# 1. String Length
# Question: Write a program to input a string and display its length without using the len() function.

s = input("Enter a string: ")

count = 0
for ch in s:
    count += 1

print("Length =", count)