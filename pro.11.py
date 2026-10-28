# 11. Word Count
# Question: Count the total number of words in a sentence.

s = input("Enter a sentence: ")

words = s.split()
count = 0

for word in words:
    count += 1

print("Total words =", count)