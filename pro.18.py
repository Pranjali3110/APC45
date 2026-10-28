# Q18. Write a program to remove duplicate characters while maintaining the original order.

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch

print("After removing duplicates =", result)