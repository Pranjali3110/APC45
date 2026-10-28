# 5. Uppercase and Lowercase Count
# Question: Count the number of uppercase and lowercase letters in a string.

s = input("Enter a string: ")

upper = lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase =", upper)
print("Lowercase =", lower)