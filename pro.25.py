# Q25. Second Most Frequent Character
# Find the second most frequently occurring character.

s = input("Enter a string: ")

frequency = {}

for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1

counts = sorted(set(frequency.values()), reverse=True)

if len(counts) >= 2:
    second_count = counts[1]

    for ch in frequency:
        if frequency[ch] == second_count:
            print("Second most frequent character =", ch)
            break
else:
    print("No second most frequent character")