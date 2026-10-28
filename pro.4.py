# 4. Palindrome Check
# Question: Check whether the entered string is a palindrome.

s = input("Enter a string: ")

reverse = ""

for ch in s:
    reverse = ch + reverse

if s == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")