# Q19. Write a program to check whether a given substring exists in the main string.

s = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in s:
    print("Substring found")
else:
    print("Substring not found")