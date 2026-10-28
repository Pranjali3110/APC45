# 3. Reverse a String
# Question: Reverse the given string without using built-in reverse functions.

s = input("Enter a string: ")

reverse = ""

for ch in s:
    reverse = ch + reverse

print("Reverse =", reverse)