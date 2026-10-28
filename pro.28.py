# Q28. Word Frequency Dictionary
# Count the frequency of every word in a paragraph.

paragraph = input("Enter a paragraph: ")

words = paragraph.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

for word in frequency:
    print(word, "=", frequency[word])