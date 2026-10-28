# Q24. Most Frequent Character
# Find the character with the highest frequency.

s = input("Enter a string: ")

most = s[0]
max_count = s.count(s[0])

for ch in s:
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        most = ch

print("Character:", most)
print("Frequency:", max_count)