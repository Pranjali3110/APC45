# Q15. Write a program to print all duplicate characters in a string.

s = input("Enter a string: ")

for ch in set(s):
    if s.count(ch) > 1:
        print(ch)